## This was written incorrectly. I have fixed.


# Saturation definitions
image map_two_areas_completed = "map_two_areas_completed.png"
image map_one_areas_completed = "map_one_areas_completed.png"
image map_zero_areas_completed = "map_zero_areas_completed.png"


# This label is what you jump to when you want to display the mapScreen.
label EcoHub:

    $ check_investigations()


    call screen mapScreen
    # Add any additional logic or dialogue here if necessary.
    # The return statement will return control to the point where the label was called.
    return

# This is the definition of the mapScreen screen.
screen mapScreen:
    # Choose the map image based on the number of areas completed
    if completed_areas_count >= 3:
        add "map_three_areas_completed"
        
    elif completed_areas_count == 2:
        add "map_two_areas_completed"
    elif completed_areas_count == 1:
        add "map_one_areas_completed"
    else:
        add "map_zero_areas_completed"

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
        xpos 206
        ypos 171
        idle "garden_idle.png"  # Replace with your image file for the idle state.
        hover "garden_hover.png"  # Replace with your image file for the hover state.
        action Jump("vegetablegarden")
        hovered [Show("displayText", text="Vegetable Garden"), Play("sound", "audio/click.wav")]
        unhovered Hide("displayText")


    imagebutton:
        xpos 1302
        ypos 23
        idle "solar_idle.png"  # Replace with your image file for the idle state.
        hover "solar_hover.png"  # Replace with your image file for the hover state.
        action Jump("solarpanels")
        hovered [Show("displayText", text="Solar Panels"), Play("sound", "audio/click.wav")]
        unhovered Hide("displayText")

    imagebutton:
        xpos 1246
        ypos 88
        idle "recycling_idle.png"  # Replace with your image file for the idle state.
        hover "recycling_hover.png"  # Replace with your image file for the hover state.
        action Jump("recyclingcentre")
        hovered [Show("displayText", text="Recycling Centre"), Play("sound", "audio/click.wav")]
        unhovered Hide("displayText")

    if show_office:
        imagebutton:
            xpos 1476   
            ypos 546
            idle "office_idle.png"  # Replace with your image file for the idle state.
            hover "office_hover.png"  # Replace with your image file for the hover state.
            action Jump("office")
            hovered [Show("displayText", text=""), Play("sound", "audio/click.wav")]
            unhovered Hide("displayText")
        
        add "images/sign.png"



# This is the definition of the displayTextScreen screen.
#screen displayTextScreen(displayText=""):
#    vbox:
#        xalign 762
#        yalign 341
#        frame:
#            text displayText