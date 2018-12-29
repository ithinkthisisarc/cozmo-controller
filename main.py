import cozmo
from cozmo.util import distance_mm, speed_mmps, degrees
import inputs
from inputs import get_gamepad
import random

roasts = [
    "you so fat even a black hole can't suck you in",
    "you so stupid you got locked out of a motorcycle",
    "you should be an astronaut... on a one way trip to pluto",
    "you so fat even dora couldn't explore ya"
]

def main(robot: cozmo.robot.Robot):
    print(f"\n---------------------------\n\nStarting robot as {robot}\n\n")
    robot.say_text("Starting manual control").wait_for_completed()
    robot.drive_off_charger_contacts().wait_for_completed()
    robot.drive_straight(distance_mm(100), speed_mmps(200)).wait_for_completed()
    while 1:
        events = get_gamepad()
        for event in events:
            if event.code == "BTN_SOUTH" and event.state == 1:
                print("[inputs]", event.code, event.state, "\n  >SMASHING\n")
                robot.set_lift_height(1, 0, 0, 0).wait_for_completed()
                robot.set_lift_height(0, 0, 0, 0).wait_for_completed()

            if event.code == "BTN_WEST" and event.state == 1:
                print("[inputs]", event.code, event.state, "\n  >ROASTED")
                rand = random.randint(0,len(roasts)-1)
                print(f"rand is {rand}")
                robot.say_text(roasts[rand]).wait_for_completed()


            if event.code == "ABS_HAT0Y" and event.state == -1:
                print("[inputs]", event.code, event.state, "\n  >LIFTING UP\n")
                robot.set_lift_height(1, 5, 0, 0).wait_for_completed()
            elif event.code == "ABS_HAT0Y" and event.state == 1:
                print("[inputs]", event.code, event.state, "\n  >LIFTING DOWN\n")
                robot.set_lift_height(0, 5, 0, 0).wait_for_completed()

            if event.code == "ABS_Y" and event.state >= 3000:
                print("[inputs]", event.code, event.state, "\n  >DRIVING FORWARD\n")
                robot.drive_straight(distance_mm(300), speed_mmps(200)).wait_for_completed()
            elif event.code == "ABS_Y" and event.state <= -3000:
                print("[inputs]", event.code, event.state, "\n  >LIFTING BACKWARD\n")
                robot.drive_straight(distance_mm(-300), speed_mmps(200)).wait_for_completed()
            
            if event.code == "ABS_RX" and event.state >= 3000:
                print("[inputs]", event.code, event.state, "\n  >TURNING RIGHT\n")
                robot.turn_in_place(degrees(-45)).wait_for_completed()
            elif event.code == "ABS_RX" and event.state <= -3000:
                print("[inputs]", event.code, event.state, "\n  >TURNING LEFT\n")
                robot.turn_in_place(degrees(45)).wait_for_completed()

cozmo.run_program(main)