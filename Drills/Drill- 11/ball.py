import random
from pico2d import *
import game_world
import game_framework
from brick import Brick

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(150, 1450-1), 60, 0
        self.velocity = 0
        self.dir = 0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time
        if self.dir == 1:
            self.x += self.velocity * game_framework.frame_time
            if self.x >= 1450:
                self.dir = -1
        elif self.dir == -1:
            self.x -= self.velocity * game_framework.frmae_time
            if self.x <= 150:
                self.dir = 1

    def stop(self):
        self.fall_speed = 0
        self.velocity = 0


# fill here
class BigBall(Ball):
    MIN_FALL_SPEED = 50 # 50pps = 1.5 m/s
    MAX_FALL_SPEED = 200 # 200pps = 6 m/s
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1600-1), 500
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED,
                                         BigBall.MAX_FALL_SPEED)
        self.velocity = 0
        self.dir = 0

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
