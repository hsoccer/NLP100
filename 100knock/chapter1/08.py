def cipher(x):
    res =""
    for i in range(len(x)):
        if "a" <= x[i] <= "z":
            res += chr(219 - ord(x[i]))
    return res

print(cipher("I have a pen."))
