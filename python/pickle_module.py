import pickle

#pickling python object
# cars = ["Audi","Bmw","maruti suzuki","Harryti Tuzuki"]
# file = "mycar.pkl"
# fileobj = open(file,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()

#decode the pickle file
file = "mycar.pkl"
fileobj = open(file,'rb')
mycar = pickle.load(fileobj)
print(mycar)

