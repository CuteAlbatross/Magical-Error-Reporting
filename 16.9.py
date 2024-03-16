count = 0
a = 0
def add(n):
    global count, a
    a += 1
    if a != 101:
        count += n
        add(n+1)
add(1)
print(count)
