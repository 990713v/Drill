from pico2d import *

import game_framework

class Pause:
    # Pause 클래스 초기화
    def __init__(self):
        self.image = load_image('pause.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 300, 500, 500)

def enter():
    global pause
    pause = Pause()

def exit():
    global pause
    del(pause)

def update():
    global pause
    pause.update()

def draw():
    global pause
    clear_canvas()
    pause.update()
    pause.draw()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        #pause 상태에서 p를 한번 더 누르면 이전상태로 복귀
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()

def pause():
    pass


def resume():
    pass
