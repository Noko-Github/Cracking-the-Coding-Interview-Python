from enum import Enum


class Color(Enum):
    Black = 1
    White = 1
    Red = 1
    Yellow = 1
    Green = 1


def init_paint_fill(screen, r, c, ncolor):
    if screen[r][c] == ncolor:
        return False

    paint_fill(screen, r, c, screen[r][c], ncolor)


def paint_fill(screen, r, c, ocolor, ncolor):
    if r < 0 or c < 0 or len(screen) <= r or len(screen[0]) <= c:
        return False

    if screen[r][c] == ocolor:
        screen[r][c] = ncolor
        paint_fill(screen, r+1, c, ocolor, ncolor)
        paint_fill(screen, r-1, c, ocolor, ncolor)
        paint_fill(screen, r, c+1, ocolor, ncolor)
        paint_fill(screen, r, c-1, ocolor, ncolor)

    return True
