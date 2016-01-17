__author__ = 'cashsun'
from datetime import datetime

# this use less memory but slower
def fib(idx):
    if idx in (0, 1):
        return idx
    else:
        return fib(idx - 1) + fib(idx - 2)

# this use memory to cache generated ones but faster
memo = {0: 0, 1: 1}
def fibm(idx):
    if idx not in memo:
        memo[idx] = fibm(idx - 1) + fibm(idx - 2)
    return memo[idx]


# recursive solution - much faster
def fibi(idx):
    a, b = 0, 1
    for k in range(idx):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    index = 30
    start = datetime.now()
    print('generating fibonacci sequence up to...' + str(index) + '\n')

    for i in range(index):
        print('{}: {}'.format(i + 1, fib(i)))

    print('performance: ' + str(datetime.now() - start))

    start2 = datetime.now()
    for i in range(index):
        print('{}: {}'.format(i + 1, fibm(i)))
    print('performance2: ' + str(datetime.now() - start2))

    start3 = datetime.now()
    for i in range(index):
        print('{}: {}'.format(i + 1, fibi(i)))
    print('performance2: ' + str(datetime.now() - start3))
