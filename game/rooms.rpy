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

#backgrounds
image lobby_background = im.FactorScale("rooms/Lobby_Room/png/Lobby_default.png", 0.5)
image keyhole_exhibit_background = im.FactorScale("rooms/Keyhole_Exhibit_Room/png/Keyhole_Exhibit_Room_nothing_placed.png", 0.5)

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

screen LobbyRoomScreen():
    add "lobby_background"
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

screen KeyholeExhibitRoomScreen():
    add "keyhole_exhibit_background"
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
