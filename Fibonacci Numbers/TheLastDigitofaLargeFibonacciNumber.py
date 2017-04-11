import time

n = int(input("Your number is: "))
start_time = time.time()
if n < 7:
    print(n)
else:
    a = 13
    b = 21
    for i in range(7, n):
        a, b = b % 10, (a + b) % 10
    print(a)

print("--- %s seconds ---" % (time.time() - start_time))