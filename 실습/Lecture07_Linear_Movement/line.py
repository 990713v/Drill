#LEC07 직선이동 실습
import turtle
import random

def stop():
    turtle.bye()

def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    a = (y2 - y1)/(x2 - x1)
    b = y1 - x1*a
    for x in range(x1, x2+1, 10):
        y = a*x+b
        draw_point((x, y))

    draw_point(p2)

def draw_line(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    for i in range(0, 100+1, 2):
        t = i/100 #0~1사이 100으로나눔
        x=(1-t)*p1[0]+t*p2[0]
        y=(1-t)*p1[1]+t*p2[1]
        draw_point((x, y))

    draw_point(p2)

#prepare_turtle_canvas()
#draw_line_basic((-100, -100),(300, 150))
#turtle.done()


#prepare_turtle_canvas()
#draw_line((-200, -100),(300,150))
#turtle.done()


#### 여러개 선분 그리기 ###
#points = [(-300,200),(400,350),(300,-300),(-200,-200)]
#size = len(points)
#n=1
#prepare_turtle_canvas()
#while True:
#    draw_line(points[n-1],points[n])
#    n=(n+1)%size


#### 랜덤 선분 ###
points = [(random.randint(-500, 500), random.randint(-350, 350))for i in range(size)]
size = 6
n = 1
prepare_turtle_canvas()
while True:
    draw_line(points[n-1],points[n])
    n=(n+1)%size


# Python List Comprehension 중요함. .
# 리스트를 빠르게 만들기 위한 독특한 문법 구조
