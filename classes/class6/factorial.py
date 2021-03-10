'''
n! = n * (n-1) * (n-2) * ... * 1
5! = 5 * 4 * 3 * 2 * 1
3! = 3 * 2 * 1 = 6
0! = 1
'''

'''
def fact(n):
    assert(n >= 0)

    result = 1
    for i in range(1, n+1):
        result = result * i

    return result
'''

# recursively
def fact(n):
    assert(n >= 0)

    if n == 0:
        return 1

    # recursion
    return n * fact(n-1)

if __name__ == '__main__':
    print(fact(1))
    print(fact(2))
    print(fact(3))
    print(fact(4))
    print(fact(5))