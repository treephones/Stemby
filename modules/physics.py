import math
from utils.mathutils import quadratic

to_name = {
    "a": "Acceleration",
    "d": "Displacement",
    "t": "Time",
    "v1": "Initial Velocity",
    "v2": "Final Velocity"
}

big5s = {
    "d t v1 v2": {
        "d": lambda t, v1, v2: ((v1+v2)*t)/2,
        "t": lambda d, v1, v2: (2*d)/(v1+v2),
        "v1": lambda d, t, v2: ((2*d)/t)-v2,
        "v2": lambda d, t, v1: ((2*d)/t)-v1
    },
    "a t v1 v2": {
        "a": lambda t, v1, v2: (v2-v1)/t,
        "t": lambda a, v1, v2: (v2-v1)/a,
        "v1": lambda a, t, v2: v2-(a*t),
        "v2": lambda a, t, v1: v1+(a*t)
    },
    "a d t v1": {
        "a": lambda d, t, v1: (2*(d-(v1*t)))/t**2,
        "d": lambda a, t, v1: (v1*t)+((a*(t**2))/2),
        "t": lambda a, d, v1: quadratic((1/2)*a, v1, -d),
        "v1": lambda a, d, t: (d-((a*(t**2))/2))/t
    },
    "a d t v2": {
        "a": lambda d, t, v2: -((2*(d-(v2*t)))/t**2),
        "d": lambda a, t, v2: (v2*t)-((a*(t**2))/2),
        "t": lambda a, d, v2: quadratic(-(1/2)*a, v2, -d),
        "v2": lambda a, d, t: (d+((a*(t**2))/2))/t
    },
    "a d v1 v2": {
        "a": lambda d, v1, v2: ((v2**2)-(v1**2))/(2*d),
        "d": lambda a, v1, v2: ((v2**2)-(v1**2))/(2*a),
        "v1": lambda a, d, v2: math.sqrt((v2**2)-(2*a*d)),
        "v2": lambda a, d, v1: math.sqrt((v1**2)+(2*a*d))
    }
}

def kinematics(vars, find, pairs):
    try:
        ans = big5s[vars][find](pairs[0], pairs[1], pairs[2])
        if ans == None:
            raise ValueError
        ret = f"{to_name[find]}: {round(ans, 2)}" #CRASHES WHEN PASSED TUPLE!!
    except KeyError:
        return ("One or more of the motion variables was not valid! \n NOTE: " \
              "```\nAcceleration = a\nDisplacement = d\nTime = t\nInitial Velocity = v1\nFinal Velocity = v2\n```", False)
    except ValueError:
        return ("Unable to perform that calculation!", False)
    return (ret, True)

if __name__ == "__main__":
    print(big5s["a d t v2"]["d"](3,5,12))