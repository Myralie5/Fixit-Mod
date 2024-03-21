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
        attribute cry null #crying. defaults for n
        attribute smcry null #ce2 cry



    group mouth:
        
        #Default Closed Mouths:
        attribute cm default if_any(["happ","pres"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_happcm.png"
        attribute cm default if_any(["neut","glit","curi","surp"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_neutcm.png"
        attribute cm default if_any(["angr","flus","anno"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_angrcm.png"
        attribute cm default if_any(["yand","nerv"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_nervcm.png"
        attribute om if_any(["sad"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_sadcm.png"
        
        #Open Mouths:
        attribute om if_any(["happ","pres"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_happom.png"
        attribute om if_any(["nerv"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_nervom.png"
        attribute om if_any(["neut","glit","curi"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_neutom.png"
        attribute om if_any(["angr","anno","flus","sad"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_angrom.png"
        attribute om if_any(["yand"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_yandom.png"
        attribute om if_any(["surp"]):
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_surpom.png"

        ###All mouths - truncated tags:
        attribute ma:
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_angrom.png"
        attribute mb:
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_angrcm.png"
        attribute mc:
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_happom.png"
        attribute md:
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_happcm.png"
        attribute me:
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_happ2om.png"
        attribute mf:
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_happ2cm.png"
        attribute mg:
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_nervom.png"
        attribute mh:
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_nervcm.png"
        attribute mi:
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_neutom.png"
        attribute mj:
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_neutcm.png"
        attribute mk:
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_sadcm.png"
        attribute ml:
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_surpom.png"
        attribute mm:
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_yandom.png"
        attribute mn:
            "mod_assets/MPT/gwynn/mouths/gwynn_mouth_yand2om.png"
    


    group eyes:
        
        #Default Opened eyes:
        attribute oe default if_any(["neut","happ","sad"]):
            "mod_assets/MPT/gwynn/eyes/gwynn_eyes_neut.png"
        attribute oe default if_any(["angr","anno"]):
            "mod_assets/MPT/gwynn/eyes/gwynn_eyes_angr.png"
        attribute oe default if_any(["nerv"]):
            "mod_assets/MPT/gwynn/eyes/gwynn_eyes_nerv.png"
        attribute oe default if_any(["supr"]):
            "mod_assets/MPT/gwynn/eyes/gwynn_eyes_supr.png"
        attribute oe default if_any(["sad"]):
            "mod_assets/MPT/gwynn/eyes/gwynn_eyes_sad.png"
        attribute oe default if_any(["pres"]):
            "mod_assets/MPT/gwynn/eyes/gwynn_eyes_suppressed.png"
        attribute oe default if_any(["glit"]):
            "mod_assets/MPT/gwynn/eyes/gwynn_eyes_glitch.png"
        attribute oe default if_any(["yand"]):
            "mod_assets/MPT/gwynn/eyes/gwynn_eyes_yand.png"
        
        #Default Closed eyes:
        attribute ce if_any(["neut","sad","angr","pres","glit","curi","flus","anno"]):
            "mod_assets/MPT/gwynn/eyes/gwynn_ce1.png"
        attribute ce if_any(["happ","yand","nerv"]):
            "mod_assets/MPT/gwynn/eyes/gwynn_ce2.png"

        ###All eyes - truncated tags:
        attribute e1:
            "mod_assets/MPT/gwynn/eyes/gwynn_eyes1a.png"
        attribute e2:
            "mod_assets/MPT/gwynn/eyes/gwynn_eyes1b.png"
        attribute e3:
            "mod_assets/MPT/gwynn/eyes/gwynn_eyes1c.png"
        attribute e4:
            "mod_assets/MPT/gwynn/eyes/gwynn_eyes1d.png"
        attribute e5:
            "mod_assets/MPT/gwynn/eyes/gwynn_eyes1e.png"
        attribute e6:
            "mod_assets/MPT/gwynn/eyes/gwynn_eyes1f.png"
        attribute e7:
            "mod_assets/MPT/gwynn/eyes/gwynn_eyes1g.png"
        attribute e8:
            "mod_assets/MPT/gwynn/eyes/gwynn_eyes1h.png"
        attribute ce1:
            "mod_assets/MPT/gwynn/eyes/gwynn_ce1.png"
        attribute ce2:
            "mod_assets/MPT/gwynn/eyes/gwynn_ce2.png"



    group nose:
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "mod_assets/MPT/gwynn/noses/gwynn_nobl.png"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "mod_assets/MPT/gwynn/noses/gwynn_awkw.png"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "mod_assets/MPT/gwynn/noses/gwynn_blus.png"
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            "mod_assets/MPT/gwynn/noses/gwynn_blaw.png"
        attribute nose default if_any(["awkry"]):#default nose when "crying and awkward"
            "mod_assets/MPT/gwynn/noses/gwynn_awkry.png"
        attribute nose default if_any(["blcry"]):#default nose when "blushing and crying"
            "mod_assets/MPT/gwynn/noses/gwynn_blcry.png"
        attribute nose default if_any(["blawcry"]):#default nose when "blushing and awkward and crying"
            "mod_assets/MPT/gwynn/noses/gwynn_blawcry.png"
        attribute nose default if_any(["smcry"]):#default nose when "blushing and awkward and crying"
            "mod_assets/MPT/gwynn/noses/gwynn_ce2_cry.png"
        
        #All noses - truncated tags:
        attribute n1:
            "mod_assets/MPT/gwynn/noses/gwynn_awkw.png"
        attribute n2:
            "mod_assets/MPT/gwynn/noses/gwynn_blus.png"
        attribute n3:
            "mod_assets/MPT/gwynn/noses/gwynn_blaw.png"
        attribute n4a:
            "mod_assets/MPT/gwynn/noses/gwynn_cry.png"
        attribute n4b:
            "mod_assets/MPT/gwynn/noses/gwynn_ce2_cry.png"
        attribute n5:
            "mod_assets/MPT/gwynn/noses/gwynn_awkry.png"
        attribute n6:
            "mod_assets/MPT/gwynn/noses/gwynn_blcry.png"
        attribute n7:
            "mod_assets/MPT/gwynn/noses/gwynn_blawcry.png"



    group eyebrows:
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","pres","glit"]):
            "mod_assets/MPT/gwynn/eyebrows/gwynn_brow_neut.png"
        attribute brow default if_any(["sad","nerv"]):
            "mod_assets/MPT/gwynn/eyebrows/gwynn_brow_sad.png"
        attribute brow default if_any(["angr","yand","flus","anno"]):
            "mod_assets/MPT/gwynn/eyebrows/gwynn_brow_angr.png"
        attribute brow default if_any(["doub","surp"]):
            "mod_assets/MPT/gwynn/eyebrows/gwynn_brow_doub.png"
        attribute brow default if_any(["conf"]):
            "mod_assets/MPT/gwynn/eyebrows/gwynn_brow_conf1.png"
    
        #All eyebrows - truncated tags:
        attribute b1:
            "mod_assets/MPT/gwynn/eyebrows/gwynn_brow_neut.png"
        attribute b2:
            "mod_assets/MPT/gwynn/eyebrows/gwynn_brow_sad.png"
        attribute b3:
            "mod_assets/MPT/gwynn/eyebrows/gwynn_brow_angr.png"
        attribute b4:
            "mod_assets/MPT/gwynn/eyebrows/gwynn_brow_doub.png"
        attribute b5a:
            "mod_assets/MPT/gwynn/eyebrows/gwynn_brow_conf1.png"
        attribute b5b:
            "mod_assets/MPT/gwynn/eyebrows/gwynn_brow_conf2.png"


    group blood:

        attribute blood:
            "mod_assets/MPT/gwynn/casual_left_point.png"