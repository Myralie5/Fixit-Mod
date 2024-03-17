layeredimage gwynn forward: #All definitions are for her facing forward.

    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null  #crying
        attribute curi null #curious
        attribute flus null #flustered
        attribute happ null #happy
        attribute nerv null #nervous
        attribute surp null #surprised
        attribute yand null #yandere
        attribute pres null #supressed
        attribute glit null #glitch
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template!



    group pose:
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute ldown default:
            "mod_assets/Gwynn MPT/monika_forward_uniform_left_down.png"
        attribute lpoint:
            "mod_assets/Gwynn MPT/monika_forward_uniform_left_point.png"
        attribute knife:
            "mod_assets/Gwynn MPT/monika_forward_casual_left_point.png"
        



    group blush: #These are intentionally separate from mood; the idea being that these aren't consciously controlled by the character - rather, they're a result of their emotions making them blush/sweat/etc.
        attribute nobl default null #Default, no blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n
        attribute blawcry null #blushing, crying and awkward. why.  defaults for n
        attribute blcry null #blushing and crying.  defaults for n
        attribute awkry null #crying and awkward.  defaults for n



    group mouth:
        
        #Default Closed Mouths:
        attribute cm default if_any(["happ","nerv"]):
            "mod_assets/Gwynn MPT/monika_forward_mouth_ma.png"
        attribute cm default if_any(["neut"]):
            "mod_assets/Gwynn MPT/monika_forward_mouth_md.png"
        attribute cm default if_any(["sad","angr"]):
            "mod_assets/Gwynn MPT/monika_forward_mouth_md.png"
        attribute cm default if_any(["yand"]):
            "mod_assets/Gwynn MPT/monika_forward_mouth_mo.png"
        
        #Open Mouths:
        attribute om if_any(["happ"]):
            "mod_assets/Gwynn MPT/monika_forward_mouth_mb.png"
        attribute om if_any(["nerv","yand"]):
            "mod_assets/Gwynn MPT/monika_forward_mouth_mc.png"
        attribute om if_any(["neut"]):
            "mod_assets/Gwynn MPT/monika_forward_mouth_md.png"
        attribute om if_any(["sad"]):
            "mod_assets/Gwynn MPT/monika_forward_mouth_mk.png"
    


    group eyes:
        
        #Default Opened eyes:
        attribute oe default if_any(["neut","happ","sad"]):
            "mod_assets/Gwynn MPT/monika_forward_eyes_e1a.png"
        attribute oe default if_any(["angr"]):
            "mod_assets/Gwynn MPT/monika_forward_eyes_e1d.png"
        attribute oe default if_any(["nerv"]):
            "mod_assets/Gwynn MPT/monika_forward_eyes_e2b.png"
        attribute oe default if_any(["yand"]):
            "mod_assets/Gwynn MPT/monika_forward_eyes_e3a.png"
        
        #Default Closed eyes:
        attribute ce if_any(["neut","sad","angr"]):
            "mod_assets/Gwynn MPT/monika_forward_eyes_e4a.png"
        attribute ce if_any(["happ","yand","nerv"]):
            "mod_assets/Gwynn MPT/monika_forward_eyes_e4b.png"

        ###All eyes - truncated tags:
        attribute e1a:
            "mod_assets/MPT/monika/monika_forward_eyes_e1a.png"
        attribute e1b:
            "mod_assets/MPT/monika/monika_forward_eyes_e1b.png"
        attribute e1c:
            "mod_assets/MPT/monika/monika_forward_eyes_e1c.png"
        attribute e1d:
            "mod_assets/MPT/monika/monika_forward_eyes_e1d.png"
        attribute e1e:
            "mod_assets/MPT/monika/monika_forward_eyes_e1e.png"
        attribute e1f:
            "mod_assets/MPT/monika/monika_forward_eyes_e1f.png"
        attribute e1g:
            "mod_assets/MPT/monika/monika_forward_eyes_e1g.png"
        attribute e1h:
            "mod_assets/MPT/monika/monika_forward_eyes_e1h.png"
        attribute e2a:
            "mod_assets/MPT/monika/monika_forward_eyes_e2a.png"
        attribute e2b:
            "mod_assets/MPT/monika/monika_forward_eyes_e2b.png"
        attribute e2c:
            "mod_assets/MPT/monika/monika_forward_eyes_e2c.png"
        attribute e2d:
            "mod_assets/MPT/monika/monika_forward_eyes_e2d.png"
        attribute e3a:
            "mod_assets/MPT/monika/monika_forward_eyes_e3a.png"
        attribute e3b:
            "mod_assets/MPT/monika/monika_forward_eyes_e3b.png"
        attribute e4a:
            "mod_assets/MPT/monika/monika_forward_eyes_e4a.png"
        attribute e4b:
            "mod_assets/MPT/monika/monika_forward_eyes_e4b.png"
        attribute e4c:
            "mod_assets/MPT/monika/monika_forward_eyes_e4c.png"
        attribute e4d:
            "mod_assets/MPT/monika/monika_forward_eyes_e4d.png"
        attribute e4e:
            "mod_assets/MPT/monika/monika_forward_eyes_e4e.png"
        attribute e0a:
            "mod_assets/MPT/monika/monika_forward_eyes_e0a.png"
        attribute e0b:
            "mod_assets/MPT/monika/monika_forward_eyes_e0b.png"



    group nose:
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "mod_assets/Gwynn MPT/monika_forward_nose_n1.png"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "mod_assets/Gwynn MPT/monika_forward_nose_n2.png"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "mod_assets/Gwynn MPT/monika_forward_nose_n3.png"
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            "mod_assets/Gwynn MPT/monika_forward_nose_n4.png"
        attribute nose default if_any(["awkry"]):#default nose when "crying and awkward"
            "mod_assets/Gwynn MPT/monika_forward_nose_n5.png"
        attribute nose default if_any(["blcry"]):#default nose when "blushing and crying"
            "mod_assets/Gwynn MPT/monika_forward_nose_n6.png"
        attribute nose default if_any(["blawcry"]):#default nose when "blushing and awkward"
            "mod_assets/Gwynn MPT/monika_forward_nose_n7.png"



    group eyebrows:
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","yand"]):
            "mod_assets/Gwynn MPT/monika_forward_eyebrows_b1a.png"
        attribute brow default if_any(["cry","sad","nerv"]):
            "mod_assets/Gwynn MPT/monika_forward_eyebrows_b1b.png"
        attribute brow default if_any(["angr"]):
            "mod_assets/Gwynn MPT/monika_forward_eyebrows_b1e.png"
    


    group blood:

        attribute blood:
            "mod_assets/Gwynn MPT/monika_forward_casual_left_point.png"