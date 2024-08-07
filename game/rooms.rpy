#user interface idle assets
image dropdown_button_idle = "user_interface/dropdown/button/idle/Dropdown_Button.png"
image dropdown_button_inversed_idle = "user_interface/dropdown/button/idle/Dropdown_Button_inversed_resized.png"
image user_interface_idle = "user_interface/dropdown/interaction_panel/interaction_panel_resized.png"

image look_button_idle = "user_interface/icons/look/idle/eyeball.png"
image talk_button_idle = "user_interface/icons/talk/idle/talk.png"
image take_button_idle = "user_interface/icons/take/idle/take.png"
image inventory_button_idle = "user_interface/icons/inventory/idle/inventory.png"

#user interface hover assets
image look_button_hover:
    "user_interface/icons/look/hover/frame_00.png"
    pause 0.5
    "user_interface/icons/look/hover/frame_01.png"
    pause 0.1
    "user_interface/icons/look/hover/frame_02.png"
    pause 0.3
    "user_interface/icons/look/hover/frame_01.png"
    pause 0.1
    "user_interface/icons/look/hover/frame_00.png"
    pause 0.1
    "user_interface/icons/look/hover/frame_03.png"
    pause 0.1
    "user_interface/icons/look/hover/frame_04.png"
    pause 0.3
    "user_interface/icons/look/hover/frame_03.png"
    pause 0.1
    repeat

image talk_button_hover:
    "user_interface/icons/talk/hover/frame_00.png"
    pause 0.5
    "user_interface/icons/talk/hover/frame_01.png"
    pause 0.1
    "user_interface/icons/talk/hover/frame_02.png"
    pause 0.1
    "user_interface/icons/talk/hover/frame_03.png"
    pause 0.1
    repeat

image take_button_hover:
    "user_interface/icons/take/hover/frame_00.png"
    pause 0.5
    "user_interface/icons/take/hover/frame_01.png"
    pause 0.1
    "user_interface/icons/take/hover/frame_02.png"
    pause 0.1
    "user_interface/icons/take/hover/frame_03.png"
    pause 0.5
    "user_interface/icons/take/hover/frame_02.png"
    pause 0.1
    "user_interface/icons/take/hover/frame_01.png"
    pause 0.1
    repeat

image inventory_button_hover:
    "user_interface/icons/inventory/hover/frame_00.png"
    pause 1
    "user_interface/icons/inventory/hover/frame_01.png"
    pause 0.1
    "user_interface/icons/inventory/hover/frame_02.png"
    pause 0.3
    "user_interface/icons/inventory/hover/frame_03.png"
    pause 0.1
    "user_interface/icons/inventory/hover/frame_04.png"
    pause 0.1
    "user_interface/icons/inventory/hover/frame_02.png"
    pause 1
    "user_interface/icons/inventory/hover/frame_01.png"
    pause 0.1
    repeat

#inventory interface idle assets
image root_inventory_idle = "user_interface/inventory/background/root/idle/root_inventory_menu.png"
image up_arrow_inventory_idle = "user_interface/inventory/background/icons/up_arrow/idle.png"
image down_arrow_inventory_idle = "user_interface/inventory/background/icons/down_arrow/idle.png"
image look_inventory_idle = "user_interface/inventory/background/icons/look/idle.png"
image use_inventory_idle = "user_interface/inventory/background/icons/use/idle.png"
image close_inventory_idle = "user_interface/inventory/background/icons/close/idle.png"

image hammer_inventory_icon = "user_interface/inventory/icons/hammer/idle/hammer.png"
image mirror_inventory_icon = "user_interface/inventory/icons/mirror/idle/mirror.png"
image broken_mirror_inventory_icon = "user_interface/inventory/icons/broken_mirror/idle/broken_mirror.png"
image nail_inventory_icon = "user_interface/inventory/icons/nail/idle/nail.png"
image lighter_inventory_icon = "user_interface/inventory/icons/lighter/idle/idle.png"

#backgrounds
#image lobby_background = im.FactorScale("rooms/Lobby_Room/png/Lobby_default.png", 0.5)
image lobby_background = im.FactorScale("rooms/Lobby_Room/png/Lobby_default.png", 0.5)
image keyhole_exhibit_background = im.FactorScale("rooms/Keyhole_Exhibit_Room/png/Keyhole_Exhibit_Room_nothing_placed.png", 0.5)
#image keyhole_exhibit_background = im.FactorScale("rooms/Keyhole_Exhibit_Room/png/Keyhole_Exhibit_Room_nothing_placed.png", 0.5)

#objects
#lobby
image keyhole_exhibit_door = im.FactorScale("objects/lobby_room_objects/Keyhole_Exhibit_Room_Door/png/Keybole_Exhibit_Room_With_Magazine.png", 0.5)
image office_door = im.FactorScale("objects/lobby_room_objects/Office_Door/png/Office_Door.png", 0.5)
image debbie_desk = im.FactorScale("objects/lobby_room_objects/Debbie_Desk/png/Debbie_Desk.png", 0.5)
image banned_items_box = im.FactorScale("objects/lobby_room_objects/Lost_Box/png/Banned_Items_Box.png", 1.0)
image car_room_door = im.FactorScale("objects/lobby_room_objects/Car_Room_Door/png/Car_Room_Door.png", 0.5)
image lighter = im.FactorScale("objects/lobby_room_objects/Lighter/png/idle/idle.png", 0.25)

#keyhole exhibit
image keyhole_exhibit_plaque = im.FactorScale("objects/keyhole_exhibit_room_objects/Plaque/png/Plaque.png", 0.5)
image keyhole_exhibit_lock = im.FactorScale("objects/keyhole_exhibit_room_objects/Lock/png/Lock.png", 0.5)
image keyhole_exhibit_locked_door = im.FactorScale("objects/keyhole_exhibit_room_objects/Wooden_Door/png/Door_with_Lock.png", 0.5)
image keyhole_exhibit_magazine_indicator = im.FactorScale("objects/keyhole_exhibit_room_objects/Magazine_Indicator/png/Magazine_Indicator.png", 0.5)
image keyhole_exhibit_security_screen = im.FactorScale("objects/keyhole_exhibit_room_objects/Security_Screen/png/with_key/security_screen.png", 0.5)
image keyhole_exhibit_nail_file = im.FactorScale("objects/keyhole_exhibit_room_objects/Nail_File/png/Nail_File.png", 0.5)
image keyhole_exhibit_magazine = im.FactorScale("objects/keyhole_exhibit_room_objects/Magazine/png/magazine.png", 0.5)
image lobby_door = im.FactorScale("objects/keyhole_exhibit_room_objects/Lobby_Door/png/Door_To_Lobby.png", 0.5)
image keyhole_exhibit_table = im.FactorScale("objects/keyhole_exhibit_room_objects/Table/png/Table.png", 0.5)
image slid_magazine = im.FactorScale("objects/keyhole_exhibit_room_objects/Magazine/Slid/png/magazine.png", 1.5)

#inventory interaction_panel_resized
image magazine_inventory_icon = im.FactorScale("user_interface/inventory/icons/magazine/magazine.png", 0.5)
image nail_file_inventory_icon = im.FactorScale("user_interface/inventory/icons/nail_file/idle/Nail_File.png", 0.5)

image security_screen_live_animation:
    "objects/keyhole_exhibit_room_objects/Security_Screen/Live_Overlay/animation/frame_01.png"
    pause 1
    "objects/keyhole_exhibit_room_objects/Security_Screen/Live_Overlay/animation/frame_02.png"
    pause 1
    repeat

image security_screen_key_falling_animation:
    "objects/keyhole_exhibit_room_objects/Security_Screen/animation/key_falls/resized/frame_01.png"
    pause 0.1
    "objects/keyhole_exhibit_room_objects/Security_Screen/animation/key_falls/resized/frame_02.png"
    pause 0.1
    "objects/keyhole_exhibit_room_objects/Security_Screen/animation/key_falls/resized/frame_03.png"
    pause 0.1
    "objects/keyhole_exhibit_room_objects/Security_Screen/animation/key_falls/resized/frame_04.png"
    pause 0.1
    "objects/keyhole_exhibit_room_objects/Security_Screen/animation/key_falls/resized/frame_05.png"
    pause 0.1
    "objects/keyhole_exhibit_room_objects/Security_Screen/animation/key_falls/resized/frame_06.png"
    pause 0.1
    "objects/keyhole_exhibit_room_objects/Security_Screen/animation/key_falls/resized/frame_07.png"
    pause 0.1

image security_screen_live_no_key_animation:
    "objects/keyhole_exhibit_room_objects/Security_Screen/animation/no_key/resized/frame_01.png"
    pause 1
    "objects/keyhole_exhibit_room_objects/Security_Screen/animation/no_key/resized/frame_02.png"
    pause 1
    repeat


#UI inventory transforms
transform dropdown_button_location:
    ypos 0
    xpos 568

transform open_dropdown_button_location:
    ypos 0
    xpos 568
    ease 1 xpos 568 ypos 128
    ease 1 xpos 568 ypos 112

transform open_user_interface_location:
    ypos -130
    xpos 0
    ease 1 xpos 0 ypos 0
    ease 1 xpos 0 ypos -16

transform open_look_button_location:
    ypos -110
    xpos 28
    ease 1 xpos 28 ypos 32
    ease 1 xpos 28 ypos 16

transform open_talk_button_location:
    ypos -110
    xpos 132
    ease 1 xpos 132 ypos 28
    ease 1 xpos 132 ypos 12

transform open_take_button_location:
    ypos -110
    xpos 248
    ease 1 xpos 248 ypos 28
    ease 1 xpos 248 ypos 12

transform open_inventory_button_location:
    ypos -110
    xpos 352
    ease 1 xpos 352 ypos 28
    ease 1 xpos 352 ypos 12

transform root_inventory_menu_location:
    ypos 100
    xpos 100

transform up_arrow_inventory_location:
    ypos 125
    xpos 1000

transform down_arrow_inventory_location:
    ypos 275
    xpos 1000

transform look_inventory_location:
    ypos 380
    xpos 130

transform use_inventory_location:
    ypos 380
    xpos 270

transform close_inventory_location:
    ypos 380
    xpos 710

transform inventory_spot(spot_number):
    ypos 140
    xpos (150 + (spot_number * 100))

transform option_text_location:
    xalign 0.5
    yalign 0.95

#object transforms
transform lefthand_door_location:
    ypos 252
    xpos 136

transform righthand_door_location:
    ypos 252
    xpos 1044

transform righthand_door_location_2:
    ypos 264
    xpos 1070

transform office_door_location:
    ypos 218
    xpos 362

transform debbie_desk_location:
    ypos 340
    xpos 578

transform lost_box_location:
    ypos 264
    xpos 768

transform plaque_location:
    ypos 300
    xpos 350

transform keyhole_exhibit_locked_door_location:
    ypos 220
    xpos 530

transform slid_magazine_location:
    ypos 516
    xpos 570

transform keyhole_exhibit_lock_location:
    ypos 380
    xpos 570

transform magazine_indicator_location:
    ypos 530
    xpos 595

transform keyhole_exhibit_security_location:
    ypos 220
    xpos 735

transform keyhole_exhibit_table_location:
    ypos 445
    xpos 782

transform keyhole_exhibit_nail_file_location:
    ypos 434
    xpos 820

transform keyhole_exhibit_magazine_location:
    ypos 400
    xpos 850

transform screen_location:
    ypos 220
    xpos 735

transform live_location:
    ypos 260
    xpos 790

transform lighter_location:
    ypos 309
    xpos 668

screen LobbyRoomScreen():
    add "lobby_background"
    imagebutton:
        idle "keyhole_exhibit_door"
        at lefthand_door_location
        action [SensitiveIf(in_room and not inside_option), Jump("KeyholeExhibitDoor")]
    imagebutton:
        idle "office_door"
        at office_door_location
    imagebutton:
        idle "debbie_desk"
        at debbie_desk_location
    imagebutton:
        idle "banned_items_box"
        at lost_box_location
        action [SensitiveIf(in_room and not inside_option), Jump("BannedItemsBox")]
    if unpacked_box and not 'lighter' in inventory:
        imagebutton:
            idle "lighter"
            at lighter_location
            action [SensitiveIf(in_room and not inside_option), Jump("Lighter")]
    imagebutton:
        idle "car_room_door"
        at righthand_door_location
    if not open_menu and not open_inventory:
        imagebutton:
            idle "dropdown_button_idle"
            at dropdown_button_location
            action [SensitiveIf(not inside_option), SetVariable("open_menu", True)]
    if open_menu and not open_inventory:
        imagebutton:
            idle "dropdown_button_inversed_idle"
            at open_dropdown_button_location
            action [SensitiveIf(not inside_option), SetVariable("open_menu", False)]
        imagebutton:
            idle "user_interface_idle"
            at open_user_interface_location
        imagebutton:
            auto "look_button_%s"
            at open_look_button_location
            action [SensitiveIf(not inside_option), SetVariable("active_action", "look"), SetVariable("selected_item", ''), SetVariable("option_text", "Look at what?")]
        imagebutton:
            auto "talk_button_%s"
            at open_talk_button_location
            action [SensitiveIf(not inside_option), SetVariable("active_action", "talk"), SetVariable("selected_item", ''), SetVariable("option_text", "Talk to what?")]
        imagebutton:
            auto "take_button_%s"
            at open_take_button_location
            action [SensitiveIf(not inside_option), SetVariable("active_action", "take"), SetVariable("selected_item", ''), SetVariable("option_text", "Take what?")]
        imagebutton:
            auto "inventory_button_%s"
            at open_inventory_button_location
            action [SensitiveIf(not inside_option), SetVariable("open_menu", False), SetVariable("open_inventory", True), SetVariable('active_action', ''), SetVariable('selected_item', ''), SetVariable('option_text', '')]
    if open_inventory:
        imagebutton:
            idle "root_inventory_idle"
            at root_inventory_menu_location
        imagebutton:
            idle "up_arrow_inventory_idle"
            at up_arrow_inventory_location
        imagebutton:
            idle "down_arrow_inventory_idle"
            at down_arrow_inventory_location
        imagebutton:
            idle "look_inventory_idle"
            at look_inventory_location
        imagebutton:
            idle "use_inventory_idle"
            at use_inventory_location
        imagebutton:
            idle "close_inventory_idle"
            at close_inventory_location
            action [SensitiveIf(in_room and not inside_option), SetVariable("open_inventory", False)]
        for item in inventory:
            imagebutton:
                idle "{}_inventory_icon".format(item)
                at inventory_spot(inventory.index(item))
                action [SensitiveIf(in_room and not inside_option), SetVariable("active_action", ""), SetVariable("open_inventory", False), SetVariable("selected_item", item), SetVariable("option_text", "Use {} with what?".format(item.capitalize().replace('_', ' ')))]
    if option_text != '':
        text "{}".format(option_text):
            at option_text_location

screen KeyholeExhibitRoomScreen():
    add "keyhole_exhibit_background"
    imagebutton:
        idle "keyhole_exhibit_plaque"
        at plaque_location
        action [SensitiveIf(in_room and not inside_option), Jump("Plaque")]
    imagebutton:
        idle "lobby_door"
        at righthand_door_location_2
        action [SensitiveIf(in_room and not inside_option), Jump("LobbyDoor")]
    imagebutton:
        idle "keyhole_exhibit_locked_door"
        at keyhole_exhibit_locked_door_location
    if magazine_slid:
        imagebutton:
            idle "slid_magazine"
            at slid_magazine_location
            action [SensitiveIf(in_room and not inside_option), Jump("SlidMagazine")]
    imagebutton:
        idle "keyhole_exhibit_lock"
        at keyhole_exhibit_lock_location
        action [SensitiveIf(in_room and not inside_option), Jump("Lock")]
    imagebutton:
        idle "keyhole_exhibit_magazine_indicator"
        at magazine_indicator_location
        action [SensitiveIf(in_room and not inside_option), Jump("MagazineIndicator")]
    imagebutton:
        idle "keyhole_exhibit_security_screen"
        at keyhole_exhibit_security_location
        action [SensitiveIf(in_room and not inside_option), Jump("SecurityScreen")]
    imagebutton:
        idle "security_screen_live_animation"
        at live_location
    if show_key_falling:
        imagebutton:
            idle "security_screen_key_falling_animation"
            at screen_location
    elif key_fallen:
        imagebutton:
            idle "security_screen_live_no_key_animation"
            at screen_location
    imagebutton:
        idle "keyhole_exhibit_table"
        at keyhole_exhibit_table_location
    if not 'nail_file' in inventory:
        imagebutton:
            idle "keyhole_exhibit_nail_file"
            at keyhole_exhibit_nail_file_location
            action [SensitiveIf(in_room and not inside_option), Jump("NailFile")]
    if not 'magazine' in inventory and not magazine_slid:
        imagebutton:
            idle "keyhole_exhibit_magazine"
            at keyhole_exhibit_magazine_location
            action [SensitiveIf(in_room and not inside_option), Jump("Magazine")]
    if not open_menu and not open_inventory:
        imagebutton:
            idle "dropdown_button_idle"
            at dropdown_button_location
            action [SensitiveIf(not inside_option), SetVariable("open_menu", True)]
    if open_menu and not open_inventory:
        imagebutton:
            idle "dropdown_button_inversed_idle"
            at open_dropdown_button_location
            action [SensitiveIf(not inside_option), SetVariable("open_menu", False)]
        imagebutton:
            idle "user_interface_idle"
            at open_user_interface_location
        imagebutton:
            auto "look_button_%s"
            at open_look_button_location
            action [SensitiveIf(not inside_option), SetVariable("active_action", "look"), SetVariable("selected_item", ''), SetVariable("option_text", "Look at what?")]
        imagebutton:
            auto "talk_button_%s"
            at open_talk_button_location
            action [SensitiveIf(not inside_option), SetVariable("active_action", "talk"), SetVariable("selected_item", ''), SetVariable("option_text", "Talk to what?")]
        imagebutton:
            auto "take_button_%s"
            at open_take_button_location
            action [SensitiveIf(not inside_option), SetVariable("active_action", "take"), SetVariable("selected_item", ''), SetVariable("option_text", "Take what?")]
        imagebutton:
            auto "inventory_button_%s"
            at open_inventory_button_location
            action [SensitiveIf(not inside_option), SetVariable("open_menu", False), SetVariable("open_inventory", True), SetVariable('active_action', ''), SetVariable('selected_item', ''), SetVariable('option_text', '')]
    if open_inventory:
        imagebutton:
            idle "root_inventory_idle"
            at root_inventory_menu_location
        imagebutton:
            idle "up_arrow_inventory_idle"
            at up_arrow_inventory_location
        imagebutton:
            idle "down_arrow_inventory_idle"
            at down_arrow_inventory_location
        imagebutton:
            idle "look_inventory_idle"
            at look_inventory_location
        imagebutton:
            idle "use_inventory_idle"
            at use_inventory_location
        imagebutton:
            idle "close_inventory_idle"
            at close_inventory_location
            action [SensitiveIf(in_room and not inside_option), SetVariable("open_inventory", False)]
        for item in inventory:
            imagebutton:
                idle "{}_inventory_icon".format(item)
                at inventory_spot(inventory.index(item))
                action [SensitiveIf(in_room and not inside_option), SetVariable("active_action", ""), SetVariable("open_inventory", False), SetVariable("selected_item", item), SetVariable("option_text", "Use {} with what?".format(item.capitalize().replace('_', ' ')))]
    if option_text != '':
        text "{}".format(option_text):
            at option_text_location
