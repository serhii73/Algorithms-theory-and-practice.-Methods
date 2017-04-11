import time

n = int(input("Your number is: "))
start_time = time.time()
if n <= 1:
    print(n)
else:
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    print(a)
print("--- %s seconds ---" % (time.time() - start_time))

# Your number is: 100000
# --- 0.3441460132598877 seconds ---
