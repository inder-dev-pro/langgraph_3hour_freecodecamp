from typing import Optional

def name(n:Optional[str]):
    if n==None:
        print("Nothing is provided!")
    else:
        print("your name is:", n)

name(None)
name("Inder")