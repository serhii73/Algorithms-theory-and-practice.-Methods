import time


def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Your number is: "))
start_time = time.time()
our_rezult = fibonacci(n)
print(our_rezult)
print("--- %s seconds ---" % (time.time() - start_time))
