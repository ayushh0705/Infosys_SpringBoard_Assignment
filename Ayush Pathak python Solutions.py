# 1. Write a python program to swap below string  . Input = Ravi Kumar Patel,  output = Kumar Ravi patel 

def swap(Input):
    string = Input.split()
    if len(string) == 3:
        swapped_strings = f"{string[1]} {string[0]} {string[2]}"
    else:
        swapped_strings = "The Given String is Invalid Please check again!"
    return swapped_strings

Input = "Ravi Kumar Patel"
output = swap(Input)
print(output)
print('-------------------------------------------------------------------')


# 2. Write a python program to find maximum number from the list without using sorting  list = [87,43 ,76,1,99,23,8]

def max_num(Input):
    list1 = max(Input)
    return list1
Input = [87,43 ,76,1,99,23,8]
output = max_num(Input)
print(output)
print('-------------------------------------------------------------------')

# 3. Write python to find the occurance of character in string s1= google output = g=2,o=2...

def word_count(Input):
    result = {}
    for char in Input:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
Input = "google"
output = word_count(Input)
print(output)
print('-------------------------------------------------------------------')

# 4. Use list comprehension to solve below problem . Find all number from 1-1000 are divided by 7 
def div():
    list_comprehension = [i for i in range(1,1000) if i % 7 == 0]
    return list_comprehension

output = div()
print(output)
print('-------------------------------------------------------------------')

# 5. Produce a list containing word even if number is even and odd if number is odd . Input = [75,8,94,2,23,29,100], output = [odd, even ,even ,...]

def oddEve(Values):
    result = []
    for i in Values:
        if i % 2 == 0:
            result.append("Even")
        else:
            result.append("ODD")
    return result
Input = [75,8,94,2,23,29,100]
Output = oddEve(Input)
print(Output)
print('-------------------------------------------------------------------')

# 6. Write a program to extract numbers from the string .input = 'hello 1 hi 9 . How are 10' output =[1,9,10]
def extract_num(string):
    number = []
    words = string.split()
    for i in words:
        if i.isdigit():
            number.append(int(i))
    return number
Input = 'hello 1 hi 9 . How are 10'
output = extract_num(Input)
print(output)
print('-------------------------------------------------------------------')

# 7. Write a program to find give string of email is in correct format or not. Input=xyz@gmail.com output = correct 

def mail_check(string):
    if '@' in string and '.' in string.split('@')[-1]:
        return 'Correct'
    else:
        print('Incorrect')
Input = 'xyz@gmail.com'
Output = mail_check(Input)
print(Output)
print('-------------------------------------------------------------------')

# 8. Write program to remove all white space in from the string 

def remove_space(Input):
    string = ''
    for i in Input:
        if i != ' ':
            string += i
    return string
Input = " Hey! It's me! How are you!"
Output = remove_space(Input)
print(Output)
print('-------------------------------------------------------------------')

# 9. Write a program to find sum of 1 to 50 numbers using list comprehension 

sum_of_numbers = sum([num for num in range(1, 51)])

print("The sum of numbers from 1 to 50 is:", sum_of_numbers)
print('-------------------------------------------------------------------')

# 10. Write a program to check string is alpha numeric or not

def is_alphanumeric(string):
    if string.isalnum():
        return "The string is alphanumeric."
    else:
        return "The string is not alphanumeric."

# Example usage
input_string = "Hello123"
output = is_alphanumeric(input_string)
print(output)

# Q1
import numpy as np

array = np.zeros((4,4), dtype=int)
array[1:3, 1:3] = 1
print(array)

# matrix question using numpy border of matrix is 1 and middle part is 0

n = 5
matrix = np.ones((n,n), dtype=int)
matrix[1:-1,1:-1] = 0
print(matrix)

