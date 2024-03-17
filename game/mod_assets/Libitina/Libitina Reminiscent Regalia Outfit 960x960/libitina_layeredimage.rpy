
layeredimage libitina base:
    at Flatten

    group outfit:
        attribute uniform default:
            "mod_assets/Libitina MPT/Poses/1.png"
        attribute regalia:
            "mod_assets/gov.sdc.libitina_gh/Poses/1k.png"

    group mood: 
        attribute happ null # happy
        attribute amus null # amused
        attribute plea null # pleased
        attribute teas null # teaseful/teasing
        attribute flat null # flattered
        
        attribute neut null # neutral (b)
        attribute unim null # unimpressed
        attribute sad null # sad
        attribute angr null # angry

        attribute neut2 null # neutral 2 (c)
        attribute unsu null # unsure
        attribute conc null # concentraiting
        attribute upse null # upset
        attribute worr null # worried

        attribute lsur null # lightly surprised
        attribute vsur null # very surprised
        attribute vple null # very pleased
        attribute vtea null # very teaseful
        attribute awkw null # awkward
    
    group blush:
        attribute nobl default:
            "mod_assets/Libitina MPT/Blushes/a.png"

    group nose:
        attribute nose_a default:
            "mod_assets/Libitina MPT/Noses/a.png"

    group mouth:
        attribute cm default if_any(['happ', 'amus', 'plea', 'teas', 'flat', 'vsur', 'lsur', 'vple', 'vtea']):
            "mod_assets/Libitina MPT/Mouths/a.png"
        attribute cm default if_any(['neut', 'unim', 'sad', 'angr']):
            "mod_assets/Libitina MPT/Mouths/b.png"
        attribute cm default if_any(['neut2', 'unsu', 'conc', 'upse', 'worr', 'awkw']):
            "mod_assets/Libitina MPT/Mouths/c.png"

        attribute om if_any(['happ', 'vsur', 'flat', 'vple', 'vtea']):
            "mod_assets/Libitina MPT/Mouths/d.png"
        attribute om if_any(['lsur', 'amus', 'plea', 'worr', 'awkw']):
            "mod_assets/Libitina MPT/Mouths/e.png"

        attribute mouth_a:
            "mod_assets/Libitina MPT/Mouths/a.png"
        attribute mouth_b:
            "mod_assets/Libitina MPT/Mouths/b.png"
        attribute mouth_c:
            "mod_assets/Libitina MPT/Mouths/c.png"
        attribute mouth_d:
            "mod_assets/Libitina MPT/Mouths/d.png"
        attribute mouth_e:
            "mod_assets/Libitina MPT/Mouths/e.png"

    group eyes:
        attribute oe default if_any(['happ', 'neut', 'neut2', 'amus', 'vsur', 'vple', 'plea']):
            "mod_assets/Libitina MPT/Eyes/a.png"
        attribute oe default if_any(['flat', 'unim', 'unsu', 'lsur', 'angr', 'upse', 'worr', 'teas', 'vtea', 'awkw', 'sad', 'conc']):
            "mod_assets/Libitina MPT/Eyes/b.png"

        attribute ce if_any(['happ', 'amus', 'vsur', 'flat', 'lsur', 'teas', 'vtea', 'vple']):
            "mod_assets/Libitina MPT/Eyes/c.png"
        attribute ce if_any(['plea', 'unim', 'unsu', 'sad', 'awkw', 'worr']):
            "mod_assets/Libitina MPT/Eyes/d.png"

        attribute eyes_a:
            "mod_assets/Libitina MPT/Eyes/a.png"
        attribute eyes_b:
            "mod_assets/Libitina MPT/Eyes/b.png"
        attribute eyes_c:
            "mod_assets/Libitina MPT/Eyes/c.png"
        attribute eyes_d:
            "mod_assets/Libitina MPT/Eyes/d.png"
    
    group eyebrows:
        attribute brow default if_any(["happ", 'neut', 'neut2', 'amus', 'lsur', 'vsur', 'flat', 'umim', 'unsu', 'plea', 'vple', 'conc', 'unim']):
            "mod_assets/Libitina MPT/Eyebrows/a.png"
        attribute brow default if_any(['teas', 'vtea', 'angr', 'upse']):
            "mod_assets/Libitina MPT/Eyebrows/b.png"
        attribute brow default if_any(['sad', 'awkw', 'worr']):
            "mod_assets/Libitina MPT/Eyebrows/c.png"

        attribute eyebrows_a:
            "mod_assets/Libitina MPT/Eyebrows/a.png"
        attribute eyebrows_b:
            "mod_assets/Libitina MPT/Eyebrows/b.png"
        attribute eyebrows_c:
            "mod_assets/Libitina MPT/Eyebrows/c.png"

layeredimage libitina leaning:
    at Flatten
    
    group outfit:
        attribute uniform default:
            "mod_assets/Libitina MPT/Poses/2.png"
        attribute yandere:
            "mod_assets/Libitina MPT/Poses/3.png"
        attribute regalia:
            "mod_assets/gov.sdc.libitina_gh/Poses/2k.png"
        attribute regalia_yandere:
            "mod_assets/gov.sdc.libitina_gh/Poses/3k.png"

    group mood: 
        attribute happ null # happy
        attribute amus null # amused
        attribute plea null # pleased
        attribute teas null # teaseful/teasing
        attribute flat null # flattered
        
        attribute neut null # neutral (b)
        attribute unim null # unimpressed
        attribute sad null # sad
        attribute angr null # angry

        attribute neut2 null # neutral 2 (c)
        attribute unsu null # unsure
        attribute conc null # concentraiting
        attribute upse null # upset
        attribute worr null # worried

        attribute lsur null # lightly surprised
        attribute vsur null # very surprised
        attribute vple null # very pleased
        attribute vtea null # very teaseful
        attribute awkw null # awkward

        attribute yand null # yandere
    
    group blush:
        attribute nobl default:
            "mod_assets/Libitina MPT/Blushes/a3.png"
        attribute lblu:
            "mod_assets/Libitina MPT/Blushes/a2.png"
        attribute blus:
            "mod_assets/Libitina MPT/Blushes/b3.png"

    group nose:
        attribute nose_a default if_not(["yand"]):
            "mod_assets/Libitina MPT/Noses/a2.png"
        attribute nose_b default if_any(["yand"]):
            "mod_assets/Libitina MPT/Noses/a3.png"

    group mouth:
        attribute cm default if_any(['happ', 'amus', 'plea', 'teas', 'flat', 'vsur', 'lsur', 'vple', 'vtea']):
            "mod_assets/Libitina MPT/Mouths/a2.png"
        attribute cm default if_any(['neut', 'unim', 'sad', 'angr']):
            "mod_assets/Libitina MPT/Mouths/b2.png"
        attribute cm default if_any(['neut2', 'unsu', 'conc', 'upse', 'worr', 'awkw']):
            "mod_assets/Libitina MPT/Mouths/c2.png"

        attribute om if_any(['happ', 'vsur', 'flat', 'vple', 'vtea', 'worr', 'awkw']):
            "mod_assets/Libitina MPT/Mouths/d2.png"
        attribute om if_any(['lsur', 'amus', 'plea']):
            "mod_assets/Libitina MPT/Mouths/e2.png"
        attribute om if_any(["yand"]):
            "mod_assets/Libitina MPT/Mouths/a3.png"

        attribute mouth_a:
            "mod_assets/Libitina MPT/Mouths/a2.png"
        attribute mouth_b:
            "mod_assets/Libitina MPT/Mouths/b2.png"
        attribute mouth_c:
            "mod_assets/Libitina MPT/Mouths/c2.png"
        attribute mouth_d:
            "mod_assets/Libitina MPT/Mouths/d2.png"
        attribute mouth_e:
            "mod_assets/Libitina MPT/Mouths/e2.png"
        attribute mouth_f:
            "mod_assets/Libitina MPT/Mouths/a3.png"
            
    group eyes:
        attribute oe default if_any(['happ', 'neut', 'neut2', 'amus', 'vsur', 'vple', 'plea']):
            "mod_assets/Libitina MPT/Eyes/a2.png"
        attribute oe default if_any(['flat', 'unim', 'unsu', 'lsur', 'angr', 'upse', 'worr', 'teas', 'vtea', 'awkw', 'sad', 'conc']):
            "mod_assets/Libitina MPT/Eyes/b2.png"
        attribute oe default if_any(["yand"]):
            "mod_assets/Libitina MPT/Eyes/a3.png"

        attribute ce if_any(['happ', 'amus', 'vsur', 'flat', 'lsur', 'teas', 'vtea', 'vple']):
            "mod_assets/Libitina MPT/Eyes/c2.png"
        attribute ce if_any(['plea', 'unim', 'unsu', 'sad', 'awkw', 'worr']):
            "mod_assets/Libitina MPT/Eyes/d2.png"

        attribute eyes_a:
            "mod_assets/Libitina MPT/Eyes/a2.png"
        attribute eyes_b:
            "mod_assets/Libitina MPT/Eyes/b2.png"
        attribute eyes_c:
            "mod_assets/Libitina MPT/Eyes/c2.png"
        attribute eyes_d:
            "mod_assets/Libitina MPT/Eyes/d2.png"
        attribute eyes_e:
            "mod_assets/Libitina MPT/Eyes/a3.png"
        attribute eyes_f:
            "mod_assets/Libitina MPT/Eyes/b3.png"
        attribute eyes_g:
            "mod_assets/Libitina MPT/Eyes/c3.png"
    
    group eyebrows:
        attribute brow default if_any(["happ", 'neut', 'neut2', 'amus', 'lsur', 'vsur', 'flat', 'umim', 'unsu', 'plea', 'vple', 'conc', 'unim']):
            "mod_assets/Libitina MPT/Eyebrows/a2.png"
        attribute brow default if_any(['teas', 'vtea', 'angr', 'upse']):
            "mod_assets/Libitina MPT/Eyebrows/b2.png"
        attribute brow default if_any(['sad', 'awkw', 'worr']):
            "mod_assets/Libitina MPT/Eyebrows/c2.png"
        attribute brow default if_any(['yand']):
            "mod_assets/Libitina MPT/Eyebrows/a3.png"

        attribute eyebrows_a:
            "mod_assets/Libitina MPT/Eyebrows/a2.png"
        attribute eyebrows_b:
            "mod_assets/Libitina MPT/Eyebrows/b2.png"
        attribute eyebrows_c:
            "mod_assets/Libitina MPT/Eyebrows/c2.png"
        attribute eyebrows_d:
            "mod_assets/Libitina MPT/Eyebrows/a3.png"
        attribute eyebrows_e:
            "mod_assets/Libitina MPT/Eyebrows/b3.png"
        attribute eyebrows_f:
            "mod_assets/Libitina MPT/Eyebrows/c3.png"
    