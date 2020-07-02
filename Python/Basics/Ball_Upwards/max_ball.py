# Given we are on earth's surface.
a = -9.81 # m/s**2

def kmh_to_mps(kmh):
    '''
    converts kmh to metres per second
    '''
    return kmh * (10 / 36)

def rectify_error(t,v0):
    '''
    We contemplate 0.1 seconds error in v measurements
    '''
    positions = {
        t-0.1: position(t-0.1,v0),
        t: position(t,v0),
        t+0.1: position(t+0.1,v0)
    }
    sorted_pos = sorted(positions.items(), key=lambda pos: pos[1]) # list of tupples (t,pos)
    return sorted_pos[-1][0]

# Equations of Constant Acceleration Motion

# Position
def position(t,v0=0,x0=0):
    x = x0 + v0 * t + 0.5 * a * pow(t,2)
    return x

# Velocity
def velocity(t,v0=0):
    v = v0 + a * t
    return v

def max_ball(v0):
    v0 = kmh_to_mps(v0) # convert from kmh to metres per second, v0 is in kmh
    '''
    When the ball reaches the maximum height is when
    v = 0, from the equations we know that this
    happens in t = abs(v0 / a)
    due to limitations on our sensors we only can record 0.1 sec interval
    '''

    # initial conditions of the experiment
    v = v0
    t = 0.1

    while(v >= 0):
        v = velocity(t,v0)
        t = t + 0.1 # increase time to the next instant

    t = t - 0.1 # rectify time

    t = rectify_error(t,v0)
    # x_max = position(t,v0) max position recorded

    return t * 10 # return the time in tenth of a second


def test_max_ball():
    assert max_ball(37) ==  10
    assert max_ball(45) ==  13
    assert max_ball(99) ==  28
    assert max_ball(85) ==  24