import time
import sys

def slow_type(text, delay=0.01):
    """Print text with a typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after the text is printed

def horrow_game():
    slow_type("Happy Spring Break!")
    slow_type("After a long day in the beach sun, you and your friends decide to relax and go to the movies.")
    slow_type("The movie was really funny, you are just having a good time and laughing.")
    slow_type("You just blink and the lights go out, and you hear a loud crash.")
    slow_type("Then you turn around and find yourself alone in an old abandoned movie theater.")
    slow_type("You start watching moments of your childhood on the screen.")
    slow_type("Be careful to type the right words, or it will be the end of you...your game I mean...yeah...")

    choice1 = input("Do you want to watch the MOVIE or go EXPLORE the theater? >> ").strip().lower()

    if choice1 == "movie":
        slow_type("\nYou are tempted to stay and watch but a deep voice says:")
        slow_type("\n'Every moment you watch is a moment gone from your life.'")
        slow_type("\nYou can feel your memories fading away from you.")
        slow_type("You are unsure of what is going on, you look around for clues")
        slow_type("Do you try to STAY to figure out what's going on, or escape to EXPLORE the empty hallways?")
        choice2 = input(">> ").strip().lower()

        if choice2 == "stay":
            slow_type("\nThe screen starts to resemble a door.")
            slow_type("Do you go through the DOOR or STAY?")
            choice3 = input(">> ").strip().lower()

            if choice3 == "door":
                slow_type("\nYou walk through the door and find the projector room.")
                slow_type("You see a big red button that says 'EJECT.' Do you press it?")
                choice4 = input(">> ").strip().lower()

                if choice4 == "eject":
                    slow_type("\nThe movie stops and the lights come back on.")
                    slow_type("You find yourself back in the theater with your friends.")
                    slow_type("You breathe a sigh of relief. You are confused, but you are out!")
                else:
                    slow_type("\nYou decide to stay and watch. The screen starts to glow.")
                    slow_type("You feel yourself being pulled in. You scream, but no one hears you.")
                    slow_type("You are trapped in the movie forever. Game over.")
            if choice3 == "stay":
                slow_type("\nYou decide to stay and watch. The screen starts to glow.")
                slow_type("You feel yourself being pulled in. You scream, but no one hears you.")
                slow_type("You are trapped in the movie forever. Game over.")

        elif choice2 == "explore":
            slow_type("\nThe walls are covered in movie posters from your life.")
            slow_type("One of them looks back at you and stares.")
            slow_type("Do you TALK with it or RUN away?")
            choice3 = input(">> ").strip().lower()

            if choice3 == "talk":
                slow_type("Suddenly, the poster comes to life and pulls you in.")
                slow_type("You are trapped in that moment of your life forever. Game over.")
            elif choice3 == "run":
                slow_type("\nYou hear a voice behind you but don't look back. You run for your life.")
                slow_type("You find the projector room with the lights on.")
                slow_type("Do you ENTER the room or RUN away?")
                choice4 = input(">> ").strip().lower()

                if choice4 == "enter":
                    slow_type("\nYou enter the room and find the manager of the theater.")
                    slow_type("He welcomes you and says: 'You are the first one to find me!'")
                    slow_type("Finally! It is now my turn to go back to the real world.")
                    slow_type("You are now the man in charge of the theater.")
                    choice5 = input("Do you HEAR him or FIGHT him? >> ").strip().lower()

                    if choice5 == "hear":
                        slow_type("\nSince you are in charge, you can do whatever you want.")
                        slow_type("You can see the future and the past.")
                        slow_type("You will live forever as long as you are in the theater.")
                        slow_type("But if you tell anyone, you will be trapped forever.")
                        choice6 = input("He starts to walk away, do you FOLLOW him or STAY? >> ").strip().lower()

                        if choice6 == "follow":
                            slow_type("\nYou follow him and he is going to his death")
                            slow_type("I had been waiting for this for milenia...")
                            slow_type("I didn't expect you to wanted it too.")
                            slow_type("You just disapear forever. Game over.")
                        elif choice6 == "stay":
                            slow_type("\nYou decide to trust him and stay.")
                            slow_type("Just as he said, you can see the future and the past.")
                            slow_type("You can live forever in the theater.")
                            slow_type("You can see your friends and family but they can't see you.")
                            slow_type("You scream, but no one hears you.")
                            slow_type("You live beyond time and space now.")
                            slow_type("I hope you like it though")
                    if choice5 == "fight":
                        slow_type("\nOkay! Okay! I have been here for way too long.")
                        slow_type("And I can see that you are not easily tricked...")
                        slow_type("My boss wanted me to trap you here and he would let me go.")
                        slow_type("But together we could free us both...")
                        choice6 = input("Do you JOIN him or FIGHT him to the end? >> ").strip().lower()

                        if choice6 == "join":
                            slow_type("\nYou find the final boss of the theater.")
                            slow_type("He is the one who trapped you here.")
                            slow_type("You both fight him and win.")
                            slow_type("You both can now leave the theater.")
                            slow_type("You shave freed all people previousl trapped in the theater!")
                            slow_type("You are a true hero!")
                        elif choice6 == "fight":
                            slow_type("\nYou yell: 'I will never join you!'")
                            slow_type("He laughs and says: 'You are wrong but I would have done the same.'")
                            slow_type("You fight him and win.")
                            slow_type("Someone enters the room and tells you: 'Congrats! You are my new teather manager!'")
                            slow_type("You are in control of the place but you will never leave.")
                            slow_type("You can see your friends and family on the screen but they can't see you.")
                            slow_type("You scream, but no one hears you.")
                            slow_type("Enjoy your new job!")
                elif choice4 == "run":
                    slow_type("\nYou find yourself in an infinite hallway.")
                    slow_type("This was your only chance to escape.")
                    slow_type("You are trapped forever. Game over.")
            else:
                slow_type("\nYou are confused and don't know what to do.")
                slow_type("The voice behind you gets closer and closer.")
                slow_type("You are trapped forever. Game over.")
    elif choice1 == "explore":
        slow_type("\nYou find your friends in the lobby.")
        slow_type("They are all staring at the screen, but you are not sure what they are watching.")
        slow_type("You try to talk to them, but they don't respond.")
        slow_type("Hint: You can tell them or type anything you want.")
        slow_type("Do you TALK with them or look for the EXIT?")
        choice2 = input(">> ").strip().lower()

        if choice2 == "talk":
            slow_type("\nThey slowly turn to you and say: 'You shouldn't be here.'")
            slow_type("They freak out and start blaming you for getting them all trapped.")
            slow_type("You trapped us all forever! Game over.")
        elif choice2 == "exit":
            slow_type("\nYou find the exit door and run outside.")
            slow_type("You look back and there is no theater.")
            slow_type("You are free!")
        else:
            slow_type("That's not a valid option...")
            slow_type("CONGRATULATIONS!")
            slow_type("You open your eyes and find yourself back in the theater.")
            slow_type("You fell asleep and it was all a dream.")
            slow_type("You are free to go back with your friends and enjoy your spring break!")

#Start the game
horrow_game()