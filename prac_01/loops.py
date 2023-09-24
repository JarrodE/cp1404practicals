# 1
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# 2
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# 3
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# 4
n = int(input("Number of stars: "))

for i in range(n):
    print("*", end='')
print()

# 5
n = int(input("Number: "))

for i in range(n + 1):
    print("*" * i)
print()
