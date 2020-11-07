import turtle

# create game window
wn = turtle._Screen()
wn.title("Pong by @lalitchilka")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Main game loop
while True:
    wn.update()