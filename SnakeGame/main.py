from turtle import *
import time
import random

score=0
execution_delay=0.1

root=Screen() #object of screen class
root.title('Snake Game')
root.setup(width=600,height=600)
root.bgcolor('black')
root.bgpic('border.gif')
root.tracer(False)
root.addshape('upmouth.gif')
root.addshape('food.gif')
root.addshape('downmouth.gif')
root.addshape('leftmouth.gif')
root.addshape('rightmouth.gif')
root.addshape('body5.gif')

head=Turtle()
head.shape('upmouth.gif')
head.penup()
head.goto(0,0)
head.direction='stop'

food=Turtle()
food.shape('food.gif')
food.penup()
food.goto(0,100)

text=Turtle()
text.penup()
text.goto(0,268)
text.hideturtle()
text.color('white')
text.write('Score:0',font=('courier',25,'bold'),align='center')

lost=Turtle()
lost.color('white')
lost.penup()
lost.hideturtle()

def move_snake():
    if head.direction=='up':
        y=head.ycor()
        y=y+20
        head.sety(y)

    if head.direction=='down':
        y=head.ycor()
        y=y-20
        head.sety(y)

    if head.direction=='right':
        x=head.xcor()
        x=x+20
        head.setx(x)

    if head.direction=='left':
        x=head.xcor()
        x=x-20
        head.setx(x)

def go_up():
    if head.direction!='down':
        head.direction='up'
        head.shape('upmouth.gif')

def go_down():
    if head.direction!='up':
        head.direction='down'
        head.shape('downmouth.gif')


def go_left():
    if head.direction!='right':
        head.direction='left'
        head.shape('leftmouth.gif')


def go_right():
    if head.direction!='left':
        head.direction='right'
        head.shape('rightmouth.gif')


root.listen()

root.onkeypress(go_up,'Up')
root.onkeypress(go_down,'Down')
root.onkeypress(go_left,'Left')
root.onkeypress(go_right,'Right')
segments=[]
while True:
    root.update()

    if head.xcor()>260 or head.xcor()<-260 or head.ycor()>260 or head.ycor()<-260:
        lost.write('Game Lost',align='center',font=('courier',34,'bold'))
        time.sleep(1)
        lost.clear()
        time.sleep(1)
        head.goto(0,0)
        head.direction='stop'
        for bodies in segments:
            bodies.goto(1000,1000)
        score=0
        execution_delay=0.1
        segments.clear()
        text.clear()
        text.write('Score:0',align='center',font=('courier',25,'bold'))




    if head.distance(food)<20:
        x=random.randint(-255,255)
        y=random.randint(-255,255)
        food.goto(x,y)
        execution_delay=execution_delay-0.003


        body=Turtle()
        body.penup()
        body.shape('body5.gif')
        segments.append(body)

        score=score+10
        text.clear()
        text.write(f'Score:{score}',font=('courier',25,'bold'),align='center')


#Suppose we have eaten 3 times food so inside the segments list we will have
    # 3 segments [1st segment,2nd segment,3rd segment]

    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)

    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)







    move_snake()

    for bodies in segments:
        if bodies.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'

            for bodies in segments:
                bodies.goto(1000,1000)

            segments.clear()
            score=0
            execution_delay=0.1
            lost.write('Game Lost', align='center', font=('courier', 34, 'bold'))
            time.sleep(1)
            lost.clear()

            text.clear()
            text.write('Score:0', align='center', font=('courier', 25, 'bold'))

    time.sleep(execution_delay)


