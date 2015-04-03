import turtle
    
def draw_sides(trtl, max_sides, length, angle):
    sides = 0
    while sides < max_sides:
        trtl.forward(length)
        trtl.right(angle)
        sides = sides + 1

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    draw_sides(brad, 4, 100, 90)
    

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    bob = turtle.Turtle()
    bob.color("yellow")
    bob.right(120)
    draw_sides(bob, 3, 100, 120)

def run():
    window = turtle.Screen()
    window.bgcolor("red")

    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick()

run()