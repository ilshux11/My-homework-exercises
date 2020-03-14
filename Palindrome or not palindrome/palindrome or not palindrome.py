my_string = "Rise to vote, sir."
# or: my_string = input("Enter string: ")

# define punction
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# remove punction from the string
no_punctuation = ""
for char in my_str:
	if char not in punctuations:
		no_punctuation += char

no_punctuation = string # change variable

# remove whitespaces
new_string = " "
for char in string:
	if char == " ":
		new_string += char

new_string.lower
reverse_string = new_string[::-1]

if new_string == reverse_string:
	print("\nYes, it's a palindrome")
else:
	print("\nNo, it isn't a palindrome")