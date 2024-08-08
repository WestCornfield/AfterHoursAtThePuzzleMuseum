# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image puzzleRoom = "rooms/Puzzle_Room.png"

define e = Character("Eileen")

default in_room = False
default move_count = 0
default current_room = "PuzzleRoom"
default previous_room = ""

define audio.rock_smash = "audio/sounds/rock_smash.mp3"
define audio.stone_slide = "audio/sounds/stone_slide.mp3"
define audio.glass_break = "audio/sounds/glass_break.mp3"

define inventory = []
define inside_option = False
define magazine_slid = False
define lock_waxy = True
define unpacked_box = False
define show_key_falling = False
define key_fallen = False

define open_menu = False
define open_inventory = False
define starting_sequence = True
define active_action = ''
define selected_item = ''
define option_text = ''
define player_statement = ''

define timesScrollUnread = 0

define gameOver = False

# The game starts here.

label start:
    if starting_sequence == True:
        call Setup
        $ starting_sequence = False

    #Call the first scene
    $ current_room = "LobbyRoom"
    call MyRoom from _call_MyRoom

    e "You finished the demo!"

    $ inventory.clear()
    $ timesScrollUnread = 0

    return

label Setup:
    e "Hello!"
    e "Welcome to the Puzzle Museum!"
    e "You're a Security Guard, working your first evening here!"
    e "You were hired by the eccentaric Wendell W. Weathersby."
    e "To watch his museum, from the hours of 6pm to 8pm."
    e "The museum closed for the day at 8pm."
    e "However, after seeing no one enter or exit the museum for your shift, when you attempted to leave..."
    e "You discovered that the doors were locked... from the outside?!?"
    e "You're trying to discover a way out of the museum..."
    e "You hear there's a way to get out of the museum on the Second Floor..."
    e "But the staircase to the second floor is locked by three padlocks."
    e "A gold one, a silver one and a iron one."
    e "Can you find the three keys to access the second floor?"

    return

label MyRoom:
    if gameOver == True:
        return

    #Update values behind the scenes
    $ update_gamestate()

    #Enter the scene
    $ in_room = False
    $ renpy.show_screen(current_room + "Screen")

    #React to entrance
    if current_room != previous_room:
        $ check_intro_reactions(current_room)
    $ previous_room = current_room

    if gameOver == True:
        return

    #Enable scene interactivity
    $ in_room = True
    $ _window_hide()
    $ renpy.call_screen(current_room + "Screen")

    return

label goodEnding:
    $ gameOver = True
    return

label handleObjectClick:
    $ renpy.show_screen(current_room + "Screen")
    $ open_menu = False
    $ inside_option = True
    return

label handleObjectClickWrapUp:
    $ active_action = ''
    $ selected_item = ''
    $ option_text = ''
    return

label handleTalkClick:
    $ renpy.show_screen(current_room + "Screen")
    $ active_action = 'talk'
    $ selected_item = ''
    $ option_text = 'Talk to what?'
    jump MyRoom

label handleTakeClick:
    $ renpy.show_screen(current_room + "Screen")
    $ active_action = 'take'
    $ selected_item = ''
    $ option_text = 'Take what?'
    jump MyRoom

label handleLookClick:
    $ renpy.show_screen(current_room + "Screen")
    $ active_action = 'look'
    $ selected_item = ''
    $ option_text = 'Look at what?'
    jump MyRoom

label handleInventoryObjectClick(object=''):
    $ renpy.show_screen(current_room + "Screen")
    $ active_action = ''
    $ selected_item = object
    $ option_text = 'Use {} on what?'.format(object)
    jump MyRoom

label Door:
    call handleObjectClick from _call_handleObjectClick

    if active_action == 'take' or active_action == '':
        e "On the wall in the exhibit room, there's a door."

    elif active_action == 'look':
        e "On the wall in the exhibit room, there's a door."

    elif active_action == 'talk':
        e "Despite your best efforts to start up a conversation..."
        e "The door does not speak."

    $ inside_option = False

    call handleObjectClickWrapUp from _call_handleObjectClickWrapUp

    jump MyRoom

label Magazine:
    call handleObjectClick from _call_handleObjectClick_1

    if active_action == 'take' or active_action == '':
        call TakeMagazine

    elif active_action == 'look':
        e "On the table in the puzzle room, there's a magazine."

    elif active_action == 'talk':
        e "'Salutations!' you say, extending your hand!"
        e "..."
        e "Rudely, the magazine refuses to shake your hand."

    $ inside_option = False

    call handleObjectClickWrapUp

    jump MyRoom

label NailFile:
    call handleObjectClick

    if active_action == 'take' or active_action == '':
        call TakeNailFile

    elif active_action == 'look':
        e "On the table in the puzzle room, there's a nail file."
        e "Thin and long."

    elif active_action == 'talk':
        e "'Salutations!' you say, extending your hand!"
        e "..."
        e "Rudely, the nail file sharply rejects your greeting."

    $ inside_option = False

    call handleObjectClickWrapUp

    jump MyRoom

label Lock:
    call handleObjectClick

    if selected_item == 'nail_file':
        if not magazine_slid:
            e "Oh! Brilliant!"
            e "You'll jam the nail file into the lock to unblock the key!"
            e "Then, it'll be out of the lock and..."
            e "On the... other side of the locked door."
            e "...Hmm."
            e "Great idea, but..."
            e "How can we make sure that we'll catch the key AFTER we knock it out of the lock."
        elif lock_waxy:
            e "Aha! Very clever!"
            e "With the magazine slid into proper position, you gently slide the file into the lock."
            e "..."
            e "You twist up and down."
            e "..."
            e "What the?!?"
            e "Despite your best efforts, you don't hear a metallic plunk of a key falling out of a lock!"
            e "Should you take a closer look at the lock?"
        else:
            e "Yes!"
            e "The wax is melted enough to punch through!"
            e "The magazine is in place!"
            e "All that's left..."
            e "..."
            $ show_key_falling = True
            e "YES! Effortlessly, the key pops out of the lock!"
            $ show_key_falling = False
            $ key_fallen = True
            e "You hear a metallic tink on the other side of the door..."
            e "And the smack of something hitting magazine paper!"

    elif selected_item == 'lighter':
        if lock_waxy:
            e "Success! The wax melts away!"
            $ lock_waxy = False
        else:
            e "Okay, now you're just showing off."
            e "The wax is already completely melted."

    elif active_action == 'take' or active_action == '':
        e "The lock is part of the door."
        e "Despite your best efforts, you can't pull it off."

    elif active_action == 'look':
        e "You bring your eye up to the lock."
        e "Ah! What the?!?!"
        e "The lock is full of wax!"
        e "...I mean, this is an exhibit at a museum."
        e "I guess it's more of a display than a demo."
        e "Still! Unless you melt the wax, it's too thick to jimmy the key out of the door."

    elif active_action == 'talk':
        e "You lean into the lock and whisper your deepest darkest secret."
        e "..."
        e "The lock doesn't speak it. And never will."
        e "A true friend."

    $ inside_option = False

    call handleObjectClickWrapUp

    jump MyRoom


label Plaque:
    call handleObjectClick

    if active_action == '':
        e "On the wall beside the door is a plaque."
        e "A beautiful, marble plaque."
        e "You admire the plaque for an extended period of time, perhaps too long."
        e "But perhaps not? After all, shouldn't we enjoy the beauty in the simple things we come across every day?"
        e "The plaque also has words that you can read, if you so desired. But, take your time, for the plaque itself is a marvel to behold."

        menu:
            "Read the plaque":
                call ReadPlaque
            "Don't read the plaque ":
                call DontReadPlaque

    elif active_action == 'take':
        e "The plaque is engraved into the wall."
        e "Unfortunately, you cannot take it."

    elif active_action == 'look':
        e "You lean forward to read the plaque..."
        call ReadPlaque

    elif active_action == 'talk':
        e "'Salutations!' you say, extending your hand!"
        e "..."
        e "Unfortunately, the plaque is great at informing other people..."
        e "But tragically uninterested in listening."

    $ inside_option = False

    call handleObjectClickWrapUp

    jump MyRoom

label ReadPlaque:
    e "You decide to read the plaque."
    e "It reads..."
    e "{b}THE KEYHOLE NEWSPAPER TRICK{/b}"
    e "An old classic."
    e "The adventurer stumbles on a locked door."
    e "On the other side of the door is the key that unlocks the door, stuck inside the keyhole."
    e "What's an adventurer to do?"
    e "The answer was first discovered by adventurer Wendell Q. Willowswether in 1795 after observing his wife, fellow adventurer Wendy J. Willoswether use this technique."
    e "Simply slide a newspaper* part-ways under the door, then pop the key out of the keyhole using a thin bit of metal, like a lockpick or a file."
    e "Once the key is dislodged, it will land on the newspaper. Carefully retrieve the newspaper and voila! The key is yours!"
    e "*Unfortunately, we've had to replace our newspaper so many times, as attendees of the puzzle museum tend to steal it to check and see if the crossword puzzles have already been done."
    e "You'll instead find beside the door a copy of Enigma Fathomers Quarterly, which has no crossword puzzle."
    e "We apologize for the exhibit's subsequent inauthenticity."

    return


label DontReadPlaque:
    e "You decide not to read the plaque."
    e "Reading is for nerds."

    return

label TakeMagazine:
    e "You lean forward and snatch the magazine off the desk."

    $ inventory.append('magazine')

    e "The magazine is now in your inventory!"

    return

label TakeNailFile:
    e "You lean forward and snatch the nail file off the desk."

    $ inventory.append('nail_file')

    e "The nail file is now in your inventory!"

    return

label MagazineIndicator:
    call handleObjectClick

    if selected_item == 'magazine':
        $ inventory.remove('magazine')
        $ magazine_slid = True
        e "You slide the magazine into place under the door..."

    elif active_action == 'take':
        e "Unfortunately, the drawing is... a drawing."
        e "You cannot take it."

    elif active_action == 'look' or active_action == '':
        e "There's a sketch of a magazine on the ground."
        e "With an arrow pointing forward, toward the gap between the door and the floor."
        e "Hmm... Almost like you could *do* something, based on this oh-so-subtle hint."

    elif active_action == 'talk':
        e "'Salutations!' you say, extending your hand!"
        e "..."
        e "Rudely, the drawing's arrow refuses to turn your direction."

    $ inside_option = False

    call handleObjectClickWrapUp

    jump MyRoom

label SlidMagazine:
    call handleObjectClick

    if active_action == 'take' :
        $ inventory.append('magazine')
        $ magazine_slid = False
        e "You scoop the magazine back up off the floor."

    elif active_action == 'look' or active_action == '':
        e "It's a little hard to read the magazine from the floor."
        e "You could, I suppose, turn the page with your shoe, but that would dirty the magazine."
        e "..."
        e "Nice cover, though."

    elif active_action == 'talk':
        e "'Salutations!' you say, extending your hand!"
        e "..."
        e "Rudely, the magazine lies there, pretending it can't hear you."

    $ inside_option = False

    call handleObjectClickWrapUp

    jump MyRoom

label SecurityScreen:
    call handleObjectClick

    if active_action == 'take' :
        e "Unfortunately, the screen is screwed into the wall..."
        e "You cannot take it."

    elif active_action == 'look' or active_action == '':
        e "Embedded in the wall, there's a screen."
        e "...Hey! It looks on the other side of the door..."
        e "Is a key!"
        e "...But, how can you get it?"

    elif active_action == 'talk':
        e "'Salutations!' you say, extending your hand!"
        e "..."
        e "Rudely, the live feed blinks without saying a word."

    $ inside_option = False

    call handleObjectClickWrapUp from _call_handleObjectClickWrapUp_1

    jump MyRoom

label KeyholeExhibitDoor:
    e "You enter the door to the Keyhole Exhibit"
    $ current_room = "KeyholeExhibitRoom"

    jump MyRoom

label LobbyDoor:
    e "You enter the door to the Lobby"
    $ current_room = "LobbyRoom"

    jump MyRoom

label EnterKeyholeExhibitRoom:
    # e "You wake up in a mysterious room."
    # e "You don't remember how you arrived here. But..."
    # e "Or, perhaps, *because* you can't remember..."
    # e "You decide you'd like to leave."

    return

label BannedItemsBox:
    call handleObjectClick

    if active_action == 'take' :
        #e "Unfortunately, the screen is screwed into the wall..."
        #e "You cannot take it."
        e "You reach your arm in the Banned Items Box..."
        e "..."
        e "It's pretty empty..."
        e "OH!"
        $ unpacked_box = True
        e "Inside the box, you find a lighter!"

    elif active_action == 'look' or active_action == '':
        e "This is one of the only things Debbie explained to you about the museum."
        e "The Banned Items Box!"
        e "Allegedly, there's a community of enthusiasts that try to..."
        e "Er..."
        e "'Speedrun' the museum?"
        e "This led to an escalating sequence of museum visitors bringing increasingly ridiculous items to try and 'sequence break' the museum."
        e "Apparently, they incinerate the box contents at the end of the day..."
        e "But, maybe something's still there?"

    elif active_action == 'talk':
        e "'Salutations!' you say, extending your hand!"
        e "..."
        e "Tragically, the Banned Items Box withholds its secrets from you."

    $ inside_option = False

    call handleObjectClickWrapUp

    jump MyRoom

label Lighter:
    call handleObjectClick

    if active_action == 'take' :
        e "You take the lighter off the desk.."
        $ inventory.append('lighter')
        e "The lighter is now in your inventory!"

    elif active_action == 'look' or active_action == '':
        e "An official Puzzle Museum lighter!"
        e "As found in the gift shop!"

    elif active_action == 'talk':
        e "'Salutations!' you say, extending your hand!"
        e "..."
        e "The lighter's silence leaves you cold."

    $ inside_option = False

    call handleObjectClickWrapUp

    jump MyRoom

label EnterLobbyRoom:
    e "Front door's locked."
    e "Maybe there's an emergency exit on the second floor?"

    return
