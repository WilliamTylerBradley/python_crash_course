from random import randint

class Dice:

    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self):
        result = randint(1, self.sides)
        print(f'{result}')

d_6 = Dice()

roll = 1
while roll <= 10:
    d_6.roll_dice()
    roll += 1

d_10 = Dice(10)
roll = 0
while roll <= 10:
    d_10.roll_dice()
    roll += 1

d_20 = Dice(20)
roll = 0
while roll <= 10:
    d_20.roll_dice()
    roll += 1

