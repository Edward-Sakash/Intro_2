
# Exercise (Vowel Sort):
"""Write a Python program that sorts a list of strings based on the number of vowels they contain.
The program should take a list of strings as input from the user.
sort the strings by the number of vowels they contain using the sort() method with a custom function
print the sorted list of strings."""

# Solution 1
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

words = input("Enter a list of words separated by spaces: ").split()

# Filter out words with no vowels
words = [word for word in words if count_vowels(word) > 0]

# Sort the remaining words based on the number of vowels using a custom function
words.sort(key=count_vowels)

# Print the sorted list of words
print("Sorted list of words based on the number of vowels:")
print(words)

print("_____________________________________________")

# Solution 2

# Define a function to count the number of vowels in a word
def count_vowels(word):
    # Convert the word to lowercase to simplify checking for vowels
    # Iterate over each character in the word, counting the number of vowels
    return sum(1 for char in word.lower() if char in 'aeiou')

# Get a list of words from the user, split by whitespace
words = input("Enter a list of words: ").split()

# Sort the list of words by the number of vowels they contain,
# using the count_vowels function as the key for the sort
my_strings = sorted(words, key=count_vowels)

# Filter out any words with zero vowels using a list comprehension
my_strings = [word for word in my_strings if count_vowels(word) > 0]

# Print the sorted list of words with vowels, excluding any words without vowels
print(my_strings)

print("_____________________________________________")

