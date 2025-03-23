import math

def Y(x):
    return math.exp(x)

def f(x,y):
    return y

def euler_num_appro(h):
    x0 = 0
    y0 = 1
    # h = 0.05
    b = x0 + 2
    print("================= ")
    print("h = ", h)
    print("----------------- ")
    while x0 < b:
        xi = x0 + h
        yi = y0 + h * f(x0, y0)
        print(f"xi: {xi:5.3f} | yi: {yi:10.6f} | Yi: {Y(xi):10.6f}|   Yi-yi: {Y(xi) - yi:15.6f}")
        x0 = xi
        y0 = yi
euler_num_appro(0.05)
euler_num_appro(0.1)
