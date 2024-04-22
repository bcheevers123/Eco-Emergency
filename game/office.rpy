
label office:

    scene black
    with Pause(0.2)


    show text "Office" with dissolve
    with Pause(0.5)

    hide text with dissolve

    scene black with dissolve
    with Pause(0.2)

    scene bg_office
    
    show Fox serious with fade
    
    Fox "Detective, have you found the culprit?"

    jump finalInvestigation



screen finalScreen:
    add "bg_office.jpg"

    imagebutton:
        xpos 548    
        ypos 630
        idle "not_sure_idle.png"
        hover "not_sure_hover.png"
        action Jump ("not_ready")
        hovered Play("sound", "audio/click.wav")
        

    imagebutton:
        xpos 729    
        ypos 263
        idle "yes_idle.png"
        hover "yes_hover.png"
        action Jump ("ready")
        hovered Play("sound", "audio/click.wav")


label finalInvestigation:
    hide all
    call screen finalScreen

    return


label not_ready:
    hide all
    show Fox serious
    Fox "come back when you're ready"
    jump EcoHub


label ready:
    show Fox serious
    Fox "Okay detective let's get started"
    Fox "Select the culprit using these images"
    Fox "The fate of our Eco Hub lays on your hands..."
    hide Fox serious with fade
    call screen decisionScreen



screen decisionScreen:
    add "bg_office.jpg"

    imagebutton:
        xpos 98  
        ypos 184
        idle "polaroid/character/sheldon_idle.png"
        hover "polaroid/character/sheldon_hover.png"
        action Jump ("badEnding")
        hovered Play("sound", "audio/pencil.mp3")
        

    imagebutton:
        xpos 1227
        ypos 131
        idle "polaroid/character/cooper_idle.png"
        hover "polaroid/character/cooper_hover.png"
        action Jump ("goodEnding")
        hovered Play("sound", "audio/pencil.mp3")

    imagebutton:
        xpos 763    
        ypos 265
        idle "polaroid/character/ruby_idle.png"
        hover "polaroid/character/ruby_hover.png"
        action Jump ("badEnding")
        hovered Play("sound", "audio/pencil.mp3")

    imagebutton:
        xpos 420    
        ypos 618
        idle "polaroid/character/freddie_idle.png"
        hover "polaroid/character/freddie_hover.png"
        action Jump ("badEnding")
        hovered Play("sound", "audio/pencil.mp3")

    imagebutton:
        xpos 1164    
        ypos 633
        idle "polaroid/character/maggie_idle.png"
        hover "polaroid/character/maggie_hover.png"
        action Jump ("badEnding")
        hovered Play("sound", "audio/pencil.mp3")



label goodEnding:
    hide all

    show Fox happy
    Fox "We’ve got the DNA results back from the lab..."
    Fox "Congratulations detective you solved the crime!"

    hide Fox happy
    show badger happy

    badger " And I learnt so much about sustainability" 
    badger "we can also make small changes to help our planet"

    hide badger happy
    show Fox happy

    Fox "Thank you for helping detective"
    Fox "all of my stress is starting to fade away........"

    hide all

    scene black 
    with Pause (2)
    

    show Fox happy with dissolve 
    with Pause(2)
    hide Fox happy with fade 
    with Pause(1)

    show Fox evolved with fade 
    with Pause(3)

    return
    

label badEnding:
    hide all
    show Fox serious 
    
    Fox "Detective we have received news from the lab..."
    Fox "The DNA doesn’t match up, you’ve got the wrong guy"

    hide Fox serious with dissolve
    show Fox serious

    Fox "They've gotten away this time"
    Fox "We need another investigation"

    hide Fox serious
    show badger thinking

    badger "No problem, I’m eager to learn more about the eco hub anyway"

    hide badger thinking

    scene failed_investigation with fade
    with Pause(3)

    return




