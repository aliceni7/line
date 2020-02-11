from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
        A = y1 - y0
        B = -1 * (x1 - x0)
        if (B == 0):
            while (y0 <= y1):
                plot(screen, color, int(x0), int(y0))
                y0 = y0 + 1        
        elif (A == 0):
            while (x0 <= x1):
                plot(screen, color, int(x0), int(y0))
                x0 = x0 + 1
        else:
                slope = -1 * (A / B)
                # octant 1
                if (slope > 0 and slope <= 1):
                        d = 2 * A + B
                        while (x0 <= x1):
                                plot(screen, color, x0, y0)
                                if (d > 0):
                                        y0 = y0 + 1
                                        d = d + 2 * B
                                x0 = x0 + 1
                                d = d + 2 * A
                # octant 2
                if (slope > 1):
                        d = A + 2 * B
                        while (y0 <= y1):
                                plot(screen,color, x0, y0)
                                if (d < 0):
                                        x0 = x0 + 1
                                        d = d + 2 * A
                                y0 = y0 + 1
                                d = d + 2 * B
                # octant 3
                if (slope > -1 and slope < 0):
                        d = 2 * A - B
                        while ( x0 <= x1 ):
                                plot(screen, color, x0, y0)
                                if (d > 0):
                                        y0 = y0 - 1
                                        d = d + 2 * B
                                x0 = x0 + 1
                                d = d - 2 * A
                # octant 4
                if (slope <= -1):
                        d = A - 2 * B
                        while ( y0 >= y1 ):
                                plot(screen, color, x0, y0)
                                if (d < 0):
                                        x0 = x0 + 1
                                        d = d - 2 * A
                                y0 = y0 - 1
                                d = d + 2 * B
                
            
