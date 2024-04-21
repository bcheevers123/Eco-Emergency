label recyclingcentre:


    label splashscreen3:
    scene black
    with Pause(0.2)


    show text "The Recycling Centre" with dissolve
    with Pause(0.5)

    hide text with dissolve

    scene black with dissolve
    with Pause(0.2)



    scene bg_recyclingunit


    show snake happy with Dissolve(0.7)

    snake "Welcome to the Recycling Unit, my name is Sheldon the Snake "

    hide snake happy
    show snake happy idle
    show badger neutral at left with moveinleft

    badger "Hello there, Sheldon, what do you do here at the recycling unit?"

    hide snake happy idle
    show snake happy
    hide badger neutral
    show badger neutral idle

    snake "My job is to separate alllllll of the rubbish before it goes into the machines."

    hide snake happy
    show snake happy idle
    hide badger neutral
    show badger noting

    badger "Why do you do this?"

    hide snake happy idle
    show snake neutral
    hide badger noting
    show badger noting idle

    snake "Well, it’s to prevent every bit of rubbish going to landfills or in the ocean"
    snake "Separating the rubbish means we can create new products instead of it being left in the bin."
    snake "Here we have plastic from the bin, instead of it going to landfill it can now be made into new plastic bottles!"
    snake "Saving your plastic at home will help me do my job!"

    hide snake neutral
    show snake happy idle
    hide badger noting iddle
    show badger happy

    badger "Very good, being recyclable!"

    hide badger happy
    show badger noting

    badger "Thank you for telling me this, May I ask you some questions to do with the vandalism?"

    hide snake happy idle
    show snake sup


    snake "OH! Yes... of ... course you can."


default questionAsked3 = []

label questionAskedMenu3:
    # Check if two questions have already been asked
    if len(questionAsked3) >= 2:
        ## TODO: Change Barry's Temp Dialogue.
        badger "That's all my questions for now, I will now examine the crime scene."
        jump recyclingcentreInvestigation

    # Display the menu for asking questions
    menu:
        # Each question is shown only if it has not been asked before
        "Where were you the night of the breakin?" if "breakin?" not in questionAsked3:
            snake "I was in an engineering class. We learnt how to make bike’s from recycled plastic and metals!"
            $ questionAsked3.append("vandalism")
            jump questionAskedMenu3

        "Who do you suspect broke into the eco-hub?" if "suspect" not in questionAsked3:
            snake "I think it might be Freddie the frog, he is the last one to leave the hub at night… no one would have spotted him."
            $ questionAsked3.append("suspect")
            jump questionAskedMenu3

        "Why do you think someone would do this?" if "reason" not in questionAsked3:
            snake "Our hub is very special, we do lots of good work for the environment. Maybe someone is jealous..."
            $ questionAsked3.append("reason")
            jump questionAskedMenu3
