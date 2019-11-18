import time

a = [i for i in range(1000000)]

c = time.time()
for i in range(1000000, 1001000):
    i in a

print(time.time() - c)


c = time.time()
a = set(a)
for i in range(1000000, 1001000):
    i in a

print(time.time() - c)
