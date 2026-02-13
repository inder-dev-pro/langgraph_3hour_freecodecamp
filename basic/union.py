from typing import Union

def square(x : Union[int, float, str]) -> Union[float, str]:
    return x+x

x=3.14
print(square(x))

x=3

print(square(x))

x="Inder"

print(square(x))