#Assignment 1
#9/9/2020
#Candice Wu
#When will the bus be at our stop?

#Prompt the user to enter hour
hour = eval(input("Please enter the hour when school starts: "))
#Prompt the user to enter minute
minute = eval(input("Please enter the minute when school starts: "))
#Prompt the user to enter stop number
stop = eval(input("Please enter your stop number: "))


#Input Program Data
WHOLETRIP = 45
LENGTHINBETWEEN = 3
LENGTHATSTOP = 2
BASECOST = 100 #cents
INCREMENTS = 4
COSTPER = 15 #cents

#Calculate school start time
school_time = hour * 60 + minute
#Calculate length of running time
running_time = LENGTHINBETWEEN + LENGTHATSTOP


#Calculate bus arrival time1
arrival1 = school_time - WHOLETRIP + (stop - 1) * running_time
#Calculate bus arrival time2
arrival2 = school_time - WHOLETRIP + (stop - 1) * running_time + LENGTHATSTOP
#Calculate length of the trip
length = (WHOLETRIP - LENGTHATSTOP) - (stop - 1) * running_time
#Calculate cost of the ticket
cost = (((length)// INCREMENTS) * COSTPER + BASECOST)/100.0


#Convert arrival time to HH:MM
arrival1_HH= arrival1 // 60
arrival1_MM= arrival1 % 60
arrival2_HH= arrival2 // 60
arrival2_MM= arrival2 % 60


#Output bus arrival time
print("The bus will be at the stop number ", stop, " between ", arrival1_HH, ":", str(arrival1_MM).zfill(2), " and ", arrival2_HH, ":", str(arrival2_MM).zfill(2), sep = "")
#Output length of the trip
print("The length of the trip from stop number", stop, "is", length, "minutes")
#Output cost of the trip
print("The cost of the ticket from stop number ", stop, " is $", cost, sep = "")

