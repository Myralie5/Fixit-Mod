
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
    "end plaaytest"

label ch01_end: