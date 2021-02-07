import random

def ge_random_digits():
	digit = random.randint(0,100)
	return digit
def guess_number(num):
	print(num)
	while True:
		guess = int(input("What is your guess? "))
		if guess == num:
			print("Match")
			break
		elif guess<num:
			print('more')
		else:
			print('less')

guess_number(get_random_digits())

