import turtle


class Map:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def setup_screen(self):
        screen = turtle.Screen()
        screen.title("Where is the International Space Station?")
        screen.setup(720, 360)
        screen.bgpic('map.gif')
        screen.setworldcoordinates(-180, -90, 180, 90)

        iss = turtle.Turtle()
        iss.shape("circle")
        iss.color("red")
        iss.penup()
        iss.goto(self.longitude, self.latitude)

        label = turtle.Turtle()
        label.hideturtle()
        label.penup()
        label.goto(self.longitude + 1, self.latitude - 4)
        label.write("ISS", align="center")

    def plot(self):
        station = turtle.Turtle()
        station.penup()
        station.goto(self.longitude, self.latitude)
        station.hideturtle()