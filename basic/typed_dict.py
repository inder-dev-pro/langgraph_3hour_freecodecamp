from typing import TypedDict

class Movie(TypedDict):
    name:str
    year:int

movie=Movie(name="Avengers", year=2026)

print(movie)