import time
n = int(input('Your number is: '))
start_time = time.time()
f = [0, 1]
for i in range(2, n+1):
    f.append(f[i-1]+f[i-2])
print(f[n])
print("--- %s seconds ---" % (time.time() - start_time))

# Your number is: >? 100000
# --- 0.9316315650939941 seconds ---

