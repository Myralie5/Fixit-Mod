
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
    pause 2.0
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
    pause 1.5
    show natsuki 1c
    pause 1.0
    show natsuki 1p
    pause 0.5
    show natsuki scream
    n "KYAAAAAAAAAAGHHH!"
    show natsuki at lhide
    hide natsuki
    show monika 1l at f31 zorder 2
    m "O-oh my."
    m 1n "It seems poor Natsuki didn't take well to my arrival."
    show monika at t31 zorder 1
    show sayori 1i at f33 zorder 2
    s "Of course she didn't."
    s 1j "You {i}ruined their lives{/i} back then."
    s "Both of them."
    show sayori 1i at t33 zorder 1
    show monika 1m at f31 zorder 2
    m "..."
    m 1p "I really did, didn't I."
    m "I probably owe all of you apologies."
    m "Especially you, [player]."
    show monika 1p at t31 zorder 1
    mc "...?"
    mc "Um, Monika..."
    show monika 1d at h31
    mc "... We've never met before today."
    show monika 1d at f31 zorder 2
    m "Wh-what?"
    m 1l "What about-"
    show sayori 1o at t21 zorder 1
    show monika 1g at t31 zorder 2
    "Sayo leans over and whispers something in Monika's ear."
    "Monika seems distraught by whatever Sayo's telling her."
    show sayori 1o at t22 zorder 1
    show monika 1g at f21 zorder 2
    m "Wait, so-"
    show monika 1g at t21 zorder 2
    show sayori 1o at f22 zorder 1
    s "Shh! Keep your voice down!"
    show sayori 1o at t22 zorder 1
    "Sayori gestures at me."
    "Monika makes an 'oh' sound, and they keep conversing in hushed tones."
    show sayori at thide
    hide sayori
    show monika at thide
    hide monika
    "They move to the closet area, where they keep talking."
    "It's at this point that Yuri arrives."
    show yuri 1d at t11 zorder 1
    play music t3
    y "Hello, [player]!"
    y 1b "How are you today?"
    mc "Good, how about you?"
    y "Doing better than ever before."
    y "Thanks for asking."
    y 1f "By the way..."
    y "Where are Sayori and Natsuki?"
    mc "Natsuki showed up here earlier, then left."
    mc "Sayo's over there, talking with a new girl."
    y 1h "A new girl, huh..."
    "Yuri looks over to the closet..."
    show yuri 1r at t11 zorder 1
    y "What..."
    y "...is"
    stop music
    y 1y7 "{i}SHE{/i}"
    play music t3
    y 1r "doing here, [player]?"
    mc "She just kinda... showed up?"
    "What did Yuri just do with her eyes?"
    "..."
    "Why did it scare me so much?"
    pause 1.0
    y 3l "Apologies, [player]."
    y 3t "I shouldn't have yelled at you, when it's her that I'm angry at."
    mc "I-it's okay..."
    y "(Argh. I bet he's scared of me now.)"
    y "(I really should work on not lashing out.)"
    mc "Well, ah, I'm gonna go look for Natsuki."
    mc "D-do you want to come?"
    y 2d "Of course, [player]."
    y 1b "Helping a friend is a valiant cause indeed."
    "Yuri just said a big word and I'm not entirely certain what it means."
    "But it sounded positive, sooo..."
    mc "Alright. Let's go, then."

    scene bg corridor
    with wipeleft_scene
    stop music

    "We find Natsuki after a while of looking."
    show natsuki 12f at t22 zorder 1
    show yuri 3t at f21 zorder 1
    y "Natsuki?"
    y "Are you alright?"
    show yuri 3t at t21 zorder 1
    show natsuki 12h at f22 zorder 2
    n "She's in there, Yuri."
    n "No matter how hard we try, we're never able to escape her."
    show yuri 3t at f21 zorder 2
    show natsuki 12h at t22 zorder 1
    y "Natsuki..."
    show yuri 3w at f21 zorder 2
    pause 1.5
    y 3r "Here's my plan."
    y "We go in and act normal today."
    y "We see if this Monika instance is a threat like the last one."
    y "If she isn't, good, continue on with your regularly sheduled life."
    y "If she is, we reconvene at lunch."
    show yuri 3r at t21 zorder 1
    pause 0.5
    show natsuki 12e at f22 zorder 2
    n "...That could work."

    show bg club_day
    with wipeleft_scene
    hide yuri
    hide natsuki

    show yuri 1a at t11 zorder 1
    y "Hey, [player]."
    "Yuri reaches into her bag and pulls out a book."
    y "I didn't want you to feel left out..."
    y "So I picked out a book that I thought you might enjoy."
    y "It's a short read, so it should keep your attention, even if you don't usually read."
    y "And we could, you know..."
    show yuri at sink
    y 4b "Discuss it...if you wanted..."
    "Th-This is..."
    "How is this girl accidentally being so cute?"
    "She even picked out a book she thinks I'll like..."
    mc "Yuri, thank you! I'll definitely read this!"
    "I enthusiastically take the book."
    show yuri 2m zorder 2 at t11
    y "Phew..."
    y 2a "Well, you can read it at your own pace."
    y "I look forward to hearing what you think."
    show yuri zorder 1 at thide
    hide yuri

    "Now that everyone's settled in, I expected Sayo to kick off some at least vaguely scheduled activities for the club."
    "But that doesn't seem to be the case."
    "Sayori and Monika are having an awkward conversation near the teacher's desk."
    "Yuri's face is already buried in a book."
    "I can't help but notice her intense expression, like she was waiting for this chance."
    "Meanwhile, Natsuki is rummaging around in the closet."


    $ nextscene = poemwinner[0] + "_exclusivex_" + [chapter]
    call expression nextscene


    show sayori 1a at t11
    s "By the way, [player], did you remember to write a poem last night?"
    mc "Y-Yeah..."
    "My relaxation ends."
    "I can't believe I agreed to do something so embarrassing."
    "I couldn't really find much inspiration, since I've never really done this before."
    s "Well, now that everyone's ready, why don't you find someone to share with?"
    show sayori 4q zorder 2 at t22
    s "I personally can't wait to see what everyone's written~!"
    show sayori zorder 1 at thide
    hide sayori
    "Sayori pulls out her poem."
    "It's on a wrinkled sheet of loose leaf torn from a spiral notebook."
    "Monika rummages around in her bag and finds a composition notebook."
    "Even though she couldn't have known we were writing poems, she still had some with her."
    "I can already see her pristine handwriting from where I sit."
    "Natsuki and Yuri reluctantly comply as well, reaching into their bags."
    "I do the same, myself."

    return

label ch01_end:
    stop music fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    play music t3
    "Well..."
    "That was one hell of an experience."
    "A few of these girls in particular are {i}terrible{/i} at making people feel welcomed."
    "I glance across the room."
    "Across the room, Sayori and Monika are somewhat awkwardly talking."
    "Good for them, at least."
    "My eyes land on Yuri and Natsuki."
    show yuri 2g zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "They gingerly exchange sheets of paper, sharing their respective poems."
    show yuri 2i at t21
    "As they read in tandem, I watch each of their expressions change."
    "Natsuki's eyebrows furrow in frustration."
    "Meanwhile, Yuri smiles sadly."
    show natsuki zorder 3 at f22
    n 1q "{i}(What's with this language...?){/i}"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2f "Eh?"
    y "Um...did you say something?"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2c "Oh, it's nothing."
    "Natsuki dismissively returns the poem to the desk with one hand."
    n "I guess you could say it's fancy."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2i "Ah-- Thanks..."
    y "Yours is...cute..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2h "Cute?"
    n 1h "Did you completely miss the symbolism or something?"
    n "It's clearly about the feeling of giving up."
    n "How can that be cute?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3f "I-I know that!"
    y "I just meant..."
    y 3h "The language, I guess..."
    y "I was trying to say something nice..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n "Eh?"
    n 4w "You mean you have to try that hard to come up with something nice to say?"
    n "Thanks, but it really didn't come out nice at all!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1i "Agh, sorry..."
    y "Well, I do have a couple suggestions..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 5x "Hmph."
    n "If I was looking for suggestions, I would have asked someone who actually liked it."
    n "Which people {i}did{/i}, by the way."
    n 5e "Sayori liked it."
    n "And [player] did, too!"
    n "So based on that, I'll gladly give you some suggestions of my own."
    n "First of all--"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2l "Excuse me..."
    y "I appreciate the offer, but I've spent a long time establishing my writing style."
    y 2h "I don't expect it to change anytime soon, unless of course I come across something particularly inspiring."
    y "Which I haven't yet."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Nn...!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1k "And [player] liked my poem too, you know."
    y "He even told me he was impressed by it."
    stop music fadeout 1.0
    "Natsuki suddenly stands up."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4y "Oh?"
    n "I didn't realize you were so invested in trying to impress our new member, Yuri."
    play music t7
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1n "E-Eh?!"
    y "That's not what I...!"
    y 1o "Uu..."
    y "You...You're just..."
    "Yuri stands up as well."
    y 2r "Maybe you're just jealous that [player] appreciates my advice more than he appreciated yours!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "Huh! And how do you know he didn't appreciate {i}my{/i} advice more?"
    n "Are you that full of yourself?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3h "I...!"
    y "No..."
    y "If I was full of myself..."
    y 1r "...I would deliberately go out of my way to make everything I do overly cutesy!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Uuuuuu...!"
    show sayori 2l behind yuri, natsuki at l41
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    s "U-Um!!"
    s "Is everyone okay...?"
    show sayori 2 at lhide
    hide sayori
    show natsuki zorder 3 at f33
    n 1f "Well, you know what?!"
    n "I wasn't the one whose boobs magically grew a size bigger as soon as [player] started showing up!!"
    show yuri 3p at h32
    show natsuki zorder 2 at t33
    y "N-Natsuki!!"
    show monika 3l behind yuri, natsuki at l41
    m "Um, Natsuki, that's a little--"
    show monika at h41
    show yuri 3p zorder 3 at f32
    show natsuki 1e zorder 3 at f33
    ny "This doesn't involve you!"
    show monika at lhide
    hide monika
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    show sayori 4p behind yuri, natsuki at l41
    s "I-I don't like fighting, guys...!"
    show sayori at lhide
    hide sayori
    show yuri zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "Suddenly, both girls turn towards me, as if they just noticed I was standing there."
    show yuri zorder 3 at f21
    y 2n "[player]...!"
    y "She-- She's just trying to make me look bad...!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4w "That's not true!"
    n "She started it!"
    n 4e "If she could get over herself and learn to appreciate that {i}simple{/i} writing is more effective..."
    n "Then this wouldn't have happened in the first place!"
    n "What's the point in making your poems all convoluted for no reason?"
    n "The meaning should jump out at the reader, not force them to have to figure it out."
    n 1f "Help me explain that to her, [player]!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3o "W-Wait!"
    y "There's a reason we have so many deep and expressive words in our language!"
    y 3w "It's the only way to convey complex feelings and meaning the most effectively."
    y "Avoiding them is not only unnecessarily limiting yourself...it's also a waste!"
    y 1t "You understand that, right, [player]?"
    show yuri zorder 2 at t21
    mc "Um...!"
    show yuri 1t zorder 3 at f21
    show natsuki 1e zorder 3 at f22
    ny "Well??"
    mc "..."
    show yuri zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "How did I get dragged into this in the first place?!"
    "It's not like I know anything about writing..."
    "But whomever I agree with, they'll probably think more highly of me!"
    menu:
        "So, of course that's going to be...!"
        "Natsuki.":
            call ch01_end_natsuki
        "Yuri.":
            call ch01_end_yuri
        "Help me, Sayori!!":
            call ch01_end_sayori

    show sayori 1a at t11 zorder 2
    s "Well, now that we're past that..."
    s 4b "Everyone's read each other's poems, right?"
    s "I hope that it was worthwhile for everyone!"
    s "Especially you, [player]!"
    s "And to be honest..."
    s "It's a nice change of pace from the lazing around we got a little too used to."
    s "Hehe~"
    mc "Ah, so my joining the club was responsible for ruining the atmosphere..."
    s 1c "No, not at all!"
    s "There's still time before we go home."
    s 1a "So we'll all relax for a bit."
    s "And remember..."
    s "The most important thing about this club..."
    show sayori 4r zorder 2 at h11
    s "Is having fun!"
    show sayori at thide
    hide sayori
    "I still feel a little bit judged."
    "But in the end..."
    "...I guess it's been worth it so far."
    "As I'm thinking, Sayo comes up to me."
    show sayori 1a at t11 zorder 2
    mc "Oh. Hey, Sayo."
    s 1g "You sound... down. Is everything alright?"
    show sayori 4m at t11
    d "I wouldn't worry too much."
    d "Either of you."
    s "G-Gwynn?"
    s "I thought with Monika back, you were done your job..."
    d "So did I."
    d "But it appears there are other errors to remedy."
    "Gwynn keeps talking about 'errors' and 'gamecode'."
    "Something is going on here."
    s 1j "We should leave [player] out of this."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            d "But he's incredibly important to any matters regarding [currentuser]."
            "Who's [currentuser]?"
            d "And this definitely involves them."
        else:
            s "You just need to talk to 'them', don't you?"
            "Who's 'them'?"
            d "Well, this definitely involves them."
    else:
        s "You just need to talk to 'them', don't you?"
        "Who's 'them'?"
        d "Well, this definitely involves them."
    d "And that's neither my problem nor yours."

label ch01_end_natsuki:
    $ ch1_choice = "natsuki"
    stop music fadeout 1.0
    mc "Um..."
    mc "Yuri!"
    mc "You're really talented."
    show yuri 4a at s21
    y "Eh? W-Well..."
    play music t8
    mc "But Natsuki has a point!"
    mc "I think that..."
    show yuri zorder 2 at t21
    "I wrack my brain in an attempt to back myself up."
    mc "I think that conveying feelings with few words..."
    mc "Can be just as impressive as well!"
    mc "It lets the reader's imagination take over."
    mc "And Natsuki's poem did a really good job at that!"
    show natsuki zorder 3 at f22
    n 5y "...Yeah!!"
    n "It did, didn't it?!"
    n "Ahah!"
    n "Shows how much {i}you{/i} know!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 4b "T-That's not..."
    show yuri zorder 2 at t21
    mc "Natsuki..."
    mc "I think that's enough."
    show natsuki zorder 3 at f22
    n 1m "Huh?"
    n "Me?"
    n "But she was so mean to me...!"
    "Natsuki whines."
    show natsuki zorder 2 at t22
    mc "Look..."
    mc "What we talked about yesterday was right."
    mc "Writing is a really personal thing."
    mc "And sharing it can definitely be hard."
    mc "It looks like we learned that today."
    mc "Even small criticism can lead to something pretty heated."
    "I glance over my shoulder."
    "Sayori is nodding vigorously."
    mc "Yeah, so..."
    mc "You don't need to feel threatened."
    mc "You're a great writer, Natsuki."
    show natsuki zorder 3 at f22
    n 1h "Ah--"
    "Natsuki's voice gets caught in surprise."
    n 1q "...Thanks for noticing."
    "She finally mutters that, barely audible."
    show natsuki zorder 2 at t22
    mc "Yuri..."
    show yuri zorder 3 at f21
    y 4a "...?"
    "Yuri looks at me dejectedly."
    "With a face like that, I can't help but feel bad for her as well."
    show yuri zorder 2 at t21
    mc "I'm sure that Natsuki didn't mean everything she said."
    mc "So you don't need to feel threatened, either."
    show yuri zorder 3 at f21
    y 2v "Well..."
    y "If you say so..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1g "Hey...!"
    n "It's not like you need to apologize {i}for{/i} me, [player]."
    n 1w "Sheesh."
    "Natsuki takes a breath."
    n 1q "I..."
    n "The thing about..."
    n "Uu..."
    "Natsuki glances around the room."
    show natsuki zorder 3 at hf22
    n 1x "{i}Would everyone stop staring at me??{/i}"
    "Unsurprisingly, Natsuki has a harder time with it than she boasted."
    "Sayori and Monika look away."
    show natsuki zorder 3 at f22
    n 1i "Hmph."
    n "Anyway...!"
    n 1q "The thing about your boobs. I didn't mean it, okay?"
    n "That's all."
    "Natsuki looks away, avoiding eye contact with anyone."
    show natsuki zorder 2 at t22
    show sayori 4x behind yuri at l41
    s "Yeah! You're naturally beautiful, Yuri!!"
    mc "Sayori?!"
    show yuri 4c zorder 3 at f21
    y "..."
    y "I-I'll go make some tea..."
    show yuri at lhide
    hide yuri
    show sayori zorder 3 at f41
    s 4h "Ehh?"
    s "I was just trying to help!"
    show sayori zorder 2 at t41
    mc "I'm sure she appreciated it, Sayori."
    "I pat Sayori on the shoulder."
    show natsuki zorder 1 at thide
    show sayori 4l zorder 2 at t11
    hide natsuki
    return

label ch01_end_yuri:
    $ ch1_choice = "yuri"
    stop music fadeout 1.0
    mc "Natsuki."
    mc "You're right that I liked your poem."
    show natsuki zorder 3 at f22
    n 1e "See??"
    show natsuki 1g zorder 2 at t22
    play music t8
    mc "Wait!"
    mc "That's not an excuse for you to be so mean!"
    mc "You shouldn't pick a fight just because someone's opinion is different."
    show natsuki zorder 3 at f22
    n 1m "That's not what happened at all!"
    n "Yuri wouldn't even take my poem seriously!"
    show natsuki zorder 2 at t22
    mc "Mm..."
    mc "I understand."
    mc "Yuri."
    show yuri zorder 3 at f21
    y 2t "Eh?"
    show yuri zorder 2 at t21
    mc "You're a seriously talented writer."
    mc "It's no secret that I was impressed."
    show yuri zorder 3 at f21
    y 2u "W-Well, that's..."
    show yuri zorder 2 at t21
    mc "But here's the thing."
    mc "No matter how simple or refined someone's writing style is..."
    mc "They're still putting feelings into it, and it becomes something really personal."
    mc "That's why Natsuki felt threatened when you said her poem was cute."
    show yuri zorder 3 at f21
    y 2v "I...see..."
    y "I didn't notice that I..."
    show yuri zorder 2 at t21
    y 2w "I-I'm sorry..."
    show yuri at s21
    y "Uuu..."
    show natsuki zorder 2 at t11
    show yuri zorder 1 at thide
    hide yuri
    mc "But Natsuki, you took it way too far!"
    mc "Yuri means well, and if you just told her how you felt..."
    mc "Then this wouldn't have happened in the first place."
    n 1e "Are you kidding?"
    n "That's exactly what I did!"
    n "It was {i}her{/i} that--"
    show natsuki zorder 2 at t22
    show monika 2i zorder 3 at f21
    m "Natsuki, I think that's enough."
    m "You both said some things that you didn't mean."
    m "Yuri apologized. Don't you think you should, too?"
    show monika zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1x "Nnn...!"
    show natsuki zorder 2 at t22
    "Natsuki clenches her fists."
    "In the end, nobody has taken her side."
    "She's trapped, at this point being defiant only because she can't handle the pressure."
    "I end up even feeling bad for her."
    show monika zorder 2 at t32
    show natsuki zorder 2 at t33
    show sayori 2h at l41
    s "U-Um!"
    s "Sometimes when I'm hurt..."
    s "It helps to take a walk and clear my head!"
    show sayori zorder 2 at t41
    mc "Sayori, she doesn't need to--"
    show natsuki zorder 3 at f33
    n 2q "You know what?"
    n "I'm going to do that."
    n 2w "It'll spare me from having to look at all your faces right now."
    show natsuki zorder 1 at thide
    hide natsuki
    "Without warning, Natsuki snatches her own poem up from the desk and storms out."
    "On her way out, she crumples up the poem with her hands and throws it in the trash."
    show sayori zorder 3 at f41
    s 1k "Natsuki..."
    show sayori zorder 2 at t41
    show monika zorder 3 at f32
    m 1r "She really didn't need to do that..."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide monika
    "I look across the room."
    "Yuri has her chin buried in her hands while she stares down at her desk."
    "I gingerly approach her and sit in an adjacent chair."
    show yuri 4b zorder 2 at t11
    y "Sigh..."
    mc "Everything alright?"
    y "I'm so embarrassed..."
    y "I can't believe I acted like that."
    y "You probably hate me now..."
    mc "No--Yuri!"
    mc "How could anyone not have gotten frustrated after being treated like that?"
    mc "You handled it as well as anyone could."
    mc "I don't think any less of you."
    y 2v "Well..."
    y "...Alright, I believe you."
    y 2s "Thanks, [player]. You're too kind."
    y "I'm thankful to have you a part of this club now."
    mc "Er-- It's nothing."
    y 2v "One more thing..."
    y "Um, that one thing that Natsuki said..."
    y 4c "About...you know..."
    y "I would never do anything...so shameful..."
    y "So..."
    mc "...Eh?"
    mc "What thing did Natsuki say?"
    y 3n "--!"
    y "U-Um!"
    y 3q "Well, never mind that..."
    y "I-I'm going to go make some tea..."
    mc "Ah, good idea."
    mc "Make enough for more than one person, okay?"
    y "Y-Yeah."
    return

label ch01_end_sayori:
    $ ch1_choice = "sayori"
    mc "N-Natsuki..."
    show natsuki 5f
    "Natsuki glares at me, drying up any words I had in my mouth."
    "So instead, I turn to Yuri."
    mc "Yuri..."
    y 4a "..."
    "But Yuri's expression is so defenseless that I can't bring myself to say anything to her."
    stop music fadeout 1.0
    mc "..."
    mc "...Sayori!"
    show sayori 4m behind yuri at l31
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    s "Eh?!"
    mc "...Yeah!"
    mc "Everyone's fighting is making Sayori uncomfortable."
    mc "How can the two of you keep fighting when you know you're making your friend feel like this?"
    show sayori zorder 3 at f31
    s 4d "[player]..."
    show sayori zorder 2 at t31
    show natsuki 4w zorder 3 at f33
    n "Well... That's her problem! This isn't about her."
    show natsuki zorder 2 at t33
    show yuri 2g zorder 3 at f32
    y "I-I agree..."
    y "It's unfair for others to interject their own feelings into our conflict."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 4c "Yeah, unless Sayori wants to tell Yuri what a stuck-up jerk she's being."
    show natsuki zorder 2 at t33
    show yuri 3r zorder 3 at f32
    play music t7
    y "She would never...!"
    y "It's your immaturity that's made her upset in the first place!"
    show yuri zorder 2 at t32
    show natsuki 1e zorder 3 at f33
    n "{i}Excuse{/i} me?"
    n "Are you listening to yourself?"
    n 1x "This is exactly why..."
    n 1w "Exactly why nobody likes--"
    show natsuki zorder 2 at t33
    show sayori 4p at h31
    stop music
    s "{i}Stop!!{/i}"
    show yuri 3f zorder 3 at f32
    show natsuki 1o zorder 3 at f33
    ny "--"
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    show sayori zorder 3 at f31
    play music t8
    s 1h "Natsuki! Yuri!"
    s "You guys are my friends!"
    s 1v "I-I just want everyone to get along and be happy!"
    s "My friends are wonderful people..."
    s "And I love them because of their differences!"
    s 1g "Natsuki's poems..."
    s "They're amazing because they give you so many feelings with just a few words!"
    s "And Yuri's poems are amazing because they paint beautiful pictures in your head!"
    s 4k "Everyone's so talented..."
    s "...So why are we fighting...?"
    show sayori zorder 2 at t31
    show natsuki zorder 3 at f33
    n 1r "Be-Because..."
    show natsuki zorder 2 at t33
    show yuri 3v zorder 3 at f32
    y "Well..."
    show yuri zorder 2 at t32
    show sayori zorder 3 at f31
    s 1j "Also!"
    s "Natsuki's cute and there's nothing wrong with that!"
    s 1i "And Yuri's boobs are the same as they always were!"
    show sayori at hf31
    s 1j "Big and beautiful!!"
    show sayori 1i zorder 2 at t31
    show natsuki zorder 3 at f33
    n 1o "..."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3n "..."
    show yuri zorder 2 at t32
    mc "Sayori..."
    "Sayori stands triumphantly."
    "Monika stands behind her with a bewildered expression."
    show yuri at s32
    y 3q "I'll...make some tea..."
    show yuri behind sayori at lhide
    hide yuri
    "Yuri rushes off."
    show natsuki zorder 1 at thide
    hide natsuki
    "Natsuki sits down with a blank expression on her face, staring at nothing."
    return