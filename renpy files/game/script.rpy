# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Circe", color="#95dff1", image="circe")
define b = Character("Bella", color="#4d4d4d", image="bella")
define p = None
image bg school = "images/backgrounds/school.png"
image bg darkspace school = "images/backgrounds/darkspace school.png"
image bg darkspace exitportal = "images/backgrounds/darkspace exitportal.png"
image bg darkspace judgement eyes = "images/backgrounds/darkspace judgement eyes.jpg"
image bg darkspace eyes = "images/backgrounds/darkspace manyeyes.png"

image b = "images/characters/bella/bella.png"
image b attacked = "images/characters/bella/bella attacked.png"
image b kiss = "images/characters/bella/bella kiss.png"

image c = "images/characters/circe/circe.png"
image c blush = "images/characters/circe/circe blush.png"
image c kiss = "images/characters/circe/circe kiss.png"

image p = "images/characters/player/player.png"
image p blush = "images/characters/player/player blush.png"

label start:
    python:
        playername = renpy.input("What is your name?").strip().title()
        p = Character(playername, color="#755526", image="player")
    jump opening

label opening:
    show bg darkspace judgement eyes with fade
    $ renpy.say(None , playername + "...")
    pause 1.0
    """So you have chosen to face your past

    But what if you lived it again?

    Instead of just remembering it?

    Could you face what you did?"""
    hide bg darkspace judgement eyes with fade
    "5 Years Ago"
    "On your way to your first day at your new school, you find a mysterious object on the side of the road. Looking closer, you see that it's a small, ornate box with intricate carvings."
    "{b}You acquired a small box thats {i}definitely{/i} not cursed. Good luck lol{/b}"
    jump darkspace

label darkspace:
    show bg school with fade
    show p at left 
    show c at right
    "Girl" """h-hey... a-are you new here?

    i- i've never seen you before...
    
    i- i feel like i know you somehow..."""
    hide c with dissolve
    "The girl blushes and dashes away, leaving you confused."
    hide bg school
    hide p
    "You black out, and when you wake up, you find yourself in the school again, but there seems to be no one around..."
    show bg darkspace school
    show p at left
    "Turning around, you spot Bella, your lifelong friend, looking at you with an accusing glare."
    show b at right 
    b "What the fuck did you do this time?"
    p "I dont know, I dont know whats going on"
    b "Bullshit"
    p "Bella, I swear! Stop accusing me of something like you always do, and let's figure out what the hell is going on!"
    b "Fine, we can figure this shit out together. Since you're such a genius, any ideas?"
    p "No, but wait. Did you just call me smart?"
    b "No, dumbass. Stop yapping, and let's look around"
    b "ACTUALLY, THIS IS YOUR FUCKING FAULT, AND THERFORE YOUR DAMN PROBLEM!"
    b "YOU TRAPPED ME IN THIS PLACE, SO FUCK OFF!"
    "Bella storms off, leaving you alone in the eerie silence."
    hide b
    menu:
        "Follow her":
            jump followbella
        "Give her space":
            jump givebellaspace

label followbella:
    p "Bella, wait!"
    show b at right
    b "The fuck do you want!?"
    p "I just want to talk."
    p "B, Bella, please. Just, listen to me."
    b "Fine"
    p  "I know about as much as you do about this place, aka nothing."
    p "But I think if we work together, we can get out of here"
    b "Oh God. Another one of your sappy speeches?"
    b "Spare me. Fine. I get it. We can stick together, and get the hell out of here."
    p "You mean it?"
    b "Don't tempt me..."
    show c at center behind b,p
    "Girl" "h- hey..."
    "Girl" "i heard you guys talking about getting out of here..."
    "Girl" "c-can i join you?"
    menu:
        "Let her join you":
            jump polyending
        "Tell her to fuck off":
            p "No"
            p "Im getting out of here, with my best friend"
            p "We dont even know you"
            p "So fuck off"
            "The girl cries and runs away"
            hide c
            b "There was no reason to do that!"
            b "We didnt know her, yeah, but you didnt have to be so damn mean about it!"
            p "I'm sorry Bella..."
            b "Not good enough."
            b "Im leaving too, maybe when you learn to be nice I'll come back"
            hide b
            jump explorealone
label givebellaspace:
    show c at right
    "Girl" "it- its you again..."
    "Girl" "d- do you know whats going on?"
    "Girl" "i- i have a theory..."
    p "What is it?"
    "Girl" "i- i think we're in another dimension..."
    "Girl" "something other, even eldritch..."
    p "That's not a bad idea"
    "Girl" "y- you think so?"
    p "Yea, I do. Looking at you now, you're..."
    p "You're kind of cute..."
    show c blush
    "Girl" "Y-you think so?"
    "The girl runs away again, blushing furiously."
    hide c
    p "She keeps running away..."
    p "Am I that scary now?"
    menu:
        "Call after her":
            jump callaftercirce
        "Look around":
            jump explorealone

label callaftercirce:
    p "Hey, wait up! I never got your name, cutie!"
    show c at right with fade
    c "i- i'm circe..."
    p "Circe, huh? That's a pretty name."
    p "I'm [playername]. Nice to meet you, Circe."
    c "n- nice to meet you too, [playername.lower()]..."
    c "i w- wanted to ask you..."
    c "d- do you want to be friends?"
    p "Of course. I'd love to be friends with such a cutie~"
    "The two of you decide to explore together, and come across a large collection of cats"
    "The cats lead you to an exit portal"
    show bg darkspace exitportal
    "The two of you step through, and return to the real world"
    hide bg darkspace exitportal
    show school with fade
    c "n- now this is all over..."
    c "d- do you want to go out with me?"
    p "Of course I do, cutie~"
    show c kiss
    show p blush
    "Game End - Circe Ending"
    return

label explorealone:
    "You spend a while wandering around alone"
    "You jump at a few shadows, but nothing else happens"
    "Until, you hear a scream in the distance..."
    play sound bellascream
    menu:
        "Investigate the sound":
            jump investigatethesound
        "Do nothing":
            jump ignorethesound

label investigatethesound:
    hide p
    hide bg darkspace school
    show bg darkspace exitportal
    show b attacked at right
    show p at left
    "You arrive in time to see Bella being attacked by an eldritch figure, not unlike your new appearance." 
    menu:
        "Save Bella":
            jump savebella
        "Abandon her":
            jump abandonbella
label savebella:
    "You somehow manage to fend off the creature"
    "Huge eyes begin to appear around you" 
    show bg darkspace eyes
    p "Bella, can youy see those eyes?"
    b "What eyes? I dont see anything!"
    p "You dont? They're everywhere!"
    hide b
    hide p
    hide bg darkspace exitportal
    "The eyes attack and kill you both"
    "Game End - Death by giant eyes Ending"
    return
label abandonbella:
    "The shadowy figure kills Bella"
    hide b
    "Bet you wish you saved her the first time round..."
    "Your body begins to morph and shift, the eldritch part of you taking over"
    "Your humanity disappears"
    "Until, you remember her, Bella"
    "Your friend"
    p "I won't let her die this time"
    show b at right
    "You manange to bring Bella back from the dead"
    show b kiss
    show p blush
    "She kisses you, and the two of you live out the rest of your lives in this strange realm of memories and futures."
    "Game End - Bella Ending"
    return
label polyending:
    p "Yea, you can come with us. What's your name by the way?"
    c "i- im circe"
    p "It's lovely to meet you Circe"
    p "I'm [playername], and this is Bella"
    "You notice Circe seems unable to look away from you, but you decide to say nothing about it. She's cute, after all. Bella too, for that matter..."
    hide bg darkspace
    hide b
    hide p
    hide c
    "You explore the mysterious dimension for a long time, it seems days have passed. You cant tell how long it's really been, your sense of time is different here."
    "After a long time, you finally discover a portal that you think is an exit"
    show bg darkspace exitportal
    show p at center
    show b at left behind b
    show c at right behind b, p
    p "I guess this is it..."
    c "y-yea..."
    b "Finally."
    c "hey [playername.lower()]..."
    c "i- i like you..."
    show c kiss
    show p blush
    b "Hey! I was here first!"
    c "we can share..."
    b "Fine."
    show b kiss
    p "G- guys?"
    p "A- are we all dating now?"
    c "y-yes"
    b "Shut up and let us kiss you, dumbass"
    "You all escape together, and you happily live with your two girlfriends, finally free from those stupid memories"
    hide p
    hide b
    hide c
    show bg darkspace judgement eyes
    """So you would change things...
    
    and not leave either of them behind...
    
    You did well, [playername]"""

    "Game End - Poly Ending"
label ignorethesound:
    "You find a bunch of cats"
    "They lead you to an exit, and you escape, alive but alone"
    hide p
    show bg darkspace judgement eyes
    "So once again, you abandoned them both..."
    "Guess you can't change the past..."
    "Even if it's ony memories..."
    "Game Over - Alone Ending"
    return