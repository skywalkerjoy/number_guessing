import random

top_of_range = input('What is your top range number? ')
if top_of_range.isdigit():  # check if input is a number
    top_of_range = int(top_of_range)  # convert input into int

    if top_of_range <= 0:
        top_of_range = input('Type a larger number than 0 ')
else:
    top_of_range = input('Please input a number')

random_num = random.randrange(top_of_range)  # generate a random number
print('Now a new random number is generated')
print(random_num)

times_try = 1

while True:
    r_user = input('Input your guessing number: ')
    if r_user.isdigit():
        r_user = int(r_user)
        break
    else:
        r_user = int(input('Please type a number: '))


while (r_user != random_num):
    times_try = times_try + 1
    if r_user > random_num:
        r_user = int(input('Please input a lower number '))
    else:
        r_user = int(input('Please input a bigger number '))

print('You are correct! and Only have try ' + str(times_try) + ' times')
