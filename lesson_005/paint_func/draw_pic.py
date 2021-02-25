
def draw_pic():
    import simple_draw as sd
    from .house import house
    from .snowfall import snow_rain
    from .fractal import draw_branches
    from .smile import chel
    from .sun import sun
    sd.resolution = (1200, 800)
    sun()
    house()
    chel(1100, 230, sd.COLOR_DARK_YELLOW)
    point_root = sd.get_point(900, 80)
    draw_branches(point=point_root, angle=90, length=70)
    snow_rain()
    sd.pause()