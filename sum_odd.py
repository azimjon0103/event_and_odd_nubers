#A four-digit integer is given. Find the sum of odd digits in it.
var_int=3215
#Create a variable "var_int" and assign it a four-digit integer value.
b=(var_int%10)%2*(var_int%10)
c=(var_int%100//10)%2*(var_int%100//10)
d=(var_int%1000//100)%2*(var_int%1000//100)
f=(var_int//1000)%2*(var_int//1000)
#Create a variable "sum_even" and assign it 0.
sum_even=b+c+d+f
#Find the sum of the odd digits in the variable "var_int".
print(sum_even)