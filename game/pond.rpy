init:
    #Untested code
    # Image definitions for different states of completion
    image bg_pond = "images/pond_zero_areas_completed.png"  # Default, no areas completed
    image bg_pond_1 = "images/pond_one_areas_completed.png"  # 1 area completed
    image bg_pond_2 = "images/pond_two_areas_completed.png"  # 2 areas completed
    image bg_pond_3 = "images/pond_three_areas_completed.png"  # 3 areas completed



label pond:

    label splashscreen4:
    scene black
    with Pause(0.2)


    show text "The Pond" with dissolve
    with Pause(0.5)

    hide text with dissolve

    scene black with dissolve
    with Pause(0.2)

    if completed_areas_count == 0:
        scene bg_pond
    elif completed_areas_count == 1:
        scene bg_pond_1
    elif completed_areas_count == 2:
        scene bg_pond_2
    elif completed_areas_count >= 3:
        scene bg_pond_3
    with dissolve
    #scene bg_pond

    show frog neutral with Dissolve(0.7)

    frog "Welcome to the pond friend"
    frog "My name is Freddie Frog"

    hide frog neutral
    show frog neutral idle
    show badger happy at left with moveinleft

    badger "What a lovely area!"

    hide frog neutral idle
    show frog happy
    hide badger happy
    show badger happy idle

    frog "It’s not just any area." 
    frog "It’s a home for the wildlife!"

    hide frog happy
    show frog neutral

    frog "I tend to the nature to attracts bugs and give them a home"
    
    hide frog neutral with dissolve
    show frog sad

    frog "I worry that wildlife is dying out, and we must nurture it"
    frog "It’s important to let the wildlife grow freely." 
    frog "I ensure the pond stays nice and clean for the fish and the bugs that fly by"
    frog "But as you can see, the pond has been ruined by someone"

    hide frog sad
    show frog sad idle
    hide badger happy idle
    show badger noting with dissolve

    badger "May I ask you some questions?"


    show frog happy

    frog "Go ahead."

    hide frog happy
    show frog thinking with dissolve

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


# Define the screen where the investigation takes place
screen pondInvestigationScreen:
    # Display the background for the pond investigation

    #use if statement constuct found in ecoHub screen.rpy line 25
    if completed_areas_count >= 3:
        add "pond_three_areas_completed"
    elif completed_areas_count == 2:
        add "pond_two_areas_completed"
    elif completed_areas_count == 1:
        add "pond_one_areas_completed"
    else:
        add "pond_zero_areas_completed"

    # Image button for the window clue
    imagebutton:
        xpos 0  # Adjust this value based on the screenshot coordinates
        ypos 545
        #IMPORTANT: Must use relative paths
        idle "clue_buttons/pond/footprints.png"
        hover "clue_buttons/pond/footprints_hover.png"
        action [Play ("sound", "audio/camera.wav"), Jump("investigate_footprints")]
        hovered [Show("displayText", text="Examine the Footprints."), Play("sound", "audio/click.wav")]
        unhovered Hide("displayText")

    # Image button for the spray paint clue
    imagebutton:
        xpos 0  # Adjust this value based on the screenshot coordinates
        ypos 663
        idle "clue_buttons/pond/broken pipe.png"
        hover "clue_buttons/pond/broken pipe_hover.png"
        action [Play ("sound", "audio/camera.wav"), Jump("investigate_brokenpipe")]
        hovered [Show("displayText", text="Examine the pipe."), Play("sound", "audio/click.wav")]
        unhovered Hide("displayText")

    # Image button for the fertilizer clue
    imagebutton:
        xpos 756  # Adjust this value based on the screenshot coordinates
        ypos 615
        idle "clue_buttons/pond/trash.png"
        hover "clue_buttons/pond/trash_hover.png"
        action [Play ("sound", "audio/camera.wav"), Jump("investigate_trash")]
        hovered [Show("displayText", text="Look at the litter."), Play("sound", "audio/click.wav")]
        unhovered Hide("displayText")

    # Image button for back button
    imagebutton:
        xpos 1339  # Adjust this value based on the screenshot coordinates
        ypos 881
        idle "clue_buttons/misc/back_button.png"
        hover "clue_buttons/misc/back_button_hover.png"
        action [Play ("sound", "audio/back.wav"), Jump("back_from_pond")]
        hovered [Show("displayText", text="Leave the pond"), Play("sound", "audio/click.wav")]
        unhovered Hide("displayText")

# Screen to show text when image buttons are hovered
screen displayText(text=""):
    text text xpos 0.5 ypos 0.95 align (.5, .5)  # Center the text on the bottom of the screen

# The label where the actual investigation takes place
label pondInvestigation:
    # Clear away all the character sprites so they don't get in the way
    hide all
    # Call the SCREEN that contains the investigation UI
    call screen pondInvestigationScreen

    # The rest of game logic goes here
    return

label investigate_footprints:

    #Show Poloroid
    hide frog thinking
    show expression display_polaroid("pond", "footprints")
    with Pause (0.5)
    badger "I wonder who's footprints these belong to..."
    $ game_clues["pond"]["footprints"] = True

    # Hide Poloroid
    hide expression display_polaroid("pond", "footprints")
    # Must go "Back" to investigation screen
    jump pondInvestigation
    return


label investigate_brokenpipe:
    #Show Poloroid
    hide frog thinking
    show expression display_polaroid("pond", "broken_pipe")
    with Pause (0.5)
    badger "How strong are these pipes Mr Frog?"
    show frog thinking 
    frog "They are very strong. You would need the proper tools to unscrew them like that. Like a spanner!"
    $ game_clues["pond"]["broken pipe"] = True

    # Hide Poloroid
    hide expression display_polaroid("pond", "broken_pipe")
    # Must go "Back" to investigation screen
    jump pondInvestigation
    return

label investigate_trash:

    #Show Poloroid
    hide frog thinking
    show expression display_polaroid("pond", "trash")
    with Pause (0.5)
    badger "Looks like someone has put lots of rubbish into the pond!!"
    badger "I wonder who has access to lots of rubbish like this?"
    $ game_clues["pond"]["trash"] = True

    # Hide Poloroid
    hide expression display_polaroid("pond", "trash")
    # Must go "Back" to investigation screen
    jump pondInvestigation
    return

# User attempts to leave pond
label back_from_pond:
    # Check if they have obtained all three clues
    if all(value == True for value in game_clues["pond"].values()):
        # If all clues are true, player can proceed
        hide all
        badger "There is nothing more to investigate, time to move on..."
        jump EcoHub
    else:
        # If not all clues are true, player needs to investigate more
        hide frog thinking
        "I think there is still more to investigate!"
        jump pondInvestigation
        return
