import turtle

window = turtle.Screen()
window.setup(width=1000, height=800, startx=10, starty=0.5)
artist = turtle.Turtle() 
artist.shape("classic")

artist.penup()
artist.setpos(-390, 0)
artist.pendown()

current = 0   
seen = set()  

for step_size in range(1, 100):

    backwards = current - step_size
    if (backwards > 0) and (backwards not in seen):
        artist.setheading(90)  
        artist.circle(5 * step_size/2, 180)
        current = backwards
        seen.add(current)

    else:
        artist.setheading(270)
        artist.circle(5 * step_size/2, 180)
        current += step_size
        seen.add(current)

turtle.done()