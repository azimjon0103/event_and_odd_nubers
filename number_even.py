#A four-digit integer is given. Find the number of even digits in it.
a=3000
#Create a variable "var_int" and assign it a four-digit integer value.
b=a//1000%2
d=a-b*1000
c=d//100%2
e=d-c*100
f=e//10%2
g=e-f*10
h=g%2
#Print the number of even digits in the variable "var_int".
var_int=4-(b+c+f+h) 
print(var_int)