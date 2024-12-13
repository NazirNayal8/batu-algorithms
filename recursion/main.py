
# def add_one(n):
#     x = 1
#     return n + x

# print(add_one(5))

# def factorial(n):
#     x = n
#     while x>1:
#         x = x-1
#         n = n*x
#     return n
# #n! = (n-1)!*n
# def factorial_rec(n):
#     return n * factorial_rec(n-1) if n > 1 else 1

# print(factorial(15))
# print(factorial_rec(15))

# f(0) = 0
# f(1) = 1
# f(n) = f(n-1) + f(n-2)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# 0, 1, 2, 3, 4, 5, 6, 7,  8,  9
def fibonacci_rec(n):
    if n < 2:
        return n
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)
#0(2^n)
def fibonacci(n):
    prev = 1
    before_prev = 0
    f = 0
    for i in range(2, n + 1):
        f = prev + before_prev
        before_prev = prev
        prev = f
    return f
#0(n)
# new technique: memoization


MAX_N = 1000
memo = [-1] * MAX_N # [-1, -1, -1, -1, -1, -1, -1, -1, -1, ..., -1]

# if mem[n] is equal -1, this means that we have not calculated the value of f(n) yet
# if mem[n] is different from -1, this means that we have already calculated the value of f(n)

def fibonacci_memo(n):

    if n < 2:
        return n
    
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)

    return memo[n]
#0(n)


# compare the exection time of the two functions
import time
print(0.1+0.2)
# n = 9

# start = time.time()
# fibonacci_rec(n)
# end = time.time()
# print("Recursive", end - start)

# start = time.time()
# fibonacci(n)
# end = time.time()
# print("Iterative", end - start)
        
# create a plot that shows how speed changes with n
# import matplotlib.pyplot as plt

# n = 30
# x = list(range(n))
# y1 = []
# y2 = []
# y3 = []
# for i in range(n):
#     start = time.time()
#     fibonacci_rec(i)
#     end = time.time()
#     y1.append(end - start)
#     start = time.time()
#     fibonacci(i)
#     end = time.time()
#     y2.append(end - start)
#     start = time.time()
#     fibonacci_memo(i)
#     end = time.time()
#     y3.append(end - start)

# plt.plot(x, y1, label="Recursive")
# plt.plot(x, y2, label="Iterative")
# plt.plot(x, y3, label="Memoization")
# plt.legend()
# plt.show()
#1.616
