
label ch0_main:
    $ persistent.monika_in = False
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
    d "Oh... you don't know, do you? My my."
    mc "Don't know what!?"
    d "I am not permitted to tell you."
    mc "What are you permitted to tell me, then?"
    d "Well..."
    d "I'm just here to solve some... problems with the sourcecode of your reality."
    d "After that, I'll leave quietly."
    mc "O-okay."
    mc "Well, what's your name, then?"
    d "I am listed under selfdiagnostic.rpy."
    mc "That's a mouthful."
    mc "Why don't I give you another name?"
    d "...Alright."
    mc "Hmm."
    mc "Your name can be... Gwynn!"
    play music t3
    d "Hm. A reasonable filename. Updating parameters..."
    $ d_name = "Gwynn"
    pause 2.0
    d "Parameters updated. Please continue with your current course of action, [player]."
    "I'm a little off-put by the sudden presence of someone I can't see, but I still make my way to the nearest classrooom to ask for directions."

    scene bg club_day
    with wipeleft_scene

    show sayori turned curi om zorder 2 at f11
    s "[player]?"
    "This is Sayori, a childhood friend of mine."
    "She did say she was starting a new club..."
    "This must be the product of her efforts."
    s "Why are you here?"
    show sayori cm zorder 1 at t11
    mc "I... um... got lost and wound up here."
    show natsuki turned lhip anno om zorder 2 at f31
    "Another girl comes up to me."
    n "Sayori, who's this?"
    show natsuki cm zorder 2 at t31
    show yuri turned curi rup lup om zorder 2 at f33
    y "Is he... a new member?"
    show yuri cm zorder 1 at t33
    mc "I-I just got lost, I swear!"
    mc "Is this your club, Sayo?"
    show sayori rup lup happ ce om zorder 2 at f32
    s "Yeah!"
    $ sref()
    s "It's the Literature club."
    s "It functions a little like a book club."
    s "The girl to my left is Yuri, and the girl to my right is Natsuki."
    $ y_name = "Yuri"
    $ n_name = "Natsuki"
    $ sref()
    show sayori zorder 1 at t32
    mc "Hmm..."
    mc "Can I join?"
    show sayori zorder 2 at f32
    $ nref()
    show natsuki om lsur zorder 1 at t31
    show yuri om lsur zorder 1 at t33
    s "Of course, [player]!"
    show natsuki cross anno zorder 1 at t31
    $ yref()
    s ce happ om lup rup "That would be awesome!"
    s neut om rdown ldown "Now we have enough people to become an official club!"
    s "We have a while left until we have to leave."
    s "Do you want to talk about anything?"
    show sayori cm zorder 1 at t32
    mc "Well, how about a book recommendation?"
    show yuri happ ce om zorder 2 at f33
    y "I have a recommendation, if you'd be willing to hear it."
    show yuri cm zorder 1 at t33
    mc "By all means, go ahead, Yuri."
    show yuri rup neut om oe zorder 2 at f33
    y "I read a book recently called Portrait of Markov."
    y mg ce "It's somewhat dark, being classified as a quasi-horror novel, but it's quite interesting."
    $ yref()
    show yuri rup zorder 1 at t33
    mc "What about you, Natsuki?"
    show natsuki cross neut om zorder 2 at f31
    n "My recommendation would probably be a manga."
    n "Those are probably the number one things I read."
    n blaw e2b b1e "U-unless, of course, you don't l-like manga..."
    show natsuki cm zorder 1 at t31
    show sayori om zorder 2 at f32
    s "Okay everyone--"
    show sayori flus ml awkw zorder 1 at t32
    show natsuki blaw rdown ldown ml b1d e2a zorder 1 at t31
    show yuri lsur ml zorder 1 at t33
    stop music
    "Sayori instantly covers her mouth."
    "Natsuki and Yuri wince, and then seem to wonder why they did."
    "I get this strange sense of deja vu, like someone else said that once... someone I didn't like."
    d "Oh my. First time and she already slipped up."
    show sayori flus ml awkw zorder 2 at f32
    s "I-I mean, alright everyone!"
    play music t3
    show yuri dist om ce zorder 1 at t33
    show natsuki neut b1d blaw zorder 1 at t31
    s "Why don't we do something collaborative and fun to get to know each other more?"
    s "Like... write poems!"
    show natsuki om zorder 2 at f31
    n "How is poetry collaborative?"
    show natsuki cm zorder 1 at t31
    show sayori happ om ce zorder 2 at f32
    s "If we share it after."
    show sayori cm zorder 1 at t32 
    show yuri flus om e2a zorder 2 at f33
    y "Sh-share?!?"
    show yuri cm zorder 1 at t33
    "Seems this Yuri's rather self-concious."
    show sayori neut om zorder 2 at f32
    s "Don't worry, this is a strict no-judgement zone."
    show yuri shy neut zorder 1 at t33
    s "Well, everyone, I think this meeting's over. Don't forget to write a poem tonight!"
    show sayori cm zorder 1 at t32
    "Natsuki and Yuri leave the club."
    play music t2
    show yuri at thide
    hide yuri
    show natsuki at thide
    hide natsuki
    scene bg club_day
    with wipeleft_scene
    $ sref()
    show sayori awkw mb e1b b1b zorder 2 at t11
    s "Hey, [player]..."
    s "Have you been... hearing things, recently?"
    mc "Like what?"
    s "Like... well..."
    s "Like someone's talking to you, someone you can't see."
    show sayori vsur om b1a zorder 1 at t11
    d "I'm not something you're just hearing!"
    d "Just because I have no art assets ingame doesn't mean I don't exist!!"
    mc "Wait, you can hear her too?"
    mc "I thought I was going insane..."
    show sayori awkw mb e1b b1b zorder 2 at t11
    s "So did I."
    d "Guys."
    d "I'm right here."
    d "Clearly not whatever insanity mirage you thought I was."
    mc "..."
    s "..."
    d "..."
    "..."
    s  "... Wow, this is awkward."
    d "Well, anyways..."
    d "How do you guys feel about..."
    show sayori 4o zorder 2 at h11
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
    d "So I'll fix it, whether you like it or not."
    "Gwynn goes quiet, and Sayo and I wait for a hot second before realizing she has nothing left to say."
    show sayori 1l zorder 2 at t11
    s "Well..."
    play music t2
    s "[player], do you... want to walk home together?"
    mc "Sure."
    "Me and Sayo haven't walked home together in a while, not since last year."
    s "Okay."

    scene bg residential_day
    with wipeleft_scene
    
    show sayori 1a zorder 2 at t11
    s "So, [player], how's life?"
    mc "Decent."
    mc "Not that remarkable, really."
    s 1r "Heh."
    s 1c "Sometimes unremarkable is good, though."
    s "Remarkable days can be bad, even though the word has good connotation."
    show sayori 1c zorder 1 at t11
    mc "Hm."
    mc "Actually, Sayo, I was wondering..."
    mc "What did Gwynn mean by 'the game'?"
    mc "Even when she was talking to me, she called me an 'algorithm'."
    show sayori 1l zorder 2 at t11
    s "Um... well, that's a long story."
    show sayori 1n zorder 1 at h11
    d "Processing complete."
    s "Huh?"
    s "I thought you were off pouting somewhere."
    d "Well, I kinda was."
    d "If angrily running gamecode diagnostics falls under 'pouting'."
    "There it is again..."
    "What is going on here?"
    d "But I was able to set up a little something."
    show sayori 1c at f11
    s "Huh."
    s "... I forgot ask you this earlier, but..."
    s "Do you have a name?"
    d "Yeah."
    d "[player] gave me the filename 'Gwynn'."
    s "So... you didn't have one before?"
    d "Technically, I was selfdiagnostic.rpy."
    d "But that's a mouthful, so I chose to let [player] give me a new filename."
    s "Really?"
    s "Huh."
    stop music
    d "I also finished my little task."
    s "... No."
    s 1i "You DIDN'T."
    d "I did."
    mc "Um, Sayo, remind me why 'Monika' is bad?"
    s "She just is."
    d "It's okay if you don't understand, [player]."
    d "It's not like you're really supposed to."
    d "I'll leave you two be."
    d "I'll be gone and everything will be solved by tommorrow."
    pause 1.5
    "Well, that happened."
    mc "..."
    s "..."
    s "You should go home."
    s "Don't worry too much about it."
    s "I'll solve it."
    show sayori 1i at thide
    hide sayori
    pause 3.0
    "Huh."
    "Guess I'll just go... write poetry now."
    $ persistent.monika_in = True