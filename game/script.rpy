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
define mirror_placed = False
define wall_smashed = False
define nail_removed = False
define scroll_read = False
define broke_mirror = False

define open_menu = False
define open_inventory = False
define active_action = ''
define selected_item = ''
define option_text = ''
define player_statement = ''

define timesScrollUnread = 0

define gameOver = False

# The game starts here.

label start:
    call Setup

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

label TakeMagazine:
    e "You lean forward and snatch the magazine off the desk."

    $ inventory.append('magazine')

    e "The magazine is now in your inventory!"

    return

label SecurityScreen:
    call handleObjectClick

    if active_action == 'take' or active_action == '':
        e "Unfortunately, the screen is screwed into the wall..."
        e "You cannot take it."

    elif active_action == 'look':
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
    e "You wake up in a mysterious room."
    e "You don't remember how you arrived here. But..."
    e "Or, perhaps, *because* you can't remember..."
    e "You decide you'd like to leave."

    return

label EnterLobbyRoom:
    e "Front door's locked."
    e "Maybe there's an emergency exit on the second floor?"

    return
