# Given we are on earth's surface.
a = -9.8 # km/h

# Equations of Constant Acceleration Motion

# Position
def x(t,v0=0,x0=0):
    x = x0 + v0 * t + 0.5 * a * pow(t,2)
    return x

# Velocity
def v(t,v0=0):
    pass