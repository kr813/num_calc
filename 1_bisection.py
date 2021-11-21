# 二分法
# TODO: a,bの選び直し
# 解が二つあるので，初期値によっては収束しなくなる．why?

import matplotlib.pyplot as plt

EQUATION = 1

def f(x):
    if EQUATION == 1:
        return x ** 2 + 2 * x - 1  # 手計算の解は√2 - 1, -1 - √2
    elif EQUATION == 2:
        return x

def main():
    epsilon = 0.1 ** 16
    n = 0
    c_old = 0.191
    WRITE = 1
    clist = []
    
    a = -100.0
    b = 100.0

    while True:
        c = (a + b) / 2
        clist.append(c)

        print("{}\t{}\t{}".format(n, c, f(c)))

        if WRITE:
            with open('bisection.txt', 'a') as w:
                w.write(str(n))
                w.write('\t')
                w.write(str(c))
                w.write('\t')
                w.write(str(f(c)))
                w.write('\n')
        
        if abs(f(c)) < epsilon or c_old == c:  # 欲しい精度になったとき，またはfloat型の範囲でcの値が変化しなかったら停止
            plt.plot(list(range(n+1)), clist)
            plt.show()
            break
        c_old = c

        if f(a) * f(c) < 0.0:
            b = c
        else:
            a = c

        n += 1

if __name__ == "__main__":
    main()