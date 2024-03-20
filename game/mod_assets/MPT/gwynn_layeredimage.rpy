layeredimage gwynn forward: #All definitions are for her facing forward.
    at Flatten

    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute sad null #sad
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
            "mod_assets/MPT/gwynn/pose/gwynn_ldown.png"
        attribute lpoint:
            "mod_assets/MPT/gwynn/pose/gwynn_lpoint.png"
        attribute knife:
            "mod_assets/MPT/gwynn/pose/gwynn_knife.png"
        



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
        attribute cm default if_any(["happ","pres"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_ma.png"
        attribute cm default if_any(["neut","glit"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_md.png"
        attribute cm default if_any(["angr","flus"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_md.png"
        attribute cm default if_any(["yand","nerv"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_mo.png"
        
        #Open Mouths:
        attribute om if_any(["happ"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_mb.png"
        attribute om if_any(["nerv","yand"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_mc.png"
        attribute om if_any(["neut"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_md.png"
        attribute om if_any(["sad"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_mk.png"

        ###All mouths - truncated tags:
        attribute ma:
            "mod_assets/MPT/gwynn/mouths/gwynn_ma.png"
        attribute mb:
            "mod_assets/MPT/gwynn/mouths/gwynn_mb.png"
        attribute mc:
            "mod_assets/MPT/gwynn/mouths/gwynn_mc.png"
        attribute md:
            "mod_assets/MPT/gwynn/mouths/gwynn_md.png"
        attribute me:
            "mod_assets/MPT/gwynn/mouths/gwynn_me.png"
        attribute mf:
            "mod_assets/MPT/gwynn/mouths/gwynn_mf.png"
        attribute mg:
            "mod_assets/MPT/gwynn/mouths/gwynn_mg.png"
        attribute mh:
            "mod_assets/MPT/gwynn/mouths/gwynn_mh.png"
        attribute mi:
            "mod_assets/MPT/gwynn/mouths/gwynn_mi.png"
        attribute mj:
            "mod_assets/MPT/gwynn/mouths/gwynn_mj.png"
        attribute mk:
            "mod_assets/MPT/gwynn/mouths/gwynn_mk.png"
        attribute ml:
            "mod_assets/MPT/gwynn/mouths/gwynn_ml.png"
        attribute mm:
            "mod_assets/MPT/gwynn/mouths/gwynn_mm.png"
        attribute mn:
            "mod_assets/MPT/gwynn/mouths/gwynn_mn.png"
        attribute mo:
            "mod_assets/MPT/gwynn/mouths/gwynn_mo.png"
        attribute mp:
            "mod_assets/MPT/gwynn/mouths/gwynn_mp.png"
        attribute mq:
            "mod_assets/MPT/gwynn/mouths/gwynn_mq.png"
        attribute mr:
            "mod_assets/MPT/gwynn/mouths/gwynn_mr.png"
    


    group eyes:
        
        #Default Opened eyes:
        attribute oe default if_any(["neut","happ","sad"]):
            "mod_assets/MPT/gwynn/eyes/gwynn_e1a.png"
        attribute oe default if_any(["angr"]):
            "mod_assets/MPT/gwynn/eyes/gwyyn_e1d.png"
        attribute oe default if_any(["nerv"]):
            "mod_assets/MPT/gwynn/eyes/gwynn_e2b.png"
        attribute oe default if_any(["yand"]):
            "mod_assets/MPT/gwynn/eyes/gwynn_e3a.png"
        
        #Default Closed eyes:
        attribute ce if_any(["neut","sad","angr"]):
            "mod_assets/MPT/gwynn/eyes/gwynn_e4a.png"
        attribute ce if_any(["happ","yand","nerv"]):
            "mod_assets/MPT/gwynn/eyes/gwynn_e4b.png"

        ###All eyes - truncated tags:
        attribute e1a:
            "mod_assets/MPT/gwynn/eyes/gwynn_e1a.png"
        attribute e1b:
            "mod_assets/MPT/gwynn/eyes/gwynn_e1b.png"
        attribute e1c:
            "mod_assets/MPT/gwynn/eyes/gwynn_e1c.png"
        attribute e1d:
            "mod_assets/MPT/gwynn/eyes/gwynn_e1d.png"
        attribute e1e:
            "mod_assets/MPT/gwynn/eyes/gwynn_e1e.png"
        attribute e1f:
            "mod_assets/MPT/gwynn/eyes/gwynn_e1f.png"
        attribute e1g:
            "mod_assets/MPT/gwynn/eyes/gwynn_e1g.png"
        attribute e1h:
            "mod_assets/MPT/gwynn/eyes/gwynn_e1h.png"
        attribute e2a:
            "mod_assets/MPT/gwynn/eyes/gwynn_e2a.png"
        attribute e2b:
            "mod_assets/MPT/gwynn/eyes/gwynn_e2b.png"
        attribute e2c:
            "mod_assets/MPT/gwynn/eyes/gwynn_e2c.png"
        attribute e2d:
            "mod_assets/MPT/gwynn/eyes/gwynn_e2d.png"
        attribute e3a:
            "mod_assets/MPT/gwynn/eyes/gwynn_e3a.png"
        attribute e3b:
            "mod_assets/MPT/gwynn/eyes/gwynn_e3b.png"
        attribute e4a:
            "mod_assets/MPT/gwynn/eyes/gwynn_e4a.png"
        attribute e4b:
            "mod_assets/MPT/gwynn/eyes/gwynn_e4b.png"
        attribute e4c:
            "mod_assets/MPT/gwynn/eyes/gwynn_e4c.png"
        attribute e4d:
            "mod_assets/MPT/gwynn/eyes/gwynn_e4d.png"
        attribute e4e:
            "mod_assets/MPT/gwynn/eyes/gwynn_e4e.png"
        attribute e0a:
            "mod_assets/MPT/gwynn/eyes/gwynn_e0a.png"
        attribute e0b:
            "mod_assets/MPT/gwynn/eyes/gwynn_e0b.png"



    group nose:
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "mod_assets/MPT/gwynn/noses/gwynn_n1.png"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "mod_assets/MPT/gwynn/noses/gwynn_n2.png"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "mod_assets/MPT/gwynn/noses/gwynn_n3.png"
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            "mod_assets/MPT/gwynn/noses/gwynn_n4.png"
        attribute nose default if_any(["awkry"]):#default nose when "crying and awkward"
            "mod_assets/MPT/gwynn/noses/gwynn_n5.png"
        attribute nose default if_any(["blcry"]):#default nose when "blushing and crying"
            "mod_assets/MPT/gwynn/noses/gwynn_n6.png"
        attribute nose default if_any(["blawcry"]):#default nose when "blushing and awkward and crying"
            "mod_assets/MPT/gwynn/noses/gwynn_n7.png"

        #All noses - truncated tags:
        attribute n1:
            "mod_assets/MPT/gwynn/noses/gwynn_n1.png"
        attribute n2:
            "mod_assets/MPT/gwynn/noses/gwynn_n2.png"
        attribute n3:
            "mod_assets/MPT/gwynn/noses/gwynn_n3.png"
        attribute n4:
            "mod_assets/MPT/gwynn/noses/gwynn_n4.png"
        attribute n5:
            "mod_assets/MPT/gwynn/noses/gwynn_n2.png"
        attribute n6:
            "mod_assets/MPT/gwynn/noses/gwynn_n3.png"
        attribute n7:
            "mod_assets/MPT/gwynn/noses/gwynn_n4.png"



    group eyebrows:
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","yand"]):
            "mod_assets/MPT/gwynn/eyebrows/gwynn_b1a.png"
        attribute brow default if_any(["cry","sad","nerv"]):
            "mod_assets/MPT/gwynn/eyebrows/gwynn_b1b.png"
        attribute brow default if_any(["angr"]):
            "mod_assets/MPT/gwynn/eyebrows/gwynn_b1e.png"
    
        #All eyebrows - truncated tags:
        attribute b1a:
            "mod_assets/MPT/gwynn/eyebrows/gwynn_b1a.png"
        attribute b1b:
            "mod_assets/MPT/gwynn/eyebrows/gwynn_b1b.png"
        attribute b1c:
            "mod_assets/MPT/gwynn/eyebrows/gwynn_b1c.png"
        attribute b1d:
            "mod_assets/MPT/gwynn/eyebrows/gwynn_b1d.png"
        attribute b1e:
            "mod_assets/MPT/gwynn/eyebrows/gwynn_b1e.png"
        attribute b1f:
            "mod_assets/MPT/gwynn/eyebrows/gwynn_b1f.png"
        attribute b2a:
            "mod_assets/MPT/gwynn/eyebrows/gwynn_b2a.png"
        attribute b2b:
            "mod_assets/MPT/gwynn/eyebrows/gwynn_b2b.png"
        attribute b2c:
            "mod_assets/MPT/gwynn/eyebrows/gwynn_b2c.png"


    group blood:

        attribute blood:
            "mod_assets/MPT/gwynn/casual_left_point.png"