label vegetablegarden:

        label splashscreen2:
                scene black
                with Pause(0.2)


                show text "The Vegetable Garden" with dissolve
                with Pause(0.5)

                hide text with dissolve

                scene black with dissolve
                with Pause(0.2)



        scene bg_vegetablegarden

        show rabbit happy with Dissolve (0.7)
        rabbit "Howdy there"
        rabbit "I am Ruby Rabbit, welcome to my vegetable garden"

        hide rabbit happy
        show rabbit happy idle

        show badger neutral at left with moveinleft
        badger "Nice to meet you Ruby, and what is it you do out here?"

        hide badger neutral
        show badger neutral idle

        hide rabbit happy idle
        show rabbit neutral
        rabbit "Well I tend to the crops you see"
        rabbit "Here at the Eco Hub we use compost to grow all out vegetables"

        hide rabbit neutral
        show rabbit neutral idle
        hide badger neutral idle
        show badger neutral
        badger "What does that mean exactly?"

        hide rabbit neutral idle
        show rabbit happy
        hide badger neutral
        show badger neutral idle
        rabbit "We use plant and food waste like orange peels to soil to make a
        natural plant fertilizer"

        rabbit "Then the veg that doesn’t go out to the townsfolk will be
        used to create more compost"

        rabbit "It’s sustainable and makes our carrots so very yummy!"

        rabbit "The best part is you could even do this at home! It’s so easy, just keep
        all your fruit and veg waste to add to your soil "

        hide rabbit happy
        show rabbit happy idle
        hide badger neutral
        show badger happy

        badger "That is wonderful,
        perhaps you have some spare for me to take home with me"

        hide rabbit happy idle
        show rabbit sad
        hide badger happy
        show badger happy idle

        rabbit "I wish I did but as you can see, someone has pulled up all my veg!"

        hide rabbit sad
        show rabbit sad idle
        hide badger happy idle
        show badger thinking

        badger "May I ask you some questions Miss Rabbit?"
        hide rabbit sad idle
        show rabbit sad
        hide badger thinking
        show badger noting idle

        rabbit "Go ahead."

default questionAsked2 = []

label questionAskedMenu2:
    # Check if two questions have already been asked
    if len(questionAsked2) >= 2:
        ## TODO: Change Barry's Temp Dialogue.
        badger "That's all my questions for now, I will now examine the crime scene."
        jump vegetablegardenInvestigation

    # Display the menu for asking questions
    menu:
        # Each question is shown only if it has not been asked before
        "Where were you the night of the vandalism?" if "vandalism" not in questionAsked2:
            rabbit "Why last night I was cooking a delicious veggie stew."
            $ questionAsked2.append("vandalism")
            jump questionAskedMenu2

        "Who do you think did the crime?" if "crime" not in questionAsked2:
            rabbit "I think it might have been Freddie the Frog or Cooper the Cow, you need to have a gardener's touch to be able to pull up the crops like that."
            $ questionAsked2.append("crime")
            jump questionAskedMenu2

        "Why do you think someone would do this?" if "reason" not in questionAsked2:
            rabbit "I don’t know. The eco hub is such an amazing place I don’t know why anyone would do this."
            $ questionAsked2.append("reason")
            jump questionAskedMenu2


            
