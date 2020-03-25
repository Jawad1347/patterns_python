num = 10
m = (num*2) -2
for i in range(0, num):
    for j in range(0, m):
        print(end=" ")
    m = m-1
    for j in range(0, i+1):
        print("*", end=" ")
    print(" ")

# not complete yet.
