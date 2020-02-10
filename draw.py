from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if (x0 > x1):
        draw_line(x1, y1, x0, y0, screen, color)
    else:
        A = y1 - y0
        B = -1 * (x1 - x0)
        if (B == 0):
            while (y0 <= y1):
                plot(x0, y0, screen, color)
                y0 = y0 + 1
    else:
        slope = -1 * (A / B)
        # octant 1
        if (slope > 0):
            d = 2 * A + B
