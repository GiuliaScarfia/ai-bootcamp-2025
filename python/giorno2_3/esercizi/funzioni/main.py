#1,
def mydivmod(x,y):
    try:
        quotient= x//y
        remainder= x % y
        return (quotient, remainder)
    except ZeroDivisionError:
        print("Dividere per zero è un calcolo privo di significato, il cui risultato non esiste.")
        return (None)
#Oppure
def mydivmod(x,y):
    if y==0:
        print("Dividere per zero è un calcolo privo di significato, il cui risultato non esiste.")
        return (None)
    return (x//y,x%y)
#Provo
print(mydivmod(10,7))
print(mydivmod(10,0))

#2.
#Funzione 1: Elevare al quadrato ogni elemento della lista
def pow_list(list):
    return [x**2 for x in list]

assert pow_list([1, 2, 3]) == [1, 4, 9], (
    "Implement a function that takes a list "
    "and returns another list with each value raised "
    "to the power of 2"
)

print(pow_list([1,2,3]))

#Funzione 2: Contare il numero di parole in una stringa
str="hello world"
def count_words(str):
    return len(str.split(' '))

assert count_words("hello world"), (
    "Implement a trivial function that counts the "
    "number of words in the given string. "
    "Hint: try executing the following command in the "
    "Python console: 'hello world'.split(' ')"
)

print(count_words(str))

#Funzione 3: Invertire una stringa
str="Ciao"
def reverse_string(str):
    return str[::-1]

assert reverse_string("hello") == "olleh", (
    "Implement a function that takes a string "
    "and returns it reversed. For example, 'hello' becomes 'olleh'."
)

print(reverse_string(str))

#Funzione 4: Calcolare il fattoriale di un numero
def factorial(n):
    if n==0 or n==1:
        return 1
    result =1
    result= n*factorial(n-1)
    return result

assert factorial(5) == 120, (
    "Implement a function that computes the factorial of a given number. "
    "Factorial of n (n!) is the product of all positive integers from 1 to n. "
    "For example, factorial(5) = 5 * 4 * 3 * 2 * 1."
)

print(factorial(5))
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))

#Funzione 5: Verificare se la stringa è un palindromo
def is_palindrome(str):
    return str == str[::-1]

assert is_palindrome("racecar") == True, (
    "Implement a function that checks if a given string is a palindrome. "
    "A palindrome reads the same forwards and backwards, e.g., 'racecar'. "
    "Hint: try executing the following command in the "
    "Python console: 'racecar'[::-1]"
)

str="anna"
print(is_palindrome(str))
str="ciao"
print(is_palindrome(str))

#Funzione 6: Sommare i numeri pari di una lista
def sum_even_numbers(list):
    return sum(x for x in list if x%2==0)

assert sum_even_numbers([1, 2, 3, 4, 5]) == 6, (
    "Implement a function that takes a list of numbers "
    "and returns the sum of all even numbers in the list."
)

print(sum_even_numbers([1,2,3,4]))

#Funzion 7: Trovare il numero massimo in una lista
def find_max(list):
    return max(list)

assert find_max([3, 1, 4, 1, 5]) == 5, (
    "Implement a function that takes a list of numbers "
    "and returns the largest number in the list."
)

print(find_max([1,3,5,67]))

#Funzione 8: Contare le vocali in una stringa
def count_vowels(str):
    vowels = "aeiouAEIOU"
    return sum(1 for char in str if char in vowels)

assert count_vowels("hello world") == 3, (
    "Implement a function that takes a string "
    "and returns the count of vowels ('a', 'e', 'i', 'o', 'u') in it. "
    "For example, 'hello world' contains 3 vowels."
)

print(count_vowels("hello world"))
print(count_vowels("Python"))
print(count_vowels("AEIOU"))
print(count_vowels("xyz"))

#3.
# Bug: veniva chiamato factorial(n) invece di factorial(n - 1)
def factorial(n):
    """Calculate the factorial of the given number"""
    # FIXME: this code has a bug!
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1


assert factorial(5) == 120

print(factorial(5))
print(factorial(3))
print(factorial(1))
print(factorial(0))