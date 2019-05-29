import arcade


WIDTH = 600
HEIGHT = 600

y = 600
a = -8

my_button = [290, 50, 100, 100 ]

def on_update(delta_time):
    global y, a

    y = a + y

    if y <= 200:
        a = 0


def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_circle_outline(100, 200, 40, arcade.color.BLACK)
    arcade.draw_line(100, 160, 100, 70, arcade.color.BLACK)
    arcade.draw_line(50, 155, 100, 120, arcade.color.BLACK)
    arcade.draw_line(150, 155, 100, 120, arcade.color.BLACK)
    arcade.draw_line(50, 25, 100, 70, arcade.color.BLACK)
    arcade.draw_line(150, 25, 100, 70, arcade.color.BLACK)
    arcade.draw_text("STOP: Log off the site.", 200, 500, arcade.color.RED, 15)
    arcade.draw_text("BLOCK: Don't respond to the messages.", 200, 400, arcade.color.YELLOW, 15)
    arcade.draw_text("RECORD: Save the message.", 200, 300, arcade.color.GREEN, 15)
    arcade.draw_text("TALK: Tell a trusted adult the situation", 200, 200, arcade.color.BLUE, 15)

    texture = arcade.load_texture("Leomarc_stop_sign.png")
    scale = .1
    arcade.draw_texture_rectangle(340, 100, scale * texture.width,
                                  scale * texture.height, texture, 0)

    texture = arcade.load_texture("cantoon-clipart-sunglasses.png")
    scale = .1
    arcade.draw_texture_rectangle(100, y, scale * texture.width,
                                  scale * texture.height, texture, 0)

    arcade.draw_xywh_rectangle_outline(my_button[0],
                                       my_button[1],
                                       my_button[2],
                                       my_button[3],
                                        arcade.color.AERO_BLUE)



def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    my_button_x, my_button_y, my_button_w, my_button_h = my_button

    if (x > my_button_x and x < my_button_x + my_button_w and
            y > my_button_y and y < my_button_y + my_button_h):
        print("Don't cyberbully!")



def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.AERO_BLUE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()