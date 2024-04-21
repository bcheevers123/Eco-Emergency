label pond:

    label splashscreen4:
    scene black
    with Pause(0.2)


    show text "The Pond" with dissolve
    with Pause(0.5)

    hide text with dissolve

    scene black with dissolve
    with Pause(0.2)


    scene bg_pond

    show frog neutral with Dissolve(0.7)

    frog "Welcome to the pond friend"
    frog "My name is Freddie Frog"

    hide frog neutral
    show frog neutral idle
    show badger happy at left with moveinleft

    badger "What a lovely garden!"

    hide frog neutral idle
    show frog neutral
    hide badger happy
    show badger happy idle

    frog "It’s not just a garden. It’s a home for the wildlife"
    frog "I tend to the nature to attracts bugs and give them a home"
    frog "I worry that wildlife is dying out, and we must nurture it"
    frog "It’s important to let the wildlife grow freely. I ensure the pond stays nice and clean for the fish and the bugs that fly by"
    frog "But as you can see, the pond has been ruined by someone"

    hide badger happy idle
    show badger noting

    badger "May I ask you some questions?"
    frog "Go ahead."

default questionAsked4 = []

label questionAskedMenu4:
    # Check if two questions have already been asked
    if len(questionAsked4) >= 2:
        ## TODO: Change Barry's Temp Dialogue.
        badger "That's all my questions for now, I will now examine the crime scene."
        jump pondInvestigation

    # Display the menu for asking questions
    menu:
        # Each question is shown only if it has not been asked before
        "Where were you the night of the vandalism?" if "vandalism" not in questionAsked4:
            frog "Well I was in my house tending to my fish."
            $ questionAsked4.append("vandalism")
            jump questionAskedMenu4

        "Who do you think did the crime" if "crime" not in questionAsked4:
            frog "I think it might have been Maggie the Magpie! She has the tools to do this kind of damage."
            $ questionAsked4.append("crime")
            jump questionAskedMenu4

        "Why do you think someone would do this?" if "reason" not in questionAsked4:
            frog "I have no idea. Who would want to ruin the home for the bugs it's just horrible!"
            $ questionAsked4.append("reason")
            jump questionAskedMenu4
