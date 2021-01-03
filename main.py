
import requests

from map import *

if __name__ == "__main__":

    response2 = requests.get("http://api.open-notify.org/iss-now.json")
    position = response2.json()["iss_position"]

    latitude = position["latitude"]
    longitude = position["longitude"]

    earth = Map(float(latitude), float(longitude))
    earth.setup_screen()
    earth.plot()

    turtle.mainloop()
