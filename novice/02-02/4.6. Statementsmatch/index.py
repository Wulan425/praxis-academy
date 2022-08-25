from ctypes.wintypes import POINT


def http_status(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 402 | 403:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"
print(http_status(404))


# point is an (x, y) tuple
match print:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError('Not a point')
class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point(): 
            print("Somewhere else")
        case _:
            print("Not a point")


match POINT:
    case []:
        print("No points")
    case [POINT(0, 0)]:
        print("The origin")
    case [POINT(x, y)]:
        print(f"Single point {x}, {y}")
    case _:
        print("Something else")

match print:
    case print(x, y) if x == y:
         print(f"Y=X at {x}")
    case print(x, y):
         print(f"Not on the diagonal")

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
print("I'm feeling the blues :(")






