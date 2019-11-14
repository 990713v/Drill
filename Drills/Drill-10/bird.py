import game_framework
from pico2d import *

import game_world

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # km / hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 400       
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = RUN_SPEED_PPS
        self.frame_x = 0
        self.frame_y = 0
        self.frame_time = 0
        self.current_time = time.time()

    def update(self):
        self.x += self.velocity * game_framework.frame_time
        self.frame_x = int(self.frame_time) % 5
        self.frame_time = (self.frame_time + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        
        if self.x < 100:
            self.dir = 1
            self.velocity = RUN_SPEED_PPS
        elif self.x > 1500:
            self.dir = -1
            self.velocity = -RUN_SPEED_PPS


        if int(self.frame_time) % 14 == 10:
            self.frame_y = 0
        elif int(self.frame_time) % 14 == 5:
            self.frame_y = 1
        elif int(self.frame_time) % 14 == 0:
            self.frame_y = 2
        

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.framex) * 183, int(self.framey) * 168, 180, 168, self.x, self.y, 180, 165)

        elif self.dir == -1:
            self.image.clip_composite_draw(int(self.framex) * 183, int(self.framey) * 168, 180, 168, 0.0, 'h', self.x, self.y, 180, 165)
            
        # get_time(): 시간 획득 함수. Canvas 열린 시점시간 0.0 부터 시작

