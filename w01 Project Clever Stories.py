def create_mad_lib():
    # Collect inputs from the user
    print("Please enter the following:")
    
    adjective1 = input("adjective: ")
    adjective2 = input("adjective: ")
    animal = input("animal: ")
    verb1 = input("verb: ")
    exclamation = input("exclamation: ")
    verb2 = input("verb: ")
    verb3 = input("verb: ")
    
    # Helper function to determine whether to use "a" or "an"
    def get_article(word):
        vowels = "aeiouAEIOU"
        return "an" if word and word[0] in vowels else "a"
    
    # Get the appropriate articles
    adj_article = get_article(adjective1)
    adj_article = get_article(adjective2)
    animal_article = get_article(animal)
    
    # The story template
    story = f"""
Your story is:

And it came to pass that I was having a {adjective1} day. I was minding my own business when suddenly, {adj_article} very
{adjective2} {animal_article} {animal} appeared out of nowhere, it started to {verb1} wildly across the room. 
"{exclamation.upper()}!" I shouted, my heart racing. Without thinking, I decided to {verb2}, hoping it 
would help. To my surprise, the {animal} stopped and stared at me, as if trying to decide what 
to do next. Just when I thought it was over, it began to {verb3}, leaving everyone in the room 
completely speechless. What a day!
"""
    
    # Display the completed story
    print(story)

# Run the Mad Lib generator
if __name__ == "__main__":
    create_mad_lib()