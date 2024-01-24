import re # regular expression helps to match the pattern in the text
text = "This is the life"
pattern = r"the"
match = re.match(pattern, text)
if match: # the code in the if condition will run only if the match is found
    print("Match found: ", match.group()) # group() method returns the matched string
else:
    print("No match found")