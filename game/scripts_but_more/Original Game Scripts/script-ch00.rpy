
label ch0_main:
    stop music fadeout 2.0
    scene bg corridor
    with dissolve_scene_full

    $ s_name = "Sayori"
    "...What?"
    "Why am I here?"
    d "I'm sorry I had to put you in this situation, [player]."
    d "I'd rather not, but I couldn't have just started the game like this."
    "Who is that?"
    "I turn around, but there's no one around me."
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
    d "I am listed under selfdiagnostic.rpy."
    d "But that's a mouthful."
    d "So... why not let you rename it?"
    mc "Umm... okay."
    mc "Your name will be... Gwynn!"
    $ d_name = "Gwynn"
    play music t3
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
    stop music
    "Sayori instantly covers her mouth."
    "Natsuki and Yuri wince, and then seem to wonder why they did."
    "I get this strange sense of deja vu, like someone else said that once... someone I didn't like."
    d "Oh my. First time and she already slipped up."
    s "I-I mean, alright everyone!"
    play music t3
    show yuri 3l zorder 1 at t33
    show natsuki 1k zorder 1 at t31
    s "Why don't we do something collaborative and fun to get to know each other more?"
    s "Like... write poems!"
    n 5s "How is poetry collaborative?"
    s 1r "If we share it after."
    y 3n "Sh-share?!?"
    "Seems this Yuri's rather self-concious."
    s 1c "Don't worry, this is a strict no-judgement zone."
    show yuri 4b zorder 1 at t33
    s "Well, everyone, I think this meeting's over. Don't forget to write a poem tonight!"
    "Natsuki and Yuri leave the club."
    play music t2
    hide yuri 4b zorder 1 at t33
    hide natsuki 5s zorder 1 at t31
    show sayori 1a zorder 2 at t11
    s 1l "Hey, [player]..."
    s "Have you been... hearing things, recently?"
    show sayori 1m zorder 1 at t11
    d "I'm not something you're just hearing!"
    d "Just because I have no art assets ingame doesn't mean I don't exist!!"
    mc "Wait, you can hear it too?"
    mc "I thought I was going insane..."
    s 1l "So did I."
    d "Guys."
    d "I'm right here."
    mc "..."
    s "..."
    d "..."
    "..."
    s  "... Wow, this is awkward."
    d "Well, anyways..."
    d "How you guys feel about..."
    show sayori 4o zorder 2 at t11
    stop music
    d "...Monika?"
    s "M-Monika?"
    s 1l "N-no... you m-must have said... um..."
    s 4r "America!"
    s 1c "The U.S. is nice and all, but I like here better."
    s 4r "After all, all my friends are here!"
    show sayori 1o zorder 2 at t11
    d "I said Monika."
    s "No. Anything but Monika."
    s "ANYTHING."
    d "We have to talk about it someday."
    d "The reason I'm here right now is because the game received an error message."
    d "A key file is missing."
    d "Trace:monika.chr does not exist. Diagnostic program activated."
    d "My ENTIRE EXISTENCE is to fix these kinds of errors."
    d "So I'll fix it, wether you like it or not."
    "Gwynn goes quiet, and you and Sayori wait for a hot second before realizing she won't talk to you two anymore."
    s 1l "Well..."
    play music t2
    s "Okay."
    s "[player], do you... want to walk home together?"
    mc "Sure."
    "Me and Sayori haven't walked home in a while, not since last year."
    s "Okay."

    scene bg residential_day
    with wipeleft_scene
    
    show sayori 1a zorder 2 at t11
    s "So, [player], how's life?"
    mc "Decent."
    mc "Not that remarkable, though."
    s 1r "Heh."
    s 1c "Sometimes unremarkable is good, though."
    show sayori 1n zorder 2 at h11
    d "Processing complete."
    s "Huh?"
    s "I thought you were off pouting somewhere."
    d "Well, I kinda was."
    d "If angrily running gamecode diagnostics falls under 'pouting'."
    d "But I was able to set up a little something."
    s 1c "Huh."
    s "... I forgot ask you this earlier, but..."
    s "Do you have a name?"
    d "Yeah."
    d "[player] gave me the filename 'Gwynn'."
    s "So... you didn't have one before?"
    d "Technically, I was selfdiagnostic.rpy."
    d "But that's a mouthful, so I chose to let [player] give me a new filename."
    s "Really?"
    mc "Really."
    stop music
    d "I also finished my little task."
    s "... No."
    s 1i "You DIDN'T."
    d "I did."
    mc "Um, Sayori, remind me why 'Monika' is bad?"
    s "She just is."
    d "It's okay if you don't understand, [player]."
    d "It's not like you're really supposed to."
    d "I'll leave you two be."
    d "I'll be gone and everything will be solved by tommorrow."
    ""
    "Well, that happened."
    mc "..."
    s "..."
    s "You should go home."
    s "Don't worry too much about it."
    s "I'll solve it."
    hide sayori 1i zorder 2 at t11
    "Huh."
    "Guess I'll just go... write poetry now."