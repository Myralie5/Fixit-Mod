## script.rpy

# This is the main script that Ren'Py calls upon to start
# your mod's story! 

label start:

    # This label configures the anticheat number for the game after Act 1.
    # It is recommended to leave this as-is and use the following in your script:
    #   $ persistent.anticheat = renpy.random.randint(X, Y) 
    #   X - The minimum number | Y - The maximum number
    $ anticheat = persistent.anticheat

    # This variable sets the chapter number to 0 to use in the mod.
    $ chapter = 0

    # This variable controls whether the player can dismiss a pause in-game.
    $ _dismiss_pause = config.developer

    ## Names of the Characters
    # These variables set up the names of the characters in the game.
    # To add a character, use the following example below: 
    #   $ mi_name = "Mike". 
    # Don't forget to add the character to 'definitions.rpy'!
    $ s_name = "???"
    $ m_name = "???"
    $ n_name = "Girl 1"
    $ y_name = "Girl 2"
    $ d_name = "Girl's Voice"

    # This variable controls whether the quick menu in the textbox is enabled.
    $ quick_menu = True

    # This variable c ontrols whether we want normal or glitched dialogue
    # For glitched dialogue, use 'style.edited'.
    $ style.say_dialogue = style.normal

    # This variable controls whether Sayori is dead. It is recommended to leave
    # this as-is.
    $ in_sayori_kill = None
    
    # These variables controls whether the player can skip dialogue or transitions.
    $ allow_skipping = True
    $ config.allow_skipping = True

    ## The Main Part of the Script
    # This is where your script code is called!
    # 'persistent.playthrough' controls the playthrough number the player is on i.e (Act 1, 2, 3, 4)

    ## Example on calling scripts from DDLC.
    if persistent.playthrough == 0:
    #     # This variable sets the chapter number to X depending on the chapter
    #     # your player is experiencing ATM.
        $ chapter = 0

    #     # This call statement calls your script label to be played.
        call ch00_main
        
    #     # This call statement calls the poem mini-game to be played.
        call poem

    #     ## Day 1
        $ chapter = 1
        call ch01_main

    #     # This call statement calls the poem sharing minigame to be played.
        call poemresponse_start
        call ch1_end

        call poem

    #     ## Day 2
        $ chapter = 2
        call ch2_main
        call poemresponse_start
        call ch02_end

        call poem

    #     ## Day 3
        $ chapter = 3
        call ch3_main
        call poemresponse_start
        call ch3_end

    #    ## Day 4
        $ chapter = 4
        call ch4_main

    #     ## Day 5
        $ chapter = 5
        call ch5_main


        $ chapter = 6
        call ch6_main
        
        $ chapter = 7
        call ch7_main    
        call poem

    #   ## Day 2 - Act 2
        $ chapter = 8
        call ch8_main
        call poemresponse_start
        call ch8_end

        ## Day 3 - Act 2
        $ chapter = 9
        call ch9_main
        call poemresponse_start
        call ch9_end

    #         ## Day 4 - Act 2
        $ chapter = 10
        call ch10_main
        call ch10_end
        return
 
        call ch11_main

    #    ## Day 1 - Act 4
        $ chapter = 0
        call ch12_main
        jump credits

# This label is where the game 'ends' during Act 1.
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
