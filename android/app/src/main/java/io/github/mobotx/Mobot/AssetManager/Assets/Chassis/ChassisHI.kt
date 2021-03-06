//MIT License
//
//Copyright (c) 2021 Mobotx
//
//Permission is hereby granted, free of charge, to any person obtaining a copy
//of this software and associated documentation files (the "Software"), to deal
//in the Software without restriction, including without limitation the rights
//to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
//copies of the Software, and to permit persons to whom the Software is
//furnished to do so, subject to the following conditions:
//
//The above copyright notice and this permission notice shall be included in all
//copies or substantial portions of the Software.
//
//THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
//IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
//FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
//AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
//LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
//OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
//SOFTWARE.

package io.github.mobotx.Mobot.AssetManager.Assets.Chassis

import android.app.PendingIntent
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.hardware.usb.UsbDevice
import android.hardware.usb.UsbDeviceConnection
import android.hardware.usb.UsbManager
import android.util.Log
import com.felhr.usbserial.UsbSerialDevice
import com.felhr.usbserial.UsbSerialInterface
import io.github.mobotx.MainActivity

class ChassisHI(private val activity: MainActivity, val chassis: Chassis) {
    var available: Boolean = false // STATE VARIABLE
    var metadata:ChassisMetadata? = null // STATE VARIABLE

    private var usbManager: UsbManager = activity.getSystemService(Context.USB_SERVICE) as UsbManager
    private var usbDevice: UsbDevice? = null
    private var usbSerialDevice: UsbSerialDevice? = null
    private var usbDeviceConnection: UsbDeviceConnection? = null
    private val ACTION_USB_PERMISSION = "permission"

    class SerialReader(private val chassisHI: ChassisHI):UsbSerialInterface.UsbReadCallback{
        private var readLine:String = ""
        override fun onReceivedData(data: ByteArray?) {
            val msgChunk = String(data!!)
            for(ch in msgChunk){
                if(ch == '\r'){
                    parseLine()
                    readLine = ""
                }else if (ch != '\n'){
                    readLine += ch
                }
            }
        }
        private fun parseLine(){
            val readLineSplit = readLine.split(':')
            if(readLineSplit[0] == "METADATA"){
                val dataSplit = readLineSplit[1].split(',')
                try {
                    chassisHI.metadata = ChassisMetadata(
                            dataSplit[0].toFloat(),
                            dataSplit[1].toFloat(),
                            dataSplit[2].toFloat(),
                            dataSplit[3].toFloat())
                    chassisHI.available = true
                    chassisHI.chassis.chassisHIAvailable()
                }catch(e: Exception){
                    Log.d("Mobot", "$e")
                }
            }
        }
    }
    private var serialReader = SerialReader(this)

    private val broadcastReceiver = object : BroadcastReceiver(){
        override fun onReceive(context: Context?, intent: Intent?) {
            if (intent?.action!! == ACTION_USB_PERMISSION) {
                val granted: Boolean = intent.extras!!.getBoolean(UsbManager.EXTRA_PERMISSION_GRANTED)
                if (granted) {
                    usbDeviceConnection = usbManager.openDevice(usbDevice)
                    usbSerialDevice = UsbSerialDevice.createUsbSerialDevice(usbDevice, usbDeviceConnection)
                    if (usbSerialDevice != null) {
                        if (usbSerialDevice!!.open()) {
                            usbSerialDevice!!.setBaudRate(115200)
                            usbSerialDevice!!.setDataBits(UsbSerialInterface.DATA_BITS_8)
                            usbSerialDevice!!.setStopBits(UsbSerialInterface.STOP_BITS_1)
                            usbSerialDevice!!.setParity(UsbSerialInterface.PARITY_NONE)
                            usbSerialDevice!!.setFlowControl(UsbSerialInterface.FLOW_CONTROL_OFF)
                            usbSerialDevice?.read(serialReader)
                            usbSerialDevice?.write("GET:Metadata\r".toByteArray())
                        }
                    }
                }
            } else if (intent.action == UsbManager.ACTION_USB_DEVICE_ATTACHED) {
                startUsbConnecting()
                activity.beforeActivityRestarts()
            } else if (intent.action == UsbManager.ACTION_USB_DEVICE_DETACHED) {
                disconnect()
            }
        }
    }

    init {
        val filter = IntentFilter()
        filter.addAction(ACTION_USB_PERMISSION)
        filter.addAction(UsbManager.ACTION_USB_DEVICE_ATTACHED)
        filter.addAction(UsbManager.ACTION_USB_DEVICE_DETACHED)
        activity.registerReceiver(broadcastReceiver, filter)

        startUsbConnecting()
    }

    private fun startUsbConnecting() {
        var found = false
        val usbDevices = usbManager.deviceList
        if (!usbDevices?.isEmpty()!!) {
            usbDevices.forEach { _, dev ->
                if (!found) {
                    val deviceVendorId: Int? = dev?.vendorId
                    val productId: Int? = dev?.productId
                    val serialNumber = dev?.serialNumber
                    if (deviceVendorId == 4292 && productId == 60000 && serialNumber == "0001") {
                        usbDevice = dev
                        val intent: PendingIntent = PendingIntent.getBroadcast(activity, 0, Intent(ACTION_USB_PERMISSION), 0)
                        usbManager.requestPermission(usbDevice, intent)
                        found = true
                    }
                }
            }
        }
    }

    private fun disconnect() {
        available = false
        metadata = null
        chassis.chassisHIUnavailable()
        usbSerialDevice?.close()
    }

    fun setCmdVel(wr: Float, wl:Float){
        val msg = "CMDVEL:$wr,$wl\r"
        usbSerialDevice?.write(msg.toByteArray())
    }
}
