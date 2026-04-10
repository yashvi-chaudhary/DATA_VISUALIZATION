# Program to count vowels in a file

# Open file in read mode
with open("sentences.txt", "r") as file:
    data = file.read()   # read entire file content

# Initialize vowel count
vowel_count = 0

# Define vowels
vowels = "aeiouAEIOU"

# Count vowels
for ch in data:
    if ch in vowels:
        vowel_count += 1

print("Number of vowels in the file:", vowel_count)