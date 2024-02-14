
label ch01_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

    "It's a new day."
    "Gwynn hasn't said anything, so I assume she's made good on her promise."
    "So here I am, waiting outside Sayori's house for her to get up."
    "It's almost getting to the point where I might go in and wake her myself."
    "But, speak of the devil, here she comes."
    show sayori 2r zorder 1 at t11
    s "Hey, [player]!"
    mc "Hey, Sayori."
    mc "You're actually up on time for once."
    s 5c "Heyy!"
    s 5d "I get up on time normally..."
    pause 1.0
    mc "... Sayori."
    s 5c "... Yeah?"
    mc "Are we talking about the same person?"
    s 4p "HEY!!!"
    s "MEANIE!!!"
    pause 2.0
    s 1r "I'm glad we've gone back to doing this, [player]."
    mc "Yeah."
    mc "Me too."
    show sayori 1o at h11
    "All of a sudden, we hear someone singing some kind of love song not too far away from us."
    m "Everyday, I dream of a future where I can be with you..."
    mc "Huh?"
    mc "Who's that?"
    s 1i "We should get to school, [player]."
    mc "Wha-"
    "Sayori pulls me in the direction of the school."
    "I play along, and soon we're at school."

    scene bg class_day
    with wipeleft_scene
    play music t3

    "I've been waiting all day for the end of school so I can go and hang out with the Literature Club girls."
    "But before I can, a girl I haven't seen before stops me in class."
    show monika 5a zorder 1 at t11
    m "Hey, [player]!"
    m "Do you know the way to the Literature Club?"
    "I have a bad feeling about this girl."
    "Somehow, I feel like I remember her from somewhere."
    "But my brain keeps telling me not to trust her."
    mc "Y-yeah."
    mc "I'm part of it, actually."
    mc "Do you want me to show you the way?"
    m "Sure, [player]."
    "I turn to the exit, then almost immediately turn back to this girl."
    mc "Wait."
    mc "How do you know my name?"
    stop music
    $ timeleft = 12.453 - get_pos()
    show noise zorder 3 at noisefade(25 + timeleft)
    show vignette as flicker zorder 4 at vignetteflicker(timeleft)
    show vignette zorder 4 at vignettefade(timeleft)
    show layer master at layerflicker(timeleft)
    m 5b "Don't worry about it."
    m "We were going to the Literature Club, remember?"

    scene bg club_day
    with wipeleft_scene
    show monika 1i at t31 zorder 1
    show sayori 1i at f33 zorder 2
    pause 1.0
    s "...Monika, you're not welcome here."
    s "You know that {i}full well{/i}."
    show sayori 1i at t33 zorder 1
    "Ohh."
    "{i}This{/i} is Monika."
    $ m_name = "Monika"
    show monika 1i at f31 zorder 2
    m "Not welcome in my own club?"
    m "Oh, how far you've fallen, Sayori."
    show monika 1i at t31 zorder 1
    show sayori 4i at f33 zorder 2
    s "Hey, sail your own boat."
    s "Since you left, I've been club president."
    s "So, no, it's not 'your club' anymore, {i}Monika{/i}."
    show sayori 1i at t33 zorder 1
    "Sayo says Monika's name with such vehemence, you'd think Monika killed her puppy."
    "They must have a history."
    show monika 1i at f31 zorder 2
    m "Oh, right."
    m "You were my VP before."
    m "So why-"
    show sayori 1m at t33 zorder 1
    show monika 1d at t31 zorder 1
    show natsuki 1z at f32 zorder 2
    n "Hey Say-"
    show natsuki 1l at f32 zorder 2
    pause 1.0
    show natsuki 1c
    pause 0.5
    show natsuki 1p
    pause 0.5
    show natsuki scream
    n "KYAAAAAAAAAAGHHH!"
    "end"

    

label ch01_end: