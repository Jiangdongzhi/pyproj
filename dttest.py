from datetime import *

#print   'date.fromtimestamp():' , date.fromtimestamp(time.time()) 

tm = time(23 ,  46 ,  10 )  
print   'tm:' , tm  
print   'hour: %d, minute: %d, second: %d, microsecond: %d' % (tm.hour, tm.minute, tm.second, tm.microsecond)  
print   'timezone is ', tm.tzinfo
tm1 = tm.replace(hour = 20 )  
print   'tm1:' , tm1  
print   'isoformat():' , tm.isoformat() 

dt = datetime.now()  
print   '(%Y-%m-%d %H:%M:%S %f): ' , dt.strftime( '%Y-%m-%d %H:%M:%S %f' )  
print   '(%Y-%m-%d %H:%M:%S %p): ' , dt.strftime( '%y-%m-%d %I:%M:%S %p' )  
print   '%%a: %s '  % dt.strftime( '%a' )  
print   '%%A: %s '  % dt.strftime( '%A' )  
print   '%%b: %s '  % dt.strftime( '%b' )  
print   '%%B: %s '  % dt.strftime( '%B' )  
print   'date time%%c: %s '  % dt.strftime( '%c' )  
print   'date%%x:%s '  % dt.strftime( '%x' )  
print   'time%%X:%s '  % dt.strftime( '%X' )  
print   'today is %s day of the week' % dt.strftime( '%w' )  
print   'today is %s day of the year' % dt.strftime( '%j' )  
print   'this week is %s week of the year' % dt.strftime( '%U' )

input_time = datetime.strptime('2018-10-01 12:23:34', '%Y-%m-%d %H:%M:%S')

print (input_time) 

first_time = datetime.strptime('2018-06-11', '%Y-%m-%d')
second_time = datetime.strptime('2018-08-01', '%Y-%m-%d')

duration = second_time - first_time
print (duration)

duration2 = input_time - second_time

print (duration2)
