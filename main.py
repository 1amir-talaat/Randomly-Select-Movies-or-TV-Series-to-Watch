import os
import random
from rich import print


while True:
    print(
        "[green]What do you want to watch?\n   [red]1 [cyan]-> [blue]Movie\n   [red]2 [cyan]-> [blue]Series"
    )
    print("[green]Please enter the number: ", end="")
    ch = input()

    if ch == "1":
        dir = "F:\Movies"
        break
    elif ch == "2":
        dir = "F:\Series"
        break

with open("watched.txt", "r") as file:
    watched = file.readlines()

watched = [i.replace("\n", "") for i in watched]

def get_movie():
    path = os.listdir(dir)
    path = [i for i in path if os.path.isdir(dir + "\\" + i)]

    while True:
        movie = random.choice(path)
        if movie not in watched:
            print(f"[green]{movie} [cyan]-> [blue]F:\Movies\{movie}")
            return movie
        else:
            continue

movie = get_movie()
while True:
    print("[yellow]Are you going to watch it? (y/n): ", end="")
    inp = input("")
    if inp.lower() == "y":
        with open("watched.txt", "a+") as file:
            file.write(f"\n{movie}")
        print("[green]Okay, enjoy.")
        break
    elif inp.lower() == "n":
        movie = get_movie()
        continue
    else:
        print("[red]Please enter (y/n) only!")