from gpiozero import MotionSensor

pir = MotionSensor(4)

while True:
        try:
            pir.wait_for_motion()
            print("We're moving")

            pir.wait_for_no_motion()
            print('no motion')
        except:
            break    
pir.close()
