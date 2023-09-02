# To create acronyms using Python, you need to write a python program that generates a short form of a word from a full sentence
 

user_input = str(input("Enter a Phrase: ")) 
# Enter the word 
text = user_input.split()
#  Now THe Text will be split into word
a = " "
for i in text:
    a = a+str(i[0]).upper() 
    # The Word first letter will be concatenated then
print(a)

# Let's say i Enter the word machine Learning or Data Engineer 
# Result will be 
#  ML & DE
