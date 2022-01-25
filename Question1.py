input = "Python is a case sensitive language"
#need to find length of the string
#a)
print(len(input))
#b)Now reversing the string
reverse = "Python is a case sensitive language"[::-1]
print(reverse)
#c)Now using slice function to seperate
sliced = input[10:26]
print(sliced)
#d)Replace the phrase
sliced = "object oriented"
print(sliced)
#e)indexing a substring
index = input.index("a")
print(index)
#f)removing white spaces
def remove(input):
    return input.replace(" ","")
print(remove(input))
