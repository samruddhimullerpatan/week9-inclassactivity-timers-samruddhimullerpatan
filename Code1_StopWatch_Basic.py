from machine import Pin
import time
pb1=Pin(19,Pin.IN,Pin.PULL_UP)
pb2=Pin(14, Pin.IN, Pin.PULL_UP)

led1=Pin(25,Pin.OUT)

while True:
    
    val1=pb1.value()
    val2=pb2.value()
    
    if val1==0:
        start=time.ticks_ms()
        print(start)
        print("start estimating 5 seconds!")
        led1.on()
        
        time.sleep(0.1)
        
        
    if val2==0:
        end=time.ticks_ms()
        print(end)
        led1.off()
        
        d=time.ticks_diff(end,start)
        print(d)
        
        esti=5000-d
        print(esti)
        
        time.sleep(0.1)
