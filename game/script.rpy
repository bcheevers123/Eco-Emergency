# The script of the game goes in this file.

# Define a function to display the polaroid image and fade out at the end of the dialogue

#All functions go inside init python
init python:
    from renpy.display import im
    from renpy.display.im import matrix
    def display_polaroid(loc, clue):
        return "polaroid/{}/{}.png".format(loc, clue)


    # Import Matrix Manipulation Library
    def check_investigations():
        global show_office, completed_areas_count
        completed_areas = 0

        for area, clues in game_clues.items():
            if all(clues.values()):
                completed_areas += 1

        completed_areas_count = completed_areas  # Update the global variable with the number of completed areas

        if completed_areas >= 3:
            show_office = True
    





# Declare characters used by this game. The color argument colorizes the
# name of the character.
image splash = "Logo Final.png"
label splashscreen:
    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(2)

    hide splash with dissolve

    show text "The Eco Emergency" with dissolve
    with Pause(2)

    hide text with dissolve

    scene black with dissolve
    with Pause(1)

    return




#TODO Add clue names to the checklist/inventory dictionary
default game_clues = {
    "greenhouse": {
        "window": False,
        "spraypaint": False,
        "fertilizer": False
    },
    "pond": {
        "broken pipe": False,
        "footprints": False,
        "trash": False
    },
    "vegetable_garden": {
        "hoove print": False,
        "carrots": False,
        "cloth": False
    },
    "solar_panel": {
        "broken solar panel": False,
        "cut wires": False,
        "dirty solar panel": False
    },
    "recycling_area": {
        "broken machine": False,
        "trash bag": False,
        "ripped paper": False
    }
}

# Flag variable to check if we should show office.
default show_office = False

#Global counter of areas completed
default completed_areas_count = 0



# The game starts here.



label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_office

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Fox serious with fade

    # These display lines of dialogue.

    Fox "Welcome, Detective Billy Badger, to the eco hub!"

    Fox "This incredible community practices sustainability in different ways to help us look after our planet"

    Fox "Climate change is a big issue and the eco hub do amazing things to battle this"

    Fox "Unfortunately, someone broke into the building recently and vandalised it… "

    Fox "We are led to believe it was an employee since the criminal seemed to know their way around the site  "

    Fox "As there are no obvious signs of break in, meaning they had a key"

    Fox "Your assignment is to explore the site"

    Fox "Question the employees"

    Fox "and search for clues to decide who you think it was"
    
    Fox "Here are all the employees"
    
    # This is where fox disapear and the 5 Characters come
    
    hide Fox serious with fade

    show employees with dissolve

    Fox "Each one of these employees works at a different part of the eco hub"

    Fox "Here is a map of the eco hub, let’s take a look"

    #The screen changes to a map of the eco hub

    hide employees 
    show map with fade

    Fox "We don’t have enough time for you to go everywhere"

    Fox "Choose at least two locations and report back to the office!"

    Fox "Good luck Detective, I know you can do it…"

    call screen mapScreen

#    show map with fade 
    
#    Fox "We don’t have enough time for you to go everywhere"

#    Fox "After that, go to one outside location and one inside location"

#    Fox "Good luck Detective, I know you can do it…"

###player picks the eco hub 
#    hide bg_office with ease 

#    hide eco hub map 
#    show greenhouse 

#    show cow neutral with Dissolve (0.7)
#    hide cow neutral

#    show cow happy 

#    cow "Hello, my name is Cooper the Cow!"

#    cow "Welcome to the greenhouse!"

#    show badger neutral at left with moveinleft

#    badger "Hello Cooper, I’m Detective Billy Badger. What is your job in the greenhouse? "

#    cow "My job is to help the trees and plants grow"

#    badger "How do you do this?"

#    hide cow happy 
#    show cow neutral 

#    cow "I build homes for the trees to grow as big as they need"
#    cow "and water the plants every day so they can grow strong"

#    badger "And how does this help earth"

#    cow "Trees and plants make oxygen, which we all need to breathe"

#    cow "Here at the eco hub, I look after the trees so when they’re big enough, they can be planted somewhere in the world"

#    cow "Our goal is to have lots more plants and trees to help make our air healthy"
#    cow "and it's not just the big plants and trees we have here, it's the little plants you can have at home that help too!"

#    cow "Everyone should have plants in their home!"

#    hide badger neutral 
#    show badger happy

#    badger "That is very interesting, Cooper!"

#    hide badger happy with dissolve
#    show badger noting

#    badger "You might already know, but some vandalism has been discovered in the Eco Hub"
#    badger "May I ask you a few questions?"

#    hide cow neutral with dissolve
#    show cow nervous 

#    cow "Umm, o-okay"

    ###the player now will now ask two questions of the three possible choices


#    badger "Someone broke into a building recently and valdalized it..."
   
#    $ questionAsked = []

#    menu questionAskedMenu:
#        set questionAsked
#        "Where were you the night of the vandalsim?":
#            cow "Well, I, uh, I was playing video games with my friends"
#            pass
#            jump questionAskedMenu
#        
#        "Who do you suspect broke into the eco-hub?":
#            cow "Hmm, you see… Sheldon has been acting very s-s-suspicious. He’s very sneaky, I think he is capable of the crime."
#            pass
#            jump questionAskedMenu

#        "Why do you think someone would do this?":
#            cow "The hub does good things, I don't know why anyone would want to ruin it… "
#            pass
#            jump questionAskedMenu
    
#    jump GHclues
        
#label GHclues:
#    show greenhouse

