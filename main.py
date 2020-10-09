import turtle

def generate(n, result='[X]'):
    for _ in range(n):
        result = result.replace('F', 'FF')

        result = result.replace('X', 'F-[[X]+X]+F[+FX]-X')

    return result

def draw(chars, size=2):
    stack = []
    for ch in chars:
        if ch == 'F':
            turtle.forward(size)

        elif ch == '-':
            turtle.left(25)

        elif ch == '+':
            turtle.right(25)

        elif ch == 'X':
            pass

        elif ch == '[':
            stack.append((turtle.position(), turtle.heading()))

        elif ch == ']':
            position, heading = stack.pop()
            turtle.penup()
            turtle.setposition(position)
            turtle.setheading(heading)
            turtle.pendown()

        else:
            raise ValueError('Unknown char: {}'.format(ord(ch)))

    turtle.update()

def setup():
    turtle.hideturtle()
    turtle.tracer(1e3,0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0,-turtle.window_height()/2)
    turtle.pendown()

setup()
plant = generate(5)
draw(plant, 10)
turtle.exitonclick()