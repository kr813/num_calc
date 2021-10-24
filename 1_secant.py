# セカント法

import matplotlib.pyplot as plt

WRITE = 0

def f(x):
    return x ** 2 + 2 * x - 1  # 手計算の解は√2 - 1, -1 - √2

def f_sub(xn, xn_1):
    return (xn - xn_1) / (f(xn) - f(xn_1))

def main():

    epsilon = 0.1 ** 16
    n = 0

    x = 1.0
    x_old = 0.0
    xlist = []

    while True:
        print("{}\t{}".format(n, x))
        xlist.append(x)

        if WRITE:
            with open('newton.txt', 'a') as w:
                w.write(str(n))
                w.write('\t')
                w.write(str(x))
                w.write('\n')
        
        tmp_x = x - f(x)*f_sub(x, x_old)
        x_old = x
        x = tmp_x

        if abs(x_old - x) < epsilon:
            plt.plot(list(range(n+1)), xlist)
            plt.show()
            break

        n += 1

if __name__ == "__main__":
    main()