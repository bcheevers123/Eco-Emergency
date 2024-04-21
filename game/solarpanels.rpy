label solarpanels:


    label splashscreen5:
    scene black
    with Pause(0.2)


    show text "The Solar Panels" with dissolve
    with Pause(0.5)

    hide text with dissolve

    scene black with dissolve
    with Pause(0.2)


    scene bg_solarpanels

    show magpie happy with Dissolve(0.7)

    magpie "Hi there! Welcome to the solar panels"
    magpie "I’m Maggie and I am the solar panel engineer"

    hide magpie happy
    show magpie happy idle
    show badger thinking at left with moveinleft

    badger "What do the solar panels do?"

    hide magpie happy idle
    show magpie happy
    hide badger thinking
    show badger noting idle

    magpie "Solar panels are the future!"
    magpie "The solar panels absorb the sunlight and use it to create electricity"
    magpie "These solar panels are powering the whole eco hub"
    magpie "They’re very good for the planet and we try to encourage people to get them on their homes"
    magpie "You can even get smaller versions, like little lights for the garden that are solar powered"

    hide magpie happy
    show magpie neutral idle
    hide badger noting idle
    show badger happy

    badger "WOW! that is amazing"

    hide magpie neutral idle
    show magpie sad
    hide badger happy
    show badger neutral idle

    magpie "Yes but since some of them have been broken, we don’t have enough electricity"

    hide magpie sad
    show magpie sad idle
    hide badger neutral idle
    show badger noting

    badger "That is horrible"
    badger "May I ask you some questions?"

    hide magpie sad idle
    show magpie sad

    magpie "Okay then"

default questionAsked5 = []

label questionAskedMenu5:
    # Check if two questions have already been asked
    if len(questionAsked5) >= 2:
        ## TODO: Change Barry's Temp Dialogue.
        badger "That's all my questions for now, I will now examine the crime scene."
        jump solarpanelsInvestigation

    # Display the menu for asking questions
    menu:
        # Each question is shown only if it has not been asked before
        "Where were you the night of the vandalism?" if "vandalism" not in questionAsked5:
            magpie "I was at home trying to complete my puzzle."
            $ questionAsked5.append("vandalism")
            jump questionAskedMenu5

        "Who do you think did the crime?" if "crime" not in questionAsked5:
            magpie "I think it was the Cooper the cow or Sheldon the Snake, they look like they’re strong enough to smash up the solar panels."
            $ questionAsked5.append("crime")
            jump questionAskedMenu5

        "Why do you think someone would do this?" if "reason" not in questionAsked5:
            magpie "Clearly they have no respect for the environment or the eco hub!"
            $ questionAsked5.append("reason")
            jump questionAskedMenu5
