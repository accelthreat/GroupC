define mc = Character("Protag")
define sis = Character("Lil Sis")
define gpa = Character("Grandpa")
define edge = Character("Edgelord")

define wImg = 400
define lImg = 800
    

image mc puzzled:
    "mc puzzled.png"
    size (wImg,lImg)
image mc thinking:
    "mc thinking.png"
    size (wImg,lImg)
image mc brave:
    "mc brave.png"
    size (wImg,lImg)
image sis angry:
    "sis angry.png"
    size (400,625)
image sis happy:
    "sis happy.png"
    size (400,625)
image sis thinking:
    "sis thinking.png"
    size (400,625)
image sis angry flip:
    "sis angry.png"
    size (400,625)
    xzoom -1.0
image sis happy flip:
    "sis happy.png"
    size (400,625)
    xzoom -1.0
image sis thinking flip:
    "sis thinking.png"
    size (400,625)
    xzoom -1.0
image edge angry:
    "edge angry.png"
    size (wImg,lImg)
image edge smile:
    "edge smile.png"
    size (wImg,lImg)
image edge neutral:
    "edge neutral.png"
    size (wImg,lImg)

init:
    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #

#
init:
    define flash = Fade(.25, 0.0, .75, color="#fff")
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    define shake_and_flash = ComposeTransition(dissolve, sshake, flash)


label start:
    scene bg earth2
    with fade

    show mc puzzled at left with dissolve
    mc "I… I think I saw light!"

    show sis angry at right with dissolve
    sis "Light? Like, from the ceiling?"

    mc "No… from the sky."

    show sis thinking

    sis "Wh-what?! Where?!"

    show mc thinking
    mc "...It disappeared."

    show mc puzzled
    show sis angry
    sis "Then how do I know you’re not pranking me?!"

    show mc brave
    mc "I’m not, I swear!"

    sis "I thought skylight wasn’t real!! You’re lying to me!!"

    show mc puzzled
    mc "I..."

    hide sis with dissolve
    show gpa determined at right with moveinleft
    gpa "You’ve gotta prove yourself!"

    mc "Huh?"

    gpa "Like this."

    # Insert battle transition here HAHA

    "(Whoa, what’s happening?!)"

    with sshake

    # scene
    # with None
    scene bg earth2
    with flash

    show mc brave at left 
    show sis angry at right
    sis "Skylight isn’t real, you just want me to look stupid in front of my friends."

    mc "Uh, how does this work?"

    gpa "Pick what you think is most convincing!"

    menu .battle1:
        "Grandpa said it was real.":
            show mc puzzled
            mc "Grandpa said it was real. He's always been saying that."
            show sis thinking
            sis "Well… grandpa’s not a liar, I guess..."
            show sis angry
            sis "But wait, how do I know that grandpa really said that?"
            show mc thinking
            mc "Hm..."
            hide sis
            show gpa determined at right with dissolve
            gpa "You gotta show her something!"
            hide gpa with dissolve
            #show mc puzzled
            show sis angry at right with dissolve

        "I saw it, I really did.":
            show mc brave
            mc "I saw it, I really did."
            show sis angry
            sis "But how do I know you're not lying?!"
            show gpa determined
            gpa "Try something better, kid!"
            jump .battle1

        "Fine then, don’t believe me.":
            show mc brave
            mc "Fine then, don't believe me."
            show sis angry
            sis "Hmph!"
            show gpa disappointed
            gpa "...That's not convincing. At all."
            jump .battle1

    menu .battle2:
            "Show grandpa":
                jump .conclusion
            "Do some shit":
                jump .wrong_item
        # how 2 do inventory stuff haha just present grandpa profile or smth

    label .wrong_item:
        show sis angry
        sis "...That doesn't make any sense!"
        jump .battle2

    label .conclusion:
        show mc brave
        mc "Grandpa’s right here!"
        show gpa determined with moveinleft
        gpa "Skylight’s real, my child. It’s been gone a long time, but maybe it will come back soon."
        show sis thinking
        sis "Really grandpa? Hmm… I guess it is real then!"
        
    #battle done screen or whatev lol

    show mc puzzled
    mc "That’s what I’ve been saying..."
    show sis happy
    sis "You know what? If it's really true, we should tell the others too!"

    mc "Wh-what?! They won't believe me!"

    sis "C'mon, sis, you could do it!"
    show gpa determined
    gpa "I think this is something important that everyone should know."

    mc "Grandpa, why don't you do it?"
    show gpa disappointed
    gpa "Don't pretend like you haven't seen how they treat me. They think I'm mad."

    mc "Grandpa..."
    show gpa determined
    gpa "The skylight, it's a sign that things can and will get better. I think the others deserve to know."
    show mc thinking
    show mc brave
    mc "I'll try."
    jump grandpa

# You have to talk to grandpa again to get the science journals. Not sure how to implement that


label grandpa:
    $ protag_inv = Inventory("Your Inventory")
    $ journal = Item(name="Journal", desc="Grandpas Calculus/Physics Journal by (Young and Freedman)", icon="journal.png", act=Show("message_screen", message="The slope of the tangent line of a limacon is dy/dx\nwhere dy = dy/dΘ and dx = dx/dΘ\nTherefore, the light will come back after 75 years"))
    $ cap = Item(name="Bottle Cap", desc="The currency of your village", icon="cap.png", value=1)
    scene bg indoor2 with fade
    show gpa
    gpa "Hm? What is it, child?"

    menu .menu1:
        "Skylight":
            mc "I've been wondering about the light."

            gpa """
            Ah, the skylight. Let me give you some background on that.

            Now, you've probably heard this mentioned over and over again by <Leader>, but, the world wasn't always like this.

            Before the meteor hit, it wasn't all dust and dirt in the sky; It used to be brighter years ago, much like the light in this room right now.

            I was just a boy around your age then. I was going to school -- a big one, with actual, qualified teachers -- and learning about the atmosphere, I remember so clearly. That was when it hit.

            My pops, your great-grandfather, was a scientist. When the meteor happened, even after all the chaos, he was studying weather and climate patterns.

            He had an estimate for when the sky would clear up, and the light would come back. When we ended up settling in our community, he tried telling everyone about it. And people got hopeful.

            Unfortunately, he miscalculated. They waited days, weeks, months, then years, and it still didn't come back.

            Pops realized his error, but it was too late. When he came out with a new estimate, no one believed him anymore.

            Besides, the new estimate was decades into the future, and no one wanted to wait anymore.

            Only I believed him. I saw his journals, and I might not have finished basic calculus, but I'm sure it makes sense! He was a scientist!

            We were mocked until he passed and left me here as the sole believer, and even I was starting to lose hope unti this morning, when you saw the light.

            And I read the journals again, and they were right! The light should come back around now.

            This is important news, something that I think everyone should hear. That's why I'm telling you to do so.
            """

            #show mc puzzled
            mc "Grandpa, what will make them want to believe me?"

            gpa "Use your wits, child."

            gpa "..."

            gpa "And I think it's time to give you these."
            
            $ protag_inv.take(cap, 200)
            show screen inventory_screen(protag_inv)         
    
            $ protag_inv.take(journal)

            # insert received journals text here!! and add to inventory

            gpa "They contain all of my father's notes, and it might add to your credibility."

            #show mc thinking
            mc "I guess..."

            gpa "Now move along!! You've got a very important job to do."

label edgelord:
    label .intro:
        scene bg indoor3 with fade
        show edge neutral at right
        show mc puzzled at left with moveinleft 
        show sis happy flip with moveinleft
        edge "What do you want?"

        mc "Something important just happened, and I think everyone needs to know."

        edge "Huh?"

        mc "Something good is coming."

        show edge smile

        edge "What, did the government finally come back for us after years of leaving us to rot in this shithole?"

        mc "Wha--"

        # interrupts previous line
        edge "Oh wait! That was just a dream I had. Ten years ago. When I still thought Santa existed."

        sis "Wait, he d--"

        # interrupts
        edge "Nothing ever good happens here, Protag. Except maybe that one time I almost died while fixing the roof. That was nice."

        show sis angry flip

        sis "Can you shut up? You're really annoying."

        show edge angry

        edge "Fine, then I'm not talking to you about anything."

        mc "Sis..."

        sis "Oops."

    # There's supposed to be a part where you talk to someone else about him and you find out he likes x food so you calm him down with that but idk where to put that yet so lets skip that first
        show edge neutral
        edge "What do you want?"
    menu .menu1:
        "Light.":
            mc "I saw a light."

            show edge smile
            edge  "You must be dying then. I envy you."

            mc "No, outside. From the sky, poking through the clouds."
            show edge angry
            edge "Wh-what?!"

            #Battle stuff
            jump .preBattle1

    label .preBattle1:
        show edge neutral
        edge "You know what, I thought you and your sister were just kinda airheaded, but I know now that you are actually delusional. The more you learn."
        show sis angry flip
        sis "We're not airheads!"
        edge "Okay. So, why should I believe you?"
        jump .battle1

    menu .battle1:
        "Because I said so.":
            show mc brave
            mc "Because I said so."
            show edge smile
            edge "Hah! And who are you?"

            jump .preBattle1

        "Why shouldn't you?":
            show mc brave
            mc "Why shouldn't you?"

            edge "Because! Unlike you, I am a realist. A rational. A cynic. I don't believe everything anyone says to me. Like the tooth fairy. Only babies do that."

            sis "Wait, what?!"

            jump .preBattle2

        "I'm not dumb.":
            show mc brave
            mc "I'm not dumb. I know what I saw."

            edge "Oh yeah? How about that time you seriously thought Leader was a robot because she walked really stiff and couldn't dance?"

            mc "We were six!"

            edge "Point is, you've got a history."

            mc "That was one time!!"

            jump .preBattle1

    label .preBattle2:
        show edge neutral
        edge "You know what Leader says. The world is dying. The clouds are always going to be there."

    menu .battle2:
        "There's still hope.":
            show mc brave
            mc "There's still hope."
            show edge smile
            edge "Hah! The last time I hoped was the roof incident, and look what happened. I'm still here."

            jump .preBattle2

        "The world isn't dying.":
            show mc brave
            mc "The world isn't dying. Even if it's just a few, we still grow plants inside the laboratory, and there are still some plants and animals outside."

            edge "But we're still struggling. Life is fragile. If anything even mildly bad is going to happen to us, we don't have enough to survive that."

            jump .preBattle2

        "You believe Leader?":
            show mc brave
            mc "And you believe Leader?"

            edge "...Yes?"

            mc "And I thought you just said that you don't automatically believe everything people say."

            show edge angry
            edge "H-hey! It's not like that. It's just that our beliefs align."

            jump .preBattle3

    label .preBattle3:
        edge "Even if she were wrong, why would I choose to believe you instead? Look around us!"
        jump .battle3
    menu .battle3:
        #would probably require protag to procure a book before this option in the future
        "Look around?":
            show mc brave
            mc "Look around? That's an empirical way to assess truth."

            edge "Woooow, look at Miss Teacher's Pet here. Reading recommended books."

            mc "The fact you recognized the phrase means you've read it too."

            show edge angry
            edge "I-I read it of my own volition!"

            jump .preBattle4

        "I've never lied to you before.":
            mc "I've never lied to you before."

            edge "C'mon, were you listening? I don't have issue with you lying. I'm saying maybe you're not all that there, 'ya know."

            mc "Hmph."

            jump .preBattle3

        "It's not that bad.":
            mc "I don't think you're seeing the world as it is. It's not all that bad out there."

            show edge smile
            edge "I'M not seeing the world as it is? Really? You think I'M the one who doesn't see that we're continuing to struggle to meet the food quota every month?"

            jump .preBattle3

    label .preBattle4:
        edge "Hmph. Fine then. Show me how there's any a priori way to know that the light's coming back."
        $ edge_inv = Inventory("Edge")
        show screen inventory_screen(protag_inv, edge_inv, trade_mode=True)   
        label .looping:
            $ renpy.pause()
            if not renpy.get_screen("inventory_screen"):
                if edge_inv.qty(journal):
                    #show from inventory
                    # show journal:
                    #     xalign 0.7
                    #     yalign 0.5
                    edge "What the hell is this?"

                    mc "...Math and Physics. It calculates when the clouds will start clearing up using something called vectors and parabolic hyperboloid and what not. Anyway, it's going to be about this time."

                    edge "...Huh."

                    edge "..."

                    edge "I think I'll study this."

                    jump .conclusion
                else:
                    jump .wrong_item
            else:
                jump .looping
        

    label .wrong_item:
        edge "You're not making any sense. Have you really lost your marbles?"
        jump .preBattle4

    label .conclusion:
        # battle end wahu

        edge "Fine, you know what? _Maybe_ I'm going to consider that it will come back."

        sis "Yay!"

        edge "But know that if it doesn't actually happen, I'm really going to tell everyone that the both of you are dumb AND crazy."

        mc "It WILL come back."

        show edge smile
        edge "Heh, we'll see about that."
