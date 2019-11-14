from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

point = [
    ((random.randint(-100, 100+1)),((random.randint(-100,100+1)))),
    ((random.randint(-100, 100+1)),((random.randint(-100,100+1)))),
    ((random.randint(-100, 100+1)),((random.randint(-100,100+1)))),
    ((random.randint(-100, 100+1)),((random.randint(-100,100+1)))),
    ((random.randint(-100, 100+1)),((random.randint(-100,100+1)))),
    ((random.randint(-100, 100+1)),((random.randint(-100,100+1)))),
    ((random.randint(-100, 100+1)),((random.randint(-100,100+1)))),
    ((random.randint(-100, 100+1)),((random.randint(-100,100+1)))),
    ((random.randint(-100, 100+1)),((random.randint(-100,100+1)))),
    ((random.randint(-100, 100+1)),((random.randint(-100,100+1))))
]

global Doit

def handle_events():
    global running
    global endX, endY
    global nowX, nowY

    events = get_events()

    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            for i in range(0, 100, 2):
                t = i / 100
                nowX = ((-t ** 3 + 2 * t ** 2 - t) * point[1][0] + (3 * t ** 3 - 5 * t ** 2 + 2) * point[1][0]
                         + (-3 * t ** 3 + 4 * t ** 2 + t) * point[2][0] + (t ** 3 - t ** 2) * point[3][0]) / 2
                nowY = ((-t ** 3 + 2 * t ** 2 - t) * point[4][1] + (3 * t ** 3 - 5 * t ** 2 + 2) * point[1][1]
                         + (-3 * t ** 3 + 4 * t ** 2 + t) * point[2][1] + (t ** 3 - t ** 2) * point[3][1]) / 2

            # draw p2-p3
            for i in range(0, 100, 2):
                t = i / 100
                nowX = ((-t ** 3 + 2 * t ** 2 - t) * point[1][0] + (3 * t ** 3 - 5 * t ** 2 + 2) * point[2][0]
                         + (-3 * t ** 3 + 4 * t ** 2 + t) * point[3][0] + (t ** 3 - t ** 2) * point[4][0]) / 2
                nowY = ((-t ** 3 + 2 * t ** 2 - t) * point[1][1] + (3 * t ** 3 - 5 * t ** 2 + 2) * point[2][1]
                         + (-3 * t ** 3 + 4 * t ** 2 + t) * point[3][1] + (t ** 3 - t ** 2) * point[4][1]) / 2

            # draw p3-p4
            for i in range(0, 100, 2):
                t = i / 100
                nowX = ((-t ** 3 + 2 * t ** 2 - t) * point[2][0] + (3 * t ** 3 - 5 * t ** 2 + 2) * point[3][0]
                         + (-3 * t ** 3 + 4 * t ** 2 + t) * point[4][0] + (t ** 3 - t ** 2) * point[1][0]) / 2
                nowY = ((-t ** 3 + 2 * t ** 2 - t) * point[2][1] + (3 * t ** 3 - 5 * t ** 2 + 2) * point[3][1]
                         + (-3 * t ** 3 + 4 * t ** 2 + t) * point[4][1] + (t ** 3 - t ** 2) * point[1][1]) / 2

            # draw p4-p1
            for i in range(0, 100, 2):
                t = i / 100
                nowX = ((-t ** 3 + 2 * t ** 2 - t) * point[3][0] + (3 * t ** 3 - 5 * t ** 2 + 2) * point[4][0]
                         + (-3 * t ** 3 + 4 * t ** 2 + t) * point[1][0] + (t ** 3 - t ** 2) * point[2][0]) / 2
                nowY = ((-t ** 3 + 2 * t ** 2 - t) * point[3][1] + (3 * t ** 3 - 5 * t ** 2 + 2) * point[4][1]
                         + (-3 * t ** 3 + 4 * t ** 2 + t) * point[1][1] + (t ** 3 - t ** 2) * point[2][1]) / 2


open_canvas(KPU_WIDTH, KPU_HEIGHT)
character = load_image('animation_sheet.png')
kpu_ground = load_image('KPU_GROUND.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
nowX, nowY = KPU_WIDTH // 2, KPU_HEIGHT // 2
end_x = nowX
end_y = nowY

frame = 0
show_cursor()

while running:

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    character.clip_draw(frame * 100, 100, 100, 100, nowX, nowY)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()

close_canvas()
