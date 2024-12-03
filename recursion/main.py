
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

def fibonacci(n):
    prev = 1
    before_prev = 0
    f = 0
    for i in range(2, n + 1):
        f = prev + before_prev
        before_prev = prev
        prev = f
    return f


# compare the exection time of the two functions
import time

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
import matplotlib.pyplot as plt

n = 30
x = list(range(n))
y1 = []
y2 = []
for i in range(n):
    start = time.time()
    fibonacci_rec(i)
    end = time.time()
    y1.append(end - start)
    start = time.time()
    fibonacci(i)
    end = time.time()
    y2.append(end - start)

plt.plot(x, y1, label="Recursive")
plt.plot(x, y2, label="Iterative")
plt.legend()
plt.show()
#1.616
