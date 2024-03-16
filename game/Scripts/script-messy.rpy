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
    python:
        renpy.call_screen("dialog", message="Be done now.", ok_action=Function(renpy.full_restart))
    return