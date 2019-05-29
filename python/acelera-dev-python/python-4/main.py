import math

def calc_angle_mbc(a, b):
    h = math.hypot(a, b)
    h = h / 2.0
    adj = b / 2.0
    
    return round(math.degrees(math.acos(adj/h)))

