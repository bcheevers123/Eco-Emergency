label greenhouse:
    scene bg_greenhouse
    
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

    ###the player now will now ask two questions of the three possible choices

    hide badger noting idle
    show badger noting
    badger "Someone broke into a building recently and valdalized it..."
   
    $ questionAsked = []

    menu questionAskedMenu:
        set questionAsked
        "Where were you the night of the vandalsim?":
            cow "Well, I, uh, I was playing video games with my friends"
            pass
            jump questionAskedMenu
        
        "Who do you suspect broke into the eco-hub?":
            cow "Hmm, you see… Sheldon has been acting very s-s-suspicious. He’s very sneaky, I think he is capable of the crime."
            pass
            jump questionAskedMenu

        "Why do you think someone would do this?":
            cow "The hub does good things, I don't know why anyone would want to ruin it… "
            pass
            jump questionAskedMenu



        

            



    