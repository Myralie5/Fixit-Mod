image fake_exception = Text("An exception has occurred.", size=40, style="_default")
image fake_exception2 = Text("File \"game/selfdiagnosic.rpy\", line 2\nSee traceback.txt for details.", size=20, style="_default")

label messy:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    d "Author-chan!"
    show sayori 1 at t21 zorder 1
    s "Author-chan!"
    show monika 1 at t22 zorder 1
    m "Author-kun?"
    show scene black
    "beeeeeeeeeeeep"
    show bg residential_day
    show sayori turned dist at f21 
    s om "Somebody kill me."
    show sayori vsur at t21
    show gwynn happ ce om at f22
    d "Okay!!!"
    show scene black
    "beeeeeeeeeeeep"
    show bg residential_day
    python:
        renpy.call_screen("dialog", message="Be done now.", ok_action=Function(renpy.full_restart))
    return