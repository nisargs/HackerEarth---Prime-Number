'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
num = int(input())              #this will take input
for n in range(2,num+1):        
    if n>1:
        for i in range(2,n):
            if (n%i) == 0:      #this will give number is not prime
                break
    
        else:
            print(n, end=" ")     #end is used to display the output in single line
