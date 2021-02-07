def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return text == reverse(text)

something = input('введите текст:')
filtertext = "".join(filter(lambda x: x not in "?!., ", something))

if (is_palindrome(filtertext)):
	print('yes its a palindrome')
else:
	print('it is not a palindrome')

