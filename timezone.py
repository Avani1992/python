"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

s: a string representing time in  12 hour format
"""
s="11:30:30 PM"
s6="11:30:59 AM"

def timezone(x):
  s1=x.split(' ')
  #s2=s1[0]
  s3=s1[0].split(':')
  #print(s3)
  con_h=int(s3[0])
  con_m=int(s3[1])
  con_s=int(s3[2])
  if(s1[1]=="AM"):
    print(s1[0])
  else:
    s4=str(con_h+12) +':'+str(con_m) +':'+ str(con_s)
    print(s4)
    
timezone(s6)