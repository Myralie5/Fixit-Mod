label ch02_main:
    $ run_input(input="scene mc_pov", output="Incorrect syntax")
    hide screen console_screen
    show bg closet
    with dissolve_scene_full
    show natsuki cross anno at t21
    show yuri turned pout om at f22
    y "...and he was {i}up in my face{/i} the whole time."
    show yuri cm at t22
    mc "Sounds like one heck of a jerk."
    show yuri anno om ce at f22
    y "He so was."
    show yuri cm at t22
    "The process of getting Yuri to open up was long and hard, but the results are worth it."
    "But before anything else can happen, I hear Sayo call out."
    s "Sorry to burst the bubble over there, but we have to leave the room soon!"
    show yuri dist om at f22
    show natsuki flus at t21
    y "Shame. We were having so much fun..."
    show yuri at thide
    hide yuri
    show natsuki at thide
    hide natsuki
    show bg club_day
    with wipeleft_scene
    "I wave goodbye and grab my stuff to head home."
    show bg corridor
    with wipeleft_scene
    pause 0.5
    show bg residential_day
    with wipeleft_scene
    pause 0.5
    show bg bedroom
    "Should I write a poem again tonight?"
    "Sayo didn't say if it was just once or continuing..."
    "Maybe I should call her."
    menu:
        ""
        "Call her.":
            call ch02_call_sayo
        "Just write one.":
            call poemjumper
        "Don't write one.":
            $ poem02 = False
            call nopoem02
    call newday02
    return

label ch02_call_sayo:
    "I'll call Sayo."
    "I pull out my phone and dial her."
    "ring ring ri-{nw}"
    s "[player]?"
    mc "Hey..."
    mc "I was wondering if we're supposed to write a poem tonight."
    s "Oh, I totally forgot to tell everyone!!!"
    s "Yeah, we are."
    s "I should call the others..."
    mc "I'll leave you to it."
    s "Bye!"
    mc "Bye."
    "click"
    "Okay."
    "Good to know."
    call poemjumper
    return

label poemjumper:
    $ poem02 = True
    call poem
    return

label nopoem02:
    "Nah."
    "If she didn't say anything, we probably aren't."
    "I'll just go to bed."
    scene black
    with dissolve_scene_full
    pause 3.0
    return

label newday02:
    pause 2.0
    scene black
    show end
    with dissolve_scene_full
    python:
        renpy.call_screen("dialog", message="That's it for the playtest, folks.", ok_action=Function(renpy.full_restart))