from pico2d import *
import game_world
import game_framework

class Brick:
    image = None

    def __init__(self):
        if Brick.image == None:
            Brick.image = load_image('brick180x40.png')
        self.x, self.y = 1600 // 2, 200
        self.speed = 200
        self.dir = 1

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20 ###

    def draw(self):
        self.image.draw(self.x, self.y, 180, 40)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.speed * game_framework.frame_time * self.dir

        clamp(0, self.x, 1600)
        if self.x <= 100:
            self.dir = 1
            
        elif self.x >= 1450:
            self.dir = -1
