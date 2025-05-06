"""
Class: CSE110 Section: A7 Student Name: Alejandro Garcia Trujillo
Project Clever Stories
Creativity Credit Explanation: I changed the story template and addded my own inputs.
I also uppercased the exclamation mark in the story.
"""

#Collect inputs from the user
print("Please enter the information requested: ")

feeling = input("a feeling: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
verb4 = input("verb: ")
exclamation = input("exclamation: ")
adjective = input("adjective: ")

#Helper function to determine whether to use "a" or "an"
def get_article(word):
    vowels = "aeiouAEIOU"
    return "an" if word and word[0] in vowels else "a"


#The story template
story = f"""
Your story is:

One morning I woke up just very {feeling}. So I decided to {verb1}.
Later on I was told to {verb2} and {verb3}, which sounded strange and I yelled "{exclamation.upper()}! are you {adjective}?"
I was so confused that I decided to {verb4}. And in the end it was a combination of {verb3} and {verb4}
that solved it for me.
"""

#Display the story
print(story)