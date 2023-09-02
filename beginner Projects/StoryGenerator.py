# Our task is to generate a random story every time the user runs the program. 
# I will first store the parts of the stories in different lists, then the Random module can be used to select the random parts of the story stored in different lists:

import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))


#some of the outputs and you can try different things with random module
# A long time ago, an elephant that lived in India, went to the school and made a lot of friends
# A few years ago, a turtle that lived in England, went to the cinema and wrote a book
