## script.rpy

# This is the main script that Ren'Py calls upon to start
# your mod's story! 

#Notable calls (use as 'call <the command>')
#   -poemresponse_start: poem sharing minigame
#   -poem: poem minigame

#Notable variables (use as '$ <the variable>= <value>' to set, 'if <the variable> == <value>' to check)


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
    $ n_name = "Girl 1"
    $ k_name = "Girl 2"
    $ l_name = "Girl 3"

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
        $ chapter = 0

        call ch0_main

        call poem

    #     ## Day 1
        $ chapter = 1
        call ch01_main

        call poemresponse_start

        call ch01_end

        call poem

        $ d_name = "Girl 4"

    #     ## Day 2
        $ chapter = 2
        call ch02_main

    #     ## Day 3
        $ chapter = 3
        call ch03_main

    #    ## Day 4
        $ chapter = 4
        call ch04_main

    #     ## Day 5
        $ chapter = 5
        call ch05_main


        $ chapter = 6
        call ch06_main
        
        $ chapter = 7
        call ch07_main

    #   ## Day 2 - Act 2
        $ chapter = 8
        call ch08_main

        ## Day 3 - Act 2
        $ chapter = 9
        call ch09_main

    #   ## Day 4 - Act 2
        $ chapter = 10
        call ch10_main
 
        call ch11_main

    #    ## Day 1 - Act 4
        $ chapter = 0
        call ch12_main
        jump modcredits


label modcredits:
    pause 1.0
    if unfinished == True:
        call authorchan
    else:
        scene black
        show end
        with dissolve_scene_full
        pause 1.0
        python:
            renpy.call_screen("dialog", message="That's it for the playtest, folks.", ok_action=Function(renpy.full_restart))    


# This label is where the game 'ends' during Act 1.
#label endgame(pause_length=4.0):
    #$ quick_menu = False
    #stop music fadeout 2.0
    #scene black
    #show end
    #with dissolve_scene_full
    #pause pause_length
    #$ quick_menu = True
    #return
