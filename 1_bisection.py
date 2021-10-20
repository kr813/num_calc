# 二分法

import time

def f(x):
    return x ** 2 + 2 * x - 1  # 手計算の解は√2 - 1, -1 - √2

def main():
    epsilon = 0.1 ** 6
    n = 0
    
    a = -5.0
    b = 5.0
    c_old = 0.191
    while True:
        c = (a + b) / 2

        print("{}\t{}\t{}".format(n, c, f(c)))

        with open('bisection.txt', 'a') as w:
            w.write(str(a))
            w.write('\t')
            w.write(str(b))
            w.write('\n')

        with open('bisection.txt', 'a') as w:
            w.write(str(n))
            w.write('\t')
            w.write(str(c))
            w.write('\t')
            w.write(str(f(c)))
            w.write('\n')

        if abs(f(c)) < epsilon or c_old == c:  # float型の範囲でcの値が変化しなかったらやめる
            break
        c_old = c

        if f(a) * f(b) < 0.0:
            b = c
        else:
            a = c

        n += 1

if __name__ == "__main__":
    main()