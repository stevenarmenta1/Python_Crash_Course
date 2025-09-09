from random import choice

lottery_nums = ('2', '1', '34', '7', '9', '4', '11', '25', '88', '10', 'A', 'S', 'G', 'M', 'O')
my_ticket = ('S', '7', 'G', '88')

count = 0
while True:
    draw = (choice(lottery_nums), choice(lottery_nums), choice(lottery_nums), choice(lottery_nums))
    count += 1
    if draw == my_ticket:
        print(f"Congrats! The loop had to run {count} to give you a winning ticket.")
        break
