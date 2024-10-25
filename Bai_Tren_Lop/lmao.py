n = 4
for i in range(1, n+1):
    output = ""
    for j in range(1, 11):
        if j * i < 10:
            output += " "
        output += " " + str(j * i)
    print(output)