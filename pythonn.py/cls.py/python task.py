# 1
# p = True
# q = False
# print(p, q)

# 2
# a = 7
# b = 12
# print(a > b) 
# print(a < b) 

# 3
# x = -10
# print(x < 0)

# 4
# age = 16
# print(age >= 18) 

# 5
# m = 15
# n = 30
# print(m > 10 and n > 10)

# 6
# name = "Python"
# print(name == "Python")

# 7
# marks = 85
# print(marks >= 50)


# 8
# temp = 100
# print(temp == 100)

# String data type

# 1
# msg = "Hello Python"
# print(msg)

# 2
# my_name = "Namitha"
# print(my_name)
# print(type(my_name))

# 3
# text = "Programming"
# print(text[0])  

# 4
# print("Python"[-1])  

# 5
# word = "Learning"
# print(len(word))


# Task 1: Float and Int
# num_int = 10
# num_float = 5.5

# print(num_int + num_float)   
# print(num_int * num_float)   

# Task 2: String Practice
# name = "Namitha"

# print(name * 3)   
# print(name + " is learning Python")  

# Task 3: Boolean
# is_python_easy = True
# print("Python easy to learn? ", is_python_easy)







# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")



#     num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")



#     a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     print("Largest:", a)
# else:
#     print("Largest:", b)



# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a >= b and a >= c:
#     print("Largest:", a)
# elif b >= a and b >= c:
#     print("Largest:", b)
# else:
#     print("Largest:", c)



#     age = int(input("Enter age: "))
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")



#     marks = int(input("Enter marks: "))
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# elif marks >= 50:
#     print("Grade: C")
# else:
#     print("Fail")



#     ch = input("Enter a character: ").lower()
# if ch in "aeiou":
#     print("Vowel")
# elif ch.isalpha():
#     print("Consonant")
# else:
#     print("Not a letter")



# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("Multiple of 3 and 5")
# else:
#     print("Not a multiple of 3 and 5")



#     ch = input("Enter a character: ")
# if ch.isupper():
#     print("Uppercase")
# elif ch.islower():
#     print("Lowercase")
# elif ch.isdigit():
#     print("Digit")
# else:
#     print("Special symbol")



# num = int(input("Enter a number: "))
# if num % 7 == 0:
#     print("Divisible by 7")
# else:
#     print("Not divisible by 7")



#     age = int(input("Enter age: "))
# if age >= 60:
#     print("Senior Citizen")
# else:
#     print("Not a Senior Citizen")



#     ch = input("Enter a character: ").lower()
# if ch in "aeiou":
#     print("Vowel")
# elif ch.isalpha():
#     print("Consonant")
# else:
#     print("Not a letter")







# amount = float(input("Enter purchase amount: "))
# if amount > 5000:
#     discount = amount * 0.20
# elif 2000 <= amount <= 5000:
#     discount = amount * 0.10
# else:
#     discount = 0
# final_price = amount - discount
# print(f"Discount: ₹{discount}")
# print(f"Final Price to Pay: ₹{final_price}")



# correct_pin = "1234"  # predefined PIN
# user_pin = input("Enter your 4-digit ATM PIN: ")
# if user_pin == correct_pin:
#     print("Access Granted")
# else:
#     print("Access Denied")



# days = int(input("Enter number of days: "))
# years = days // 365
# remaining_days = days % 365
# months = remaining_days // 30
# days_left = remaining_days % 30
# print(f"{years} Years, {months} Months, {days_left} Days")



# amount = int(input("Enter amount in rupees: "))
# notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
# print("Minimum number of currency notes:")
# for note in notes:
#     count = amount // note
#     if count > 0:
#         print(f"₹{note} : {count}")
#     amount = amount % note




   
# for i in range(1, 11):
#     print(i, end=" ")
# print("\n")



# for i in range(2, 21, 2):
#     print(i, end=" ")
# print("\n")



# for i in range(1, 21, 2):
#     print(i, end=" ")
# print("\n")



# for i in range(10, 0, -1):
#     print(i, end=" ")
# print("\n")



# for i in range(1, 11):
#     print(f"{i}^2 = {i*i}")
# print()



# num = 5
# for i in range(1, 11):
#     print(f"{num} x {i} = {num*i}")
# print()



# total_sum = sum(range(1, 101))
# print("Sum of numbers from 1 to 100:", total_sum)
# print()



# product = 1
# for i in range(1, 11):
#     product *= i
# print("Product (factorial of 10):", product)
# print()



# for i in range(5, 51, 5):
#     print(i, end=" ")
# print("\n")



# for i in range(1, 31):
#     if i % 2 == 0 and i % 3 == 0:
#         print(i, end=" ")
# print()






# def odd_numbers(n):
#     for i in range(1, 2*n, 2):
#         print(i, end=" ")
#     print()



# def even_numbers(n):
#     for i in range(2, 2*n+1, 2):
#         print(i, end=" ")
#     print()



# def countdown(n):
#     for i in range(n, 0, -1):
#         print(i, end=" ")
#     print()



# def step2(n):
#     for i in range(1, n+1, 2):
#         print(i, end=" ")
#     print()



# def step3(n):
#     for i in range(1, n+1, 3):
#         print(i, end=" ")
#     print()



# def sum_of_squares(n):
#     print(sum(i**2 for i in range(1, n+1)))



# def sum_of_cubes(n):
#     print(sum(i**3 for i in range(1, n+1)))



# def product_natural(n):
#     product = 1
#     for i in range(1, n+1):
#         product *= i
#     print(product)



# def end_with_5(n):
#     for i in range(1, n+1):
#         if i % 10 == 5:
#             print(i, end=" ")
#     print()



# def count_div4(n):
#     count = 0
#     for i in range(1, n+1):
#         if i % 4 == 0:
#             count += 1
#     print(count)



# def count_not_div2(n):
#     count = 0
#     for i in range(1, n+1):
#         if i % 2 != 0:
#             count += 1
#     print(count)



# def square_of_evens(n):
#     for i in range(2, n+1, 2):
#         print(i**2, end=" ")
#     print()



# def cube_of_odds(n):
#     for i in range(1, n+1, 2):
#         print(i**3, end=" ")
#     print()



# def div_by_2_and_3(n):
#     for i in range(1, n+1):
#         if i % 2 == 0 and i % 3 == 0:
#             print(i, end=" ")
#     print()



# def div_by_2_or_5(n):
#     for i in range(1, n+1):
#         if i % 2 == 0 or i % 5 == 0:
#             print(i, end=" ")
#     print()



# def sum_div7(n):
#     print(sum(i for i in range(1, n+1) if i % 7 == 0))



# def sum_not_div3(n):
#     print(sum(i for i in range(1, n+1) if i % 3 != 0))






# def is_armstrong(num):
#     digits = str(num)
#     power = len(digits)
#     total = sum(int(d)**power for d in digits)
#     return num == total



# def print_factors(n):
#     factors = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             factors.append(i)
#     return factors



# def factorial(n):
#     if n < 0:
#         return "Factorial not defined for negative numbers"
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact



# def count_digits(n):
#     return len(str(abs(n)))





# def sum_of_prime_digits(n):
#     primes = {2, 3, 5, 7}  # prime digits only
#     total = 0
#     for digit in str(n):
#         if int(digit) in primes:
#             total += int(digit)
#     return total



# def sum_of_even_digits(n):
#     total = 0
#     for digit in str(n):
#         if int(digit) % 2 == 0:
#             total += int(digit)
#     return total



# def check_even_sum_parity(n):
#     total = 0
#     for digit in str(n):
#         if int(digit) % 2 == 0:
#             total += int(digit)
#     if total % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"





# def char_frequency(s):
#     freq = {}
#     for ch in s:
#         freq[ch] = freq.get(ch, 0) + 1
#     return freq



# def remove_duplicates(s):
#     result = ""
#     seen = set()
#     for ch in s:
#         if ch not in seen:
#             result += ch
#             seen.add(ch)
#     return result



# def longest_word(sentence):
#     words = sentence.split()
#     return max(words, key=len)



# def word_count(s):
#     words = s.split()
#     freq = {}
#     for w in words:
#         freq[w] = freq.get(w, 0) + 1
#     return freq



# def replace_spaces(s):
#     return s.replace(" ", "-")





# numbers = [1, 2, 3, 4, 5]
# total = 0
# for num in numbers:
#     total += num
# print("Sum of elements:", total)



# elements = [1, 2, 2, 3, 4, 4, 4, 5]
# frequency = {}
# for item in elements:
#     frequency[item] = frequency.get(item, 0) + 1
# print("Frequency of elements:", frequency)



# items = [1, 2, 2, 3, 4, 4, 5]
# unique = []
# for item in items:
#     if item not in unique:
#         unique.append(item)
# print("List without duplicates:", unique)



# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# merged = list1.copy()
# for item in list2:
#     merged.append(item)
# print("Merged list:", merged)





# def rearrange_even_odd(lst):
#     even_indexed = lst[::2]   # elements at even indices
#     odd_indexed = lst[1::2]   # elements at odd indices
#     return even_indexed + odd_indexed

# # Example
# print(rearrange_even_odd([10, 20, 30, 40, 50]))  # [10, 30, 50, 20, 40]



# def flatten_list(nested_list):
#     return [item for sublist in nested_list for item in sublist]

# # Example
# print(flatten_list([[1, 2], [3, 4], [5]]))  # [1, 2, 3, 4, 5]



# def second_largest_smallest(lst):
#     unique_sorted = sorted(set(lst))
#     if len(unique_sorted) < 2:
#         return None, None  # Not enough elements
#     return unique_sorted[1], unique_sorted[-2]

# # Example
# print(second_largest_smallest([5, 1, 9, 2, 9, 5, 7]))
# # Output: (2, 7) → second smallest = 2, second largest = 7




# my_list = [10, 20, 30, 40, 50]
# print(my_list)


# my_list = [10, 20, 30, 40, 50]
# print(my_list[2])


# my_list = [10, 20, 30, 40, 50]
# my_list[2] = 35
# print(my_list)


# my_list = [10, 20, 30, 40, 50]
# my_list.append(60)
# print(my_list)


# my_list=[10,20,30,40,50]
# my_list.insert(1,15)
# print(my_list)


# my_list=[10,20,30,40,50]
# my_list.remove(40)
# print(my_list)


# my_list = [10, 20, 30, 40, 50]
# del my_list[2]
# print(my_list)


# my_list = [10, 20, 30, 40, 50]
# print(len(my_list))


# my_list = [10, 20, 30, 40, 50]
# print(50 in my_list)


my_list = [10, 20, 30, 40, 50]
for item in my_list:
    print(item)


# my_list = [50, 10, 40, 20, 30]
# my_list.sort()
# print("11:", my_list)


# my_list = [50, 10, 40, 20, 30]
# my_list.sort(reverse=True)
# print("12:", my_list)


# my_list = [10, 20, 30, 40, 50]
# my_list.reverse()
# print("13:", my_list)


# my_list = [10, 20, 30, 40, 50]
# print("14:", my_list[::-1])


# my_list = [10, 20, 30, 40, 50]
# copy1 = my_list[:]
# print("15:", copy1)


# my_list=[10,20,30,40,50]
# copy2 = my_list[:]
# print("16:", copy2)


# my_list = [10, 20, 30, 40, 50]
# my_list.clear()
# print("17:", my_list)


# my_list = [10, 20, 30, 20, 40, 20]
# print("18:", my_list.count(20))


# my_list = [10, 20, 30, 40, 50]
# print("19:", my_list.index(50))


# list1 = [10, 20, 30]
# list2 = [40, 50, 60]
# combined = list1 + list2
# print("20:", combined)


# my_list = [10, 20, 30]
# print("21:", my_list * 3)


# my_list = [10, 20, 30, 40, 50, 60]
# print("22:", my_list[::2])


# my_list = [10, 20, 30, 40, 50, 60, 70]
# print("23:", my_list[2:6])


# my_list = [10, 20, 30, 40, 50]
# print("24:", all(x > 0 for x in my_list))


# my_list = [10, 20, 30, 40, 50]
# print("25:", ",".join(map(str, my_list)))


# my_list = [10, 20, 30, 40, 50]
# print("26:", max(my_list))


# my_list = [10, 20, 30, 40, 50]
# print("27:", min(my_list))


# my_list = [10, 20, 30, 40, 50]
# print("28:", sum(my_list))


# my_list = [10, 20, 30, 40, 50]
# squared = [x**2 for x in my_list]
# print("29:", squared)


# my_list = [10, 21, 32, 43, 54]
# evens = [x for x in my_list if x % 2 == 0]
# print("30:", evens)


# my_list = [10, 21, 32, 43, 54]
# odds = [x for x in my_list if x % 2 != 0]
# print("31:", odds)


# test_list = [10, 20, 30, 20, 40, 30, 50, 10]
# duplicates = [x for x in set(test_list) if test_list.count(x) > 1]
# print("32:", duplicates)


# test_list = [10, 20, 30, 20, 40, 30, 50, 10]
# no_duplicates = []
# for x in test_list:
#     if x not in no_duplicates:
#         no_duplicates.append(x)
# print("33:", no_duplicates)


# test_list = [10, 20, 30, 20, 40, 30, 50, 10]
# unique = list(set(test_list))
# print("34:", unique)


# empty_list = []
# print("35:", len(empty_list) == 0)


# n = 5
# zeros = [0] * n
# print("36:", zeros)


# swap_list = [1, 2, 3, 4]
# swap_list[1], swap_list[3] = swap_list[3], swap_list[1]
# print("37:", swap_list)


# my_list = [10, 20, 30, 40, 50]
# print("38:", my_list[-1])


# string = "Hello"
# char_list = list(string)
# print("39:", char_list)
