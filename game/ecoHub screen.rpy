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
        xpos 483
        ypos 506
        idle "GH_idle.png"  # Replace with your image file for the idle state.
        hover "GH_hover.png"  # Replace with your image file for the hover state.
        action [Hide("displayTextScreen"), Jump("greenhouse")]
        hovered [Show("displayTextScreen", displayText = "Click here!"), Play("sound", "audio/click.wav")]
        unhovered Hide("displayTextScreen")

# This is the definition of the displayTextScreen screen.
screen displayTextScreen(displayText=""):
    vbox:
        xalign 0.177
        yalign 0.506
        frame:
            text displayText