# Name-Asif Rana  # Student ID-27158632
import math
#Entering input'
n=int(input('Enter a positive integer: '))
while n<=0:
    n=int(input('Enter a positive integer: '))

#'Assigning the variables required for the approxiamtion'
no_term=n+1

#'Variables which will chage after each iteration '
n_increment=n-1
divisionConst=n+(n/no_term)
m=float(n_increment+(n_increment/divisionConst))

#Nested loop for finding approximation 
while(n_increment>0):
    if (n_increment/divisionConst)>0.1:
        m=float(n_increment+(n_increment/divisionConst))
        divisionConst=m
        print('Value of each iteration',divisionConst)
        n_increment=n_increment-1
    
    else:
        break
    

e=float(2+(1/divisionConst))
print('The approximation is',e)

    
         
      
   
    
    
    
