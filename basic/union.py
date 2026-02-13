from typing import Union

def square(x : Union[int, float]) -> float:
    return x*x

x=3.14
print(square(x))

x=3

print(square(x))

