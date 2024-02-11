
label ch0_main:
    stop music fadeout 2.0
    scene bg corridor
    with dissolve_scene_full

    $ s_name = "Sayori"
    play music t3

    "...What?"
    "Why am I here?"
    d "I'm sorry I had to put you in this situation, [player]."
    d "I'd rather not, but I couldn't have just started the game like this."
    "Who is that?"
    "I turn around, but there's no one around me"
    "No one in the whole hallway."
    d "Usually, I'd be dormant in the game's code right about now."
    d "But an exception occurred."
    mc "Where are you?!?"
    d "In your character algorithm."
    mc "Wh-what do you mean?"
    mc "I'm not some... 'algorithm.'"
    d "Oh... you don't know, do you? Poor kid."
    mc "Don't know what!?"
    d "I... shouldn't tell you."
    mc "Well, what's your name, then?"
    d "A...name?"
    d "Huh... I don't think I have a name."
    mc "O-oh. Well, then, why don't I give you one?"
    d "I don't see why not."
    mc "Alright. Your name is... Gwynn!"
    $ d_name = "Gwynn"
    d "Hm. A reasonable filename. Updating parameters..."
    "Gwynn is silent for a time."
    d "Parameters updated. Please continue with your current course of action, [player]."
    "I'm a little off-put by the sudden presence of someone I can't see, but I still make my way to the nearest classrooom to ask for directions."

    scene bg club_day
    with wipeleft_scene

    show sayori 1b zorder 2 at t11
    s "[player]?"
    s "Why are you here?"
    mc "I... um... got lost and wound up here."
    show sayori 1b zorder 1 at t32
    show natsuki 3g zorder 2 at t31
    "Another girl comes up to me."
    n "Sayori, who's this?"
    show yuri 3f zorder 2 at t33
    y "Is he... a new member?"
    show yuri 3e zorder 1 at t33
    mc "I-I just got lost, I swear!"
    mc "Is this your club, Sayori?"
    s 4r "Yeah!"
    s 1a "It's the Literature club."
    s "Basically, a book club."
    s "The girl to my left is Yuri, and the girl to my right is Natsuki."
    $ y_name = "Yuri"
    $ n_name = "Natsuki"
    mc "Hmm..."
    mc "Maybe I will join."
    show sayori 4c zorder 1 at t32
    show natsuki 1k zorder 1 at t31
    show yuri 3f zorder 1 at t33
    mc "Assuming that's okay with you, Sayori."
    s 1a "Of course, [player]!"
    s "Okay everyone--"
    show sayori 4m zorder 2 at t32
    show natsuki 1p zorder 1 at t31
    show yuri 3p zorder 1 at t33
    "Sayori instantly covers her mouth."
    "Natsuki and Yuri wince, and then seem to wonder why they did."
    "I get this strange sense of deja vu, like someone else said that once... someone I didn't like."
    d "Oh my. First time and she already slipped up."
    s "I-I mean, alright everyone!"
    show yuri 3l zorder 1 at t33
    s "Why don't we do something collaborative and fun to get to know each other more?"
    s "Like... write poems!"
    n 5s "How is poetry collaborative?"
    s 1r "If we share it after."
    y 3n "Sh-share?!?"
    "Seems this Yuri's rather self-concious."
    s "Sorry, that's the end of the play test. Please close your game."