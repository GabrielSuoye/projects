def solveQuadratic(a, b, c):
    d = b * b - 4 * a * c
    x = (-b + (d**0.5)) / (2 * a)
    y = (-b - (d**0.5)) / (2 * a)
    return x, y


def getFinalVelocity(u, a, t):
    v = u + a * t
    return v


def getForce(m, a):
    f = m * a
    return f


def getReactionForce(f):
    return -f


print(solveQuadratic(1, -2, -3))
