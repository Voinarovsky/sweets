import ev3dev2.motor as motor
import time
motor_a = motor.LargeMotor(motor.OUTPUT_A)
volar = [100, 80, 60, 40, 20, -20, -40, -60, -80, -100]
try:
    for vol in volar:
        startTime = time.time()
        startPos = motor_a.position
        name = "data" + str(vol) + ".txt"
        f = open(name, 'w')
        while (True):
            for i in range(10):
                currentTime = time.time() - startTime
                pos = motor_a.position - startPos
                motor_vel = motor_a.speed
                motor_a.run_direct(duty_cycle_sp = 10)
                motor_a.speedValue = 10
                f.write('{}, {}, {}\n'.format(currentTime, pos, motor_vel))
                f.close()
                motor_a.stop(stop_action='brake')
                if currentTime > 1:
                    break
            time.sleep(3)
except Exception as e:
    raise e 
finally:
    motor_a.stop(stop_action='brake')
