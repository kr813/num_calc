# ニュートン法
# TODO: a,bの選び直し

import matplotlib.pyplot as plt

def f(x):
    return x ** 2 + 2 * x - 1  # 手計算の解は√2 - 1, -1 - √2

def f_diff(x):
    return 2 * x + 2

def main():
    epsilon = 0.1 ** 16
    n = 0
    WRITE = 1
    xlist = []

    x = 0
    
    while True:

        print("{}\t{}".format(n, x))
        xlist.append(x)

        if WRITE:
            with open('newton.txt', 'a') as w:
                w.write(str(n))
                w.write('\t')
                w.write(str(x))
                w.write('\n')

        x_old = x
        x = x - f(x) / f_diff(x)
        if abs(x_old - x) < epsilon:
            plt.plot(list(range(n+1)), xlist)
            plt.show()
            break

        n += 1

if __name__ == "__main__":
    main()