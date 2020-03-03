#1. str()
import datetime
today=datetime.datetime.now()
s=str(today)#converting datetime object to str
print(s) #  2019-12-20 22:13:37.135388
#d=eval(s)#converting str object to datetime not possible using str()....
#print(d)

#2.repr()

today=datetime.datetime.now()
s=repr(today)#converting datetime object to str
print(s) # datetime.datetime(2019, 12, 20, 22, 13, 37, 135388)
d=eval(s)#converting str object to datetime
print(d) # 2019-12-20 22:13:37.135388