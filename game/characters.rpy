#Characters are defined here

define sounds = ['audio/fox/a1.wav', 'audio/fox/a2.wav', 'audio/fox/a3.wav', 'audio/fox/a4.wav', 'audio/fox/a5.wav', 'audio/fox/a6.wav', 'audio/fox/a7.wav', 'audio/fox/a8.wav', 'audio/fox/a9.wav', 'audio/fox/a10.wav', 'audio/fox/a11.wav']
define sounds2 = ['audio/cow/Samuel_A.wav', 'audio/cow/Samuel_B.wav','audio/cow/Samuel_ch.wav','audio/cow/Samuel_E.wav','audio/cow/Samuel_I.wav','audio/cow/Samuel_L.wav','audio/cow/Samuel_O.wav','audio/cow/Samuel_ph.wav','audio/cow/Samuel_Q.wav','audio/cow/Samuel_U.wav','audio/cow/Samuel_X.wav']
define sounds3 = ['audio/badger/cr1.wav','audio/badger/cr2.wav','audio/badger/cr3.wav','audio/badger/cr4.wav','audio/badger/cr5.wav','audio/badger/cr6.wav','audio/badger/cr7.wav','audio/badger/cr8.wav','audio/badger/cr9.wav','audio/badger/cr10.wav','audio/badger/cr11.wav']

init python:


    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v



        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

init python:


    def type_sound2(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v



        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

init python:


    def type_sound3(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v



        elif event == "slow_done" or event == "end":
            renpy.sound.stop()


define Fox = Character("Sergeant F.Fox", color="fa6607", callback=type_sound)
define cow = Character("Cooper the Cow",callback=type_sound2)
define badger = Character("Billy the Badger",color="eda05c",callback=type_sound3)
define rabbit = Character("Ruby the Rabbit")
define snake = Character("Sheldon the Snake")
define magpie = Character("Maggie the Magpie")
define frog = Character("Freddie the Frog")



image Fox serious = "Fox.png"
image Fox happy = "Fox_happy.png"
image Fox evolved = "Fox_evolved.png"

image employees = "employees.png"

image map = "map.png"

image greenhouse = "greenhouse.jpg"
image badger happy = "badger_happy.png"
image badger happy idle= "badger_happy_idle.png"
image badger thinking = "badger_thinking.png"
image badger noting = "badger_noting.png"
image badger noting idle = "badger_noting_idle.png"
image badger neutral = "badger_neutral.png"
image badger neutral idle = "badger_neutral_idle.png"

image cow happy = "cow_happy.png"
image cow happy idle = "cow_happy_idle.png"
image cow lying = "cow_lying.png"
image cow nervous = "cow_nervous.png"
image cow nervous idle = "cow_nervous_idle.png"
image cow neutral = "cow_neutral.png"
image cow neutral idle = "cow_neutral_idle.png"

image rabbit happy = "rabbit_happy.png"
image rabbit happy idle = "rabbit_happy_idle.png"
image rabbit neutral = "rabbit_neutral.png"
image rabbit neutral idle = "rabbit_neutral_idle.png"
image rabbit sus = "rabbit_sus.png"
image rabbit sus idle = "rabbit_sus_idle.png"
image rabbit sad = "rabbit_sad.png"
image rabbit sad idle = "rabbit_sad_idle.png"

image snake happy = "snake_happy.png"
image snake happy idle = "snake_happy_idle.png"
image snake sus = "snake_sus.png"
image snake sus idle = "snake_sus_idle.png"
image snake neutral = "snake_neutral.png"
image snake neutral idle = "snake_neutral_idle.png"
image snake sup = "snake_sup.png"
image snake sup idle = "snake_sup_idle.png"

image magpie neutral = "magpie_neutral.png"
image magpie neutral idle = "magpie_neutral_idle.png"
image magpie happy = "magpie_happy.png"
image magpie happy idle = "magpie_happy_idle.png"
image magpie sad = "magpie_sad.png"
image magpie sad idle = "magpie_sad_idle.png"
image magpie angry = "magpie_angry.png"
image magpie angry idle = "magpie_angry_idle.png"

image frog neutral = "frog_neutral.png"
image frog neutral idle = "frog_neutral_idle.png"
image frog happy = "frog_happy.png"
image frog happy idle = "frog_happy_idle.png"
image frog sad = "frog_sad.png"
image frog sad idle = "frog_sad_idle.png"
image frog thinking = "frog_thinking.png"
image frog thinking idle = "frog_thinking_idle.png"

image failed_investigation = "failed investigation.png"

#example of a character with the typing sound
#define Type = Character("Character with typing", callback=type_sound)


#just don't add the character callback if you don't want that ound
#define NoType = Character("Character without typing")

#regular narration that doesn't have a character attached to it, add an # to it if you don't want that
#define narrator = Character("", callback=type_sound)
