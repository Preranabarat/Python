def count_vowels_consonants_blanks(string):
    vowels = 0
    consonants = 0
    blanks = 0

    # Converting string to lowercase to simplify comparison
    string = string.lower()

    for char in string:
        if char in 'aeiouAEIOU':
            vowels += 1
        elif char.isalpha():
            consonants += 1
        elif char == ' ':
            blanks += 1

    return vowels, consonants, blanks

# Test the function
input_string = input("Enter a string: ")
vowels, consonants, blanks = count_vowels_consonants_blanks(input_string)

print("Total number of vowels:", vowels)
print("Total number of consonants:", consonants)
print("Total number of blanks:", blanks) 