import random

ordinal_numbers = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth']
lotto_num = []
chosen_num = []
num_get_list = []
num_get_count = 0
i = 0

# lotto number draw
while len(lotto_num) != 6:
    generate_num = random.randint(1, 30)

    if not generate_num in lotto_num: # just add unique number
        lotto_num.append(generate_num)

print("Pick 6 numbers from 1 to 30")

# prompt user
while len(chosen_num) != 6:
    user_input = input(f"{ordinal_numbers[i]} number: ")

    # validation
    if user_input.isdigit() and int(user_input) != 0:
        num = int(user_input)
        
        if not num > 30:
            if num not in chosen_num:
                chosen_num.append(num)
                print(f"Your number: {chosen_num}")
                i += 1
            else:
                print(f'You already have {num}.')
        else:
            print("Out of range! Just pick from 1 to 30.")
    else:
        print("Invalid input!")

# checking
for num in chosen_num:
    if num in lotto_num:
        num_get_list.append(num)
        num_get_count += 1

print("========================================")
print(f"Lotto result: {lotto_num}")
print(f"Your number: {chosen_num}")

# result
if num_get_count == 6:
    print("Congratulations! You've got the JACKPOT!")
elif num_get_count >= 3 and num_get_count < 6:
    print("You Win!")
else: 
    print("You Lose!")

print(f"You've got {num_get_count} number(s): {num_get_list}")

# Brian Galvez
