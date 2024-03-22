label EcoHub:

screen mapScreen:

    add "map.png"
    #Greenhouse
    imagebutton:

        xpos 483
        ypos 506

        auto "GH_%s.png"

        action [Hide("displayTextScreen"), Jump("greenhouse")]

        hovered [Show("displayTextScreen", displayText = "Click here!"), Play("sound", "audio/click.wav") ]
        unhovered Hide("displayTextScreen")

##display text
screen displayTextScreen:
    default displayText = ""
    vbox:
        xalign 0.177
        yalign 0.506
        frame:
            text displayText
        