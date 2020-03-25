a = input("Say something")
a = a.lower().strip()

for i in range(0, len(a)):
    for j in range(0, i):
        print(a[i-1], end="")
    print()

# I need to edit this to make it look good.
