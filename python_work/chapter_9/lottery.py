from random import choice

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

draw_1 = choice(lottery)
lottery.remove(draw_1)
draw_2 = choice(lottery)
lottery.remove(draw_2)
draw_3 = choice(lottery)
lottery.remove(draw_3)
draw_4 = choice(lottery)
lottery.remove(draw_4)
print(f'Winning tickets have: {draw_1}, {draw_2}, {draw_3}, {draw_4}!')

