def five():
    return 2


def double(x):
    return x * five()
    

print(double(2))
print(double(5))
print(double(76))
print(double(123))