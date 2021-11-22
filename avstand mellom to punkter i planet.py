# avstand mellom to punkter i planet vha pytagoras
# avstand mellom (x1, y1) og (x2, y2)
import math

def avstand(x1, y1, x2, y2):
    a = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    return a

print(avstand(2, 8, 9, 3))
