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

import android.widget.ImageView
import io.github.mobotx.*
import io.github.mobotx.ChassisMetadata
import io.grpc.ManagedChannel
import io.grpc.StatusRuntimeException

class Chassis(private val activity: MainActivity) {
    private val chassisView: ImageView = activity.findViewById<ImageView>(R.id.chassis)

    var connected: Boolean = false // STATE VARIABLE

    val chassisHI = ChassisHI(activity, this)  // HOLDS STATE
    private lateinit var stub: ChassisGrpc.ChassisBlockingStub

    init {
        refreshUI()
    }

    fun start(channel: ManagedChannel){
        if (chassisHI.available) {
            connected = true
            stub = ChassisGrpc.newBlockingStub(channel)
            Thread(Runnable {
                getCmdVelStream()
            }).start()
            refreshUI()
        }
    }

    fun stop(){
        if(connected) {
            connected = false
            refreshUI()
        }
    }

    private fun getCmdVelStream(){
        try {
            val metadata = ChassisMetadata.newBuilder()
                    .setWheelDiameter(chassisHI.metadata!!.wheelDiameter)
                    .setWheelToWheelSeparation(chassisHI.metadata!!.wheelToWheelSeparation)
                    .setMaxWheelSpeed(chassisHI.metadata!!.maxWheelSpeed)
                    .setMinWheelSpeed(chassisHI.metadata!!.minWheelSpeed)
                    .build()
            val cmdVelIterator = stub.chassisCmdStream(metadata)
            cmdVelIterator.forEachRemaining{ cmdVel ->
                if (chassisHI.available) {
                    chassisHI.setCmdVel(cmdVel.wr, cmdVel.wl)
                }
            }
        }catch (e: Exception){
            if (chassisHI.available) {
                chassisHI.setCmdVel(0.toFloat(), 0.toFloat())
            }
            stop()
        }
    }

    fun chassisHIUnavailable(){
        stop()
        refreshUI()
    }

    fun chassisHIAvailable(){
        refreshUI()
    }

    fun refreshUI(){
        activity.runOnUiThread {
            if (chassisHI.available){
                chassisView.setImageResource(R.drawable.chassis_not_streaming)
                if (connected){
                    chassisView.setImageResource(R.drawable.chassis_streaming)
                }
            }else{
                chassisView.setImageResource(R.drawable.chassis_not_available)
            }
        }
    }
}
