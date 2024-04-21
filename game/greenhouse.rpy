init:
    #Untested code
    # Image definitions for different states of completion
    image bg_greenhouse = "images/bg_greenhouse_normal.jpg"  # Default, no areas completed
    image bg_greenhouse_1 = "images/bg_greenhouse_saturated_1.jpg"  # 1 area completed
    image bg_greenhouse_2 = "images/bg_greenhouse_saturated_2.jpg"  # 2 areas completed
    image bg_greenhouse_3 = "images/bg_greenhouse_saturated_3.jpg"  # 3 areas completed


label greenhouse:

    label splashscreen1:
    scene black
    with Pause(0.2)


    show text "Greenhouse" with dissolve
    with Pause(0.5)

    hide text with dissolve

    scene black with dissolve
    with Pause(0.2)


    #UNTESTED CODE
    if completed_areas_count == 0:
        scene bg_greenhouse
    elif completed_areas_count == 1:
        scene bg_greenhouse_1
    elif completed_areas_count == 2:
        scene bg_greenhouse_2
    elif completed_areas_count >= 3:
        scene bg_greenhouse_3
    with dissolve
    
    #scene bg_greenhouse

    show cow neutral with Dissolve (0.7)
    hide cow neutral

    show cow happy

    cow "Hello, my name is Cooper the Cow!"

    cow "Welcome to the greenhouse!"

    hide cow happy
    show cow happy idle

    show badger neutral at left with moveinleft

    badger "Hello Cooper, I’m Detective Billy Badger. What is your job in the greenhouse? "
    hide badger neutral
    show badger neutral idle

    show cow happy
    cow "My job is to help the trees and plants grow"
    hide cow happy
    show cow happy idle

    hide badger neutral idle
    show badger neutral
    badger "How do you do this?"

    hide badger neutral
    show badger neutral idle
    show cow neutral
    cow "I build homes for the trees to grow as big as they need"
    cow "and water the plants every day so they can grow strong"
    hide cow neutral
    show cow neutral idle

    hide badger neutral idle
    show badger neutral
    badger "And how does this help earth"
    hide badger neutral
    show badger neutral idle

    hide cow neutral idle
    show cow happy
    cow "Trees and plants make oxygen, which we all need to breathe"

    cow "Here at the eco hub, I look after the trees so when they’re big enough, they can be planted somewhere in the world"

    cow "Our goal is to have lots more plants and trees to help make our air healthy"
    cow "and it's not just the big plants and trees we have here, it's the little plants you can have at home that help too!"

    cow "Everyone should have plants in their home!"
    hide cow happy
    show cow happy idle

    hide badger neutral idle
    show badger happy

    badger "That is very interesting, Cooper!"

    hide badger happy with dissolve
    show badger noting

    badger "You might already know, but some vandalism has been discovered in the Eco Hub"
    badger "May I ask you a few questions?"
    hide badger noting
    show badger noting idle

    hide cow happy idle with dissolve
    show cow nervous

    cow "Umm, o-okay"

### The player will now ask two questions of the three possible choices

hide badger noting idle
show badger noting
badger "Someone broke into a building recently and vandalized it..."

# Initialize a list to track questions that have been asked
default questionAsked = []

label questionAskedMenu:
    # Check if two questions have already been asked
    if len(questionAsked) >= 2:
        ## TODO: Change Barry's Temp Dialogue.
        badger "That's all my questions for now, I will now examine the crime scene."
        jump greenhouseInvestigation

    # Display the menu for asking questions
    menu:
        # Each question is shown only if it has not been asked before
        "Where were you the night of the vandalism?" if "vandalism" not in questionAsked:
            cow "Well, I, uh, I was playing video games with my friends."
            $ questionAsked.append("vandalism")
            jump questionAskedMenu

        "Who do you suspect broke into the eco-hub?" if "suspect" not in questionAsked:
            cow "Hmm, you see… Sheldon has been acting very s-s-suspicious. He’s very sneaky, I think he is capable of the crime."
            $ questionAsked.append("suspect")
            jump questionAskedMenu

        "Why do you think someone would do this?" if "reason" not in questionAsked:
            cow "The hub does good things, I don't know why anyone would want to ruin it…"
            $ questionAsked.append("reason")
            jump questionAskedMenu




# Define the screen where the investigation takes place
screen greenhouseInvestigationScreen:
    # Display the background for the greenhouse investigation

    #use if statement constuct found in ecoHub screen.rpy line 25
    add "bg_greenhouse.jpg"

    # Image button for the window clue
    imagebutton:
        xpos 160  # Adjust this value based on the screenshot coordinates
        ypos 540
        #IMPORTANT: Must use relative paths
        idle "clue_buttons/greenhouse/window_gh.jpg"
        hover "clue_buttons/greenhouse/window_gh_hover.jpg"
        action Jump("investigate_window")
        hovered [Show("displayText", text="Examine the broken window."), Play("sound", "audio/click.wav")]
        unhovered Hide("displayText")

    # Image button for the spray paint clue
    imagebutton:
        xpos 860  # Adjust this value based on the screenshot coordinates
        ypos 360
        idle "clue_buttons/greenhouse/spray_gh.jpg"
        hover "clue_buttons/greenhouse/spray_gh_hover.jpg"
        action Jump("investigate_spraypaint")
        hovered [Show("displayText", text="Look at the spray paint."), Play("sound", "audio/click.wav")]
        unhovered Hide("displayText")

    # Image button for the fertilizer clue
    imagebutton:
        xpos 380  # Adjust this value based on the screenshot coordinates
        ypos 700
        idle "clue_buttons/greenhouse/fert_gh.jpg"
        hover "clue_buttons/greenhouse/fert_gh_hover.jpg"
        action Jump("investigate_fertilizer")
        hovered [Show("displayText", text="Check the bags of fertilizer."), Play("sound", "audio/click.wav")]
        unhovered Hide("displayText")

    # Image button for back button
    imagebutton:
        xpos 1339  # Adjust this value based on the screenshot coordinates
        ypos 881
        idle "clue_buttons/misc/back_button.png"
        hover "clue_buttons/misc/back_button_hover.png"
        action Jump("back_from_greenhouse")
        hovered [Show("displayText", text="Leave the greenhouse."), Play("sound", "audio/click.wav")]
        unhovered Hide("displayText")

# Screen to show text when image buttons are hovered
screen displayText(text=""):
    text text xpos 0.5 ypos 0.95 align (.5, .5)  # Center the text on the bottom of the screen

# The label where the actual investigation takes place
label greenhouseInvestigation:
    # Clear away all the character sprites so they don't get in the way
    hide all
    # Call the SCREEN that contains the investigation UI
    call screen greenhouseInvestigationScreen

    # The rest of your game logic goes here
    return

# Labels for the investigation of each clue

##TODO change this placeholder text
label investigate_window:

    #Show Poloroid
    show expression display_polaroid("greenhouse", "window")

    "That's interesting! The glass fragments fall outside of the greenhouse. That means that the rock was thrown from within the greenhouse."
    "Whoever the vandal is must have access to the greenhouse!"
    $ game_clues["greenhouse"]["window"] = True

    # Hide Poloroid
    hide expression display_polaroid("greenhouse", "window")
    # Must go "Back" to investigation screen
    jump greenhouseInvestigation
    return

label investigate_spraypaint:

    #Show Poloroid
    show expression display_polaroid("greenhouse", "spray")
    "Spray paint! Someone's twisted expression of art?!"
    $ game_clues["greenhouse"]["spraypaint"] = True

    # Hide Poloroid
    hide expression display_polaroid("greenhouse", "spray")
    # Must go "Back" to investigation screen
    jump greenhouseInvestigation
    return


label investigate_fertilizer:
    #Show Poloroid
    show expression display_polaroid("greenhouse", "fertilizer")

    "Hmm is this fertilizer?"
    "But it seems all the plants are dead.."
    $ game_clues["greenhouse"]["fertilizer"] = True

    # Hide Poloroid
    hide expression display_polaroid("greenhouse", "fertilizer")
    # Must go "Back" to investigation screen
    jump greenhouseInvestigation
    return

# User attempts to leave greenhouse
label back_from_greenhouse:
    # Check if they have obtained all three clues
    if all(value == True for value in game_clues["greenhouse"].values()):
        # If all clues are true, player can proceed
        show badger "There is nothing more to investigate, time to move on."
        hide all
        jump EcoHub
    else:
        # If not all clues are true, player needs to investigate more
        "I think there is still more to investigate!"
        jump greenhouseInvestigation
        return
