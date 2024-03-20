label ch02_main:
    $ run_input(input="scene mc_pov", output="Incorrect syntax")
    show bg closet
    with dissolve_scene_full
    show natsuki turned cross anno at t21
    show yuri turned pout om at f22
    y "...and he was {i}up in my face{/i} the whole time."
    show yuri cm at t22
    mc "Sounds like one heck of a jerk."
    show yuri anno om ce at f22
    y "He so was."
    show yuri cm at t22
    "The process of getting Yuri to open up was long and hard, but the results are worth it."
    show yuri at thide
    hide yuri
    show natsuki at thide
    hide natsuki
    pause 2.0
    scene black
    show end
    with dissolve_scene_full
    python:
        renpy.call_screen("dialog", message="That's it for the playtest, folks.", ok_action=Function(renpy.full_restart))
    return