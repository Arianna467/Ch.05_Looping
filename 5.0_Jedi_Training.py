  #Sign your name:________________

import random
'''
 1. Make the following program work.
   '''  
# print("This program takes three numbers and returns the sum.")
# total = 0
#
# for i in range(3):
#     x = int(input("Enter a number: "))
#     total+=x
# print("The total is:", total)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
# for i in range(2,101,2):
#     print(i)



'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
# i=10
# while i>=0:
#     print(i)
#     i-=1
# print("Blast Off!")



'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
# for i in range(1):
#     num = random.randrange(1,11)
#     print(num)





'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
print("This program will show you the sum of seven numbers and tell you how many positive numbers, negative numbers, and zeros you entered.")
Pos=0
Neg=0
Zero=0
Sum=0
for i in range(7):
    num=int(input("what number would you like to enter? "))
    if num>0:
        Pos+=1
        Sum+=num
    elif num<0:
        Neg+=1
        Sum+=num
    else:
        Zero+=1
        Sum+=num
print("The sum of your numbers is: ",Sum)
print("You entered ",Pos," Positive Numbers, ",Neg," Negative numbers, and ",Zero," Zeros.")