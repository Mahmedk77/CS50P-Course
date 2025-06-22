# string='twitter'
string=input("Enter thy string: ")
for letter in string:
    if letter not in 'aeiouAEIOU' :
        print(letter,end="")


