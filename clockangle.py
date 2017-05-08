 
 #This program helps to find the angle between the hour hand and the minute hand of the clock

def clock_angle(input_time):
	hour=int(input_time[0])
	minute=int(input_time[1])
	if(hour>12):
		hour=hour%12
	minute_angle=minute*6
	if hour==12:
		hour_angle=0
	else:
		hour_angle=(hour*30)+(minute*0.5)
	diff_angle=abs(hour_angle-minute_angle)
	return(diff_angle)

print('Enter the time in the format hh:mm')
time=raw_input()
print("The time is " + time)
time_split=time.split(":")
diff=clock_angle(time_split)
print("The difference in angle between the hour and minute hand is " + str(diff) + " degree")




