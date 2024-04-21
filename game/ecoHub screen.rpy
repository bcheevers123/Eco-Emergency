## This was written incorrectly. I have fixed.

# This label is what you jump to when you want to display the mapScreen.
label EcoHub:
    call screen mapScreen
    # Add any additional logic or dialogue here if necessary.
    # The return statement will return control to the point where the label was called.
    return

# This is the definition of the mapScreen screen.
screen mapScreen:
    add "map.png"

    # Define an image button for the greenhouse.
    imagebutton:
        xpos 762
        ypos 341
        idle "GH_idle.png"  # Replace with your image file for the idle state.
        hover "GH_hover.png"  # Replace with your image file for the hover state.
        action Jump("greenhouse")
        hovered [Show("displayText", text="Greenhouse"), Play("sound", "audio/click.wav")]
        unhovered Hide("displayText")

    imagebutton:
        xpos 0
        ypos 669
        idle "pond_idle.png"  # Replace with your image file for the idle state.
        hover "pond_hover.png"  # Replace with your image file for the hover state.
        action Jump("pond")
        hovered [Show("displayText", text="Pond"), Play("sound", "audio/click.wav")]
        unhovered Hide("displayText")

    imagebutton:
        xpos 1460   
        ypos 529
        idle "office_idle.png"  # Replace with your image file for the idle state.
        hover "office_hover.png"  # Replace with your image file for the hover state.
        action Jump("office")
        hovered [Show("displayText", text="office"), Play("sound", "audio/click.wav")]
        unhovered Hide("displayText")



# This is the definition of the displayTextScreen screen.
#screen displayTextScreen(displayText=""):
#    vbox:
#        xalign 762
#        yalign 341
#        frame:
#            text displayText