def add(a,b):
    c = a+b
    return c

def my_sum(n):
    s = 0
    if n > 0:
        for i in range (n+1):
            s += i
    else:
        for i in range(n,1):
            s += i
    return s


# if __name__ == "__main__":
#     print(add(3,5))