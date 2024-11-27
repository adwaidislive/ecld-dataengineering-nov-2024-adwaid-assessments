# Track the Robot (Part 1)
"""
A robot has been given a list of movement instructions. Each instruction is either left, right, up or down, followed by a distance to move. The robot starts at [0, 0]. You want to calculate where the robot will end up and return its final position as a list.

To illustrate, if the robot is given the following instructions:

["right 10", "up 50", "left 30", "down 10"]
It will end up 20 left and 40 up from where it started, so we return [-20, 40].
"""

def track_robot(instructions):
    val = [0,0]
    for i in instructions:
        f = i.split(" ")
        f[1]=int(f[1])
        if (f[0] == 'right'):
            val[0] += f[1]
        elif (f[0] == 'left'):
            val[0] -= f[1]
        elif (f[0] == 'up'):
            val[1] += f[1]
        elif (f[0] == 'down'):
            val[1] -= f[1]

    return val

