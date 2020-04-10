# Use Python to calculate how many different passwords can be formed with 6 lower case English letters. 
# For a 1 letter password, there would be 26 possibilities. 
# For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities. 
# Using this information, print the amount of possible passwords that can be formed with 6 letters.
from itertools import product

alphabet = map(chr, range(97, 123))

# Get all combinations of ["a", "b", "c",...,"z"] and length X letters 
passwordLength = 5

differentPasswords  = list(product(alphabet, repeat=passwordLength))
total = len(differentPasswords)
print(total)
# Print the obtained combinations 
for password in differentPasswords: 
    print (password)