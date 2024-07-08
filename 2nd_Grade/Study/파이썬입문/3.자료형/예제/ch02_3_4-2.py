str = "Hello World!"
idx = str.index("World")

print("idx = {}".format(idx))

print(str[:idx])
print(str[idx:])

str2 = str[:idx] + "Python " + str[idx:]
print(str2)

print(str2[2:-3])