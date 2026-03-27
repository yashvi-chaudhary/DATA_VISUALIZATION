# Number of rows for the pattern
n = 5

# Loop through each row
for i in range(1, n + 1):
    
    # Print spaces first (for right alignment)
    # (n - i) gives decreasing spaces
    spaces = " " * (n - i)
    
    # Print stars
    # i gives increasing number of stars
    stars = "*" * i
    
    # Combine spaces and stars, then print
    print(spaces + stars)