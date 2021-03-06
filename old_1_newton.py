# ニュートン法
# TODO: a,bの選び直し
# 解が二つあるので，初期値によっては収束しなくなる．why?

def f(x):
    return x ** 2 + 2 * x - 1  # 手計算の解は√2 - 1, -1 - √2

def f_diff(x):
    return 2 * x + 2

def main():
    epsilon = 0.1 ** 16
    n = 0
    WRITE = 0

    x = 0
    
    while True:

        if WRITE:
            with open('newton.txt', 'a') as w:
                w.write(str(n))
                w.write('\t')
                w.write(str(x))
                w.write('\n')
        
        x = x - f(x) / f_diff(x)

        n += 1

if __name__ == "__main__":
    main()