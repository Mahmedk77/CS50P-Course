def is_valid(str):
    
    flag=True
    if ( (2<=len(str)<=6) and (str[0:2].isalpha())):
        if str.isalpha():
            flag=True       
        else:
           sum1=0
           sum2=0
           for letter in range(2,len(str)):
             if (str[letter].isnumeric()):
                #  if (str[letter+1].isalpha()):
                flag=False
                
             elif str[2:5].isalpha():
                flag=True
                break      
        if str[4:].isnumeric:
            flag=True      
        else:
            False
        if str[2:].isnumeric():
            flag=True
        if str[2:5].isalpha():
            flag=True
        index=str.find('0')
        if index!=-1 and str[index-1].isalpha():
            flag=False
    else:
           flag=False
    return (flag)               
def main(): 
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
main()




