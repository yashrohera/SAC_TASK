#Code to check wheather a given string is palindrome or not
def check_palindrome(string):
	string=string.lower()    #Convert the string to lower_case to make the code case insensitive 
	l=list(string)           #Converting string to list 
	length=len(l)     
	mid=(length+1)//2        #finding the mid of the list
	l=l[length-1:mid-1:-1]+l[mid-1:0:-1]+l[0:1]  #Reversing the list
	new_string=('').join(l)  #converting the list to string
	if new_string==string:
		return 1
	return 0
n=input()
if check_palindrome(n):
	print('The given string is a palindrome')
else:
	print('The given string is not a palindrome')
