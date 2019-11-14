from pico2d import *
import random

# Game object class here
# 잔디 클래스
# 클래스 내부에는 여러 개의 멤버함수로 구성된다
# init - 속성, 초기속성값 결정해줌. self 라는 인자를 가짐.
# draw - 행위
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        #self.frame = 0 # animation 상태 나타내기 위한 속성
        self.image = load_image('run_animation.png')

    def update(self): # 행위
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self): # 행위
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Small_ball:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 599
        self.speed = random.randint(3, 15) # 속도 조절
        self.image = load_image('ball21x21.png')

    def update(self):
        self.y -= self.speed

    def draw(self):
        if(self.y>=60):
            self.image.draw(self.x, self.y)
        else:
            self.image.draw(self.x, 60)

class Big_ball:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 599
        self.speed = random.randint(3, 15)
        self.image = load_image('ball41x41.png')

    def update(self):
        self.y -= self.speed

    def draw(self):
        if(self.y >= 70):
            self.image.draw(self.x, self.y)
        else:
            self.image.draw(self.x, 70)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

boy = Boy()
grass = Grass()
# List Comprehension ( 리스트를 빠르게 채우기 위한 방법 )
team = [Boy() for i in range(11)]

#공
cnt = random.randint(1, 20+1)
bigs = [Big_ball() for i in range(cnt)]
smalls = [Small_ball() for i in range(20-cnt)]

running = True

# game main loop code
while running:
    handle_events()

# update
    for boy in team:
        boy.update()

    for Big_ball in bigs:
        Big_ball.update()

    for Small_ball in smalls:
        Small_ball.update()

    clear_canvas()
    grass.draw()

# draw
    for boy in team:
        boy.draw()

    for Big_ball in bigs:
        Big_ball.draw()

    for Small_ball in smalls:
        Small_ball.draw()

    update_canvas()

    delay(0.05)

# finalization code
close_canvas()