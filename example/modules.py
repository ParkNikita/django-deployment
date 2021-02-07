import re

text_one = 'Hello, would you like some catfish?'
text_two = 'Hello, would you like to take a catnap?'
text_three = 'Hello, have you seen this caterpillar?'

pattern = r'cat(fish|nap|erpillar)'
resultone = re.findall(pattern,text_one)
print(resultone)
resulttwo = re.findall(pattern,text_two)
print(resulttwo)
resultthree = re.findall(pattern,text_three)
print(resultthree)


# text = 'Only find hypen-words in this sentence. But you dont know how log-ish they are'
# pattern = r'[\w]+-[\w]+'
# result = re.findall(pattern, text)
# print(result)






# import re
# text = 'This is a sting! But it has punctuations. How can we remove it?'
# clean = r'[^!?. ]+'
# result = re.findall(clean,text)
# print(result)
# new = ' '.join(result)
# print(new)



# phrase = 'there are 3 numbers 23 inside 123 this sentence'
# pattern = r'[^\d]+'
# result = re.findall(pattern,phrase)
# print(result)



# pattern = r'...at'
# text = 'The cat in the hat went splat'
# result = re.findall(pattern,text)
# print(result)











# import re

# text = 'My phone number is 91-691-41-45'
# phone = re.search(r'\d\d-\d\d\d-\d\d-\d\d',text)
# print(phone.group())
# phone_pattern = re.compile(r'(\d{2})-(\d{3})-(\d{2})-(\d{2})')
# result = re.search(phone_pattern,text)
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
# print(result.group(4))







# import re
# text = 'my name is nikita and my phone number is 91 691 4145'

# for match in re.finditer('is',text):
# 	print(match)
# 	print(match.span())
# 	print(match.group())







# match = re.findall('is',text)
# print(match)
# print(len(match))



# pattern = 'nikita'
# match = re.search(pattern,text)
# print(match)
# print(match.span())
# print(match.start())
# print(match.end())






#DEBUGGER
# import pdb
# x = [1,2,3]
# y = 2
# z = 1
 
# result_one = y + z

# pdb.set_trace()
# result_two = y + z 





# import random


# print(random.gauss(mu=0,sigma=1))
# print(random.uniform(a=0,b=10))



# my_list = list(range(0,20))

# print(random.choices(population = my_list, k = 12))
# print(random.sample(population = my_list, k = 12)) #not repeat


# new_list = random.choice(my_list)
# print(new_list)


# print(random.randint(0,100))
# random.seed(21)
# print(random.randint(0,100))
# print(random.randint(0,100))
# print(random.randint(0,100))










# import math
# print(math.log(8,2))
# print(math.factorial(4))
# print(math.degrees(math.pi/2))
# print(math.radians(180))







# import datetime
# from datetime import datetime

# datetime1 = datetime(2021,11,3,10,3,10)
# datetime2 = datetime(2021,11,3,11,3,10)
# mydiff = datetime1 - datetime2
# r = mydiff.total_seconds()
# print(r)

# date1 = date(2021,11,3)
# date2 = date(2022,11,4)
# result = date1 - date2
# print(type(result))
# print(result)

# today = datetime.date.today()
# print(today.year)
# print(today.month)
# print(today.day)
# print(today.ctime())

# mytime = datetime.time(2,39,10,100)
# print(mytime.hour)
# print(mytime.minute)
# print(mytime.second)
# print(mytime.microsecond)





# import os
# path = os.getcwd()
# for folder, subfolders, files in os.walk(path):
# 	print("currently looking at {0}".format(folder))
# 	print('\n')
# 	print('The subfolders are: ')
# 	for sub in subfolders:
# 		print('\tsubfolder {0}'.format(sub))
# 	print('\n')
# 	print('The files are: ')
# 	for file in files:
# 		print('\tfiles {0}'.format(file))





# import send2trash
# send2trash.send2trash('if.py')  #SEND TO TRASH


# import os
# print(os.getcwd())  #CURRENT DIRECTORY
# print(os.listdir())  #ALL ITEMS IN CURRENT FOLDER
# os.rmdir() #delete files
# os.unlink() #delete folder, folder must be empty

# import shutil

# shutil.move('D:/projects/bot','D:/python')









# from collections import namedtuple

# cat = namedtuple('Dog',['age','breed','name'])

# Pirate = cat(age=10,breed='Lab',name='Pirate')
# print(type(Pirate))

# print(Pirate.age)



# from collections import defaultdict


# d = defaultdict(lambda: 0)
# d['correct'] = 100
# print(d)
# d['wrong key']
# print(d)




# from collections import Counter
# my_list = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
# new_list = Counter(my_list)
# print(new_list)

# sentence = 'How many times does each word show up in this sentence with a word'

# new_sentence = Counter(sentence.split())
# print(list(new_sentence))


