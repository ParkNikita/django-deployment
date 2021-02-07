import django
django.setup()

from faker import Faker
makefake = Faker()

def populate(n=5):
	fake_name_list = []
	fake_email_list = []
	for entry in range(n):
		fake_name = makefake.name()
		fake_email = makefake.email()

		fake_name_list.append(fake_name)
		fake_email_list.append(fake_email)
	print(fake_name_list)
	print(fake_email_list)
populate(10)


		