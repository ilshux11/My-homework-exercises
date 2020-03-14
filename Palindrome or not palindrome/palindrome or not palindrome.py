my_str = "Rise to vote, sir."

#define punction
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

#remove punction from the string
no_punct = ""
for char in my_str:
	if char not in punctuations:
		no_punct += char

no_punct.lower
rev = no_punct[::-1]

if no_punct == rev:
	print("\nYes, it's a palindrome")
else:
	print("\nNo, it isn't a palindrome")