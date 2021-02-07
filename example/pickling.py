import pickle

shoplistfile = 'shoplist.data'
shoplist = ['яблоки','mango','carrot']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
print(f)
f.close()


del shoplist
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist) 