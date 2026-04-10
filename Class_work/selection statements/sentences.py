# Program to take 20 sentences from user and write into a file (each on new line)

# Open file in write mode
file = open("sentences.txt", "w")

# Loop to take 20 inputs
for i in range(1, 21):
    sentence = input(f"Enter sentence {i}: ")
    
    # Write each sentence in new line
    file.write(sentence + "\n")

# Close the file
file.close()

print("All sentences are saved in file successfully!")