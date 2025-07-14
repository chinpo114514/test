import random

Height = 100
x = random.randint(0,Height)
egg = 2
Budget = 10

while (egg > 0) and (Budget > 0):
    Expect = int(input("Expect:"))
    if Expect <= x:
        print("→Safe!")
    elif Expect > x:
        print("→Broken...")
        egg -= 1
    Budget -= 1

Answer = int(input("Guess:"))
if Answer == x:
    print("Cleared!")
else:
    print(f"GameOver...Answer:{x}")