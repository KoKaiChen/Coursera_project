# "Stopwatch: The Game"

# Name: 柯凱程

# URL:https://py2.codeskulptor.org/#user51_jAg1USaNlxVac8f.py

import simplegui

# define global variables
A = 0
B = 0
C = 0
D = 0
stop_time = 0
success_stop = 0
stop_record = "x/y"
time_screen = "0:00.0"


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()


def stop():
    global stop_time, success_stop, stop_record
    timer.stop()
    if D == 1:
        success_stop += 1
        stop_time += 1
    else:
        stop_time += 1
    stop_record = str(success_stop) + "/" + str(stop_time)
    print(stop_time, success_stop, D)


def reset():
    global A, B, C, D, time_screen, stop_record, stop_time, success_stop
    A = 0
    B = 0
    C = 0
    D = 0
    time_screen = "0:00.0"
    stop_record = "0/0"
    stop_time = 0
    success_stop = 0


# define event handler for timer with 0.1 sec interval
def tick():
    global A, B, C, D, time_screen
    time_screen = str(A) + ":" + str(B) + str(C) + "." + str(D)
    print(time_screen)
    if D == 9:
        C += 1
        D = 0
    elif C == 9:
        B += 1
        C = 0
        D = 0
    elif B == 6 and C == 0:
        A += 1
        B = 0
        C = 0
        D = 0
    else:
        D += 1


# define draw handler
def draw(canvas):
    canvas.draw_text(time_screen, [80, 100], 24, "White")
    canvas.draw_text(stop_record, [160, 30], 24, "White")


# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 200)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# register event handlers
timer = simplegui.create_timer(100, tick)

# draw handler
frame.set_draw_handler(draw)

# start frame
frame.start()

# Timer should stop at beginning
timer.stop()

# Please remember to review the grading rubric
