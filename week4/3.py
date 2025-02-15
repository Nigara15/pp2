import datetime 
#1
def days5():
    cd= datetime.date.today()
    nd=cd-datetime.timedelts(days=5)
    return nd

#2
def ytt():
   t= datetime.date.today()
   y= t - datetime.timedelts(days=1)
   tom= t + datetime.timedelts(days=1)
   return t,y,tom

#3
def micro(dt):
    return dt.replace(microsecond=0)

#4
def date(d1,d2):
    delta=d2-d1
    return delta.total_seconds()

print (days5)
print(ytt)
yesterday, today, tomorrow = ytt()
print(f"Yesterday: {yesterday}, Today: {today}, Tomorrow: {tomorrow}")

now = datetime.datetime.now()
print( micro(now))

date1 = datetime.datetime(2023, 1, 1, 12, 0, 0)
date2 = datetime.datetime(2023, 1, 2, 12, 0, 0)
print( date(date1, date2))