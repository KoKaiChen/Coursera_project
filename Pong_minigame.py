# Implementation of classic arcade game Pong

# Name: 柯凱程

# URL:https://py2.codeskulptor.org/#user51_Haj18Yss3Xjy6nK.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 10
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_pos = float(HEIGHT / 2)
paddle2_pos = float(HEIGHT / 2)
paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [2, 2]


# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]

    hor_v = random.randrange(120, 240) // 60  # pixels per second
    ver_v = random.randrange(60, 180) // 60

    if direction == LEFT:
        ball_vel = [-hor_v, ver_v]
    if direction == RIGHT:
        ball_vel = [hor_v, ver_v]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    spawn_ball(random.choice([RIGHT, LEFT]))


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] -= ball_vel[1]

    # keep paddle on screen
    paddle1_pos += paddle1_vel
    if paddle1_pos - HALF_PAD_HEIGHT < 0:
        paddle1_pos = HALF_PAD_HEIGHT
    if paddle1_pos + HALF_PAD_HEIGHT > HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    paddle2_pos += paddle2_vel
    if paddle2_pos - HALF_PAD_HEIGHT < 0:
        paddle2_pos = HALF_PAD_HEIGHT
    if paddle2_pos + HALF_PAD_HEIGHT > HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT

    # how to determine colab or not???
    # determine whether paddle and ball collide

    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] > paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] < paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] *= -1.1
            ball_vel[1] *= 1.1
        else:  # didnt collab
            score2 += 1
            spawn_ball(RIGHT)
    if ball_pos[0] >= (WIDTH - 1) - PAD_WIDTH - BALL_RADIUS:  # When arrive right
        if ball_pos[1] > paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] < paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] *= -1.1
            ball_vel[1] *= 1.1
        else:  # didnt collab
            score1 += 1
            spawn_ball(LEFT)

    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] *= -1

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Red", "Red")

    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel

    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos - HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT),
                         (PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT), (0, paddle1_pos + HALF_PAD_HEIGHT)],
                        1, "White", "White")
    canvas.draw_polygon([(WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH, paddle2_pos - HALF_PAD_HEIGHT),
                         (WIDTH, paddle2_pos + HALF_PAD_HEIGHT), (WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT)],
                        1, "White", "White")

    # draw scores
    canvas.draw_text(str(score1), (WIDTH / 2 - WIDTH / 4, 100), 50, 'White')
    canvas.draw_text(str(score2), (WIDTH / 2 + WIDTH / 4, 100), 50, 'White')


def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 10  # upper

    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 10  # lower

    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 10  # upper

    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 10  # lower


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart Game', new_game, 180)

# start frame
new_game()
frame.start()
