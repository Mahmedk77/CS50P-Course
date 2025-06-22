#main function for the code
def main():
    Time=input("whats the time?: ")
#passing the input string
    convert(Time)
#function to convert that #:## or ##:## str into float value
def convert(Time):
#using the split func to make two parts first and last
    first,last=Time.split(":")
    first=float(first) # first is the hrs
    last=float(last) # last is the mins
    last=last/60 # convert mins into hrs
    time=first+last # adding both hrs+hrs

    if time<=8.0 and time>=7.0: #using conditionals
        print("Breakfast")
    elif time<=13 and time>=12:
        print("Lunch")
    elif time<=19 and time>=18:
        print("Dinner")
 
main() #calling the main function