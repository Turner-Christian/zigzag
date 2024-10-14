# program that makes a zigzag graphic in terminal
import sys, time

INDENT = 0
increasing = True

try:
    # loop
    while True:
        print(' ' * INDENT, end='')
        print('*' * 5)
        # delay
        time.sleep(0.03)
        if increasing:
            INDENT += 1
            if INDENT == 20:
                # start decreasing
                increasing = False
        else:
            INDENT -= 1
            if INDENT == 0:
                # start increasing
                increasing = True
except KeyboardInterrupt:
    sys.exit()