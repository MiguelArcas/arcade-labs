import arcade
import arcade.color

def draw_wii_remote(x,y):
    # ---Drawing a Wii-remote---
    # Drawing the base
    arcade.draw_rectangle_filled(400 + x, 300 + y, 150, 500, arcade.color.WHITE)
    arcade.draw_rectangle_outline(400 + x, 300 + y, 152, 502, arcade.color.BLACK)

    # Drawing the power button
    arcade.draw_text("POWER", 340 + x, 510 + y,
                     arcade.color.BLACK, font_size=5, anchor_x="center")
    arcade.draw_circle_outline(340 + x, 530 + y, 10, arcade.color.BLACK)
    arcade.draw_circle_outline(340 + x, 530 + y, 6, arcade.color.RED)
    arcade.draw_line(340 + x, 537 + y, 340 + x, 529 + y, arcade.color.RED)

    # Drawing the cross button
    arcade.draw_rectangle_filled(400 + x, 460 + y, 25, 100, arcade.color.LAVENDER_GRAY)
    arcade.draw_rectangle_filled(400 + x, 460 + y, 100, 25, arcade.color.LAVENDER_GRAY)
    arcade.draw_line(400 + x, 500 + y, 400 + x, 480 + y, arcade.color.BLACK)
    arcade.draw_line(360 + x, 460 + y, 380 + x, 460 + y, arcade.color.BLACK)
    arcade.draw_line(400 + x, 440 + y, 400 + x, 420 + y, arcade.color.BLACK)
    arcade.draw_line(420 + x, 460 + y, 440 + x, 460 + y, arcade.color.BLACK)

    # Drawing the A button
    arcade.draw_circle_filled(400 + x, 350 + y, 25, arcade.color.LAVENDER_GRAY)
    arcade.draw_text("A", 400 + x, 337 + y,
                     arcade.color.BLACK, font_size=30, anchor_x="center")
    arcade.draw_circle_outline(400 + x, 350 + y, 27, arcade.color.BLACK)

    # Drawing the house button
    arcade.draw_circle_outline(400 + x, 300 + y, 12, arcade.color.BLACK)
    arcade.draw_rectangle_filled(396 + x, 298 + y, 4, 10, arcade.color.BABY_BLUE)
    arcade.draw_rectangle_filled(404 + x, 298 + y, 4, 10, arcade.color.BABY_BLUE)
    arcade.draw_triangle_filled(400 + x, 310 + y, 390 + x, 298 + y, 410 + x, 298 + y, arcade.color.BABY_BLUE)
    arcade.draw_text("HOME", 400 + x, 280 + y,
                     arcade.color.BLACK, font_size=5, anchor_x="center")

    # Drawing the + and - buttons
    arcade.draw_circle_outline(365 + x, 300 + y, 8, arcade.color.BLACK)
    arcade.draw_circle_filled(365 + x, 300 + y, 7, arcade.color.LAVENDER_GRAY)
    arcade.draw_line(370 + x, 300 + y, 360 + x, 300 + y, arcade.color.BLACK)
    arcade.draw_circle_outline(435 + x, 300 + y, 8, arcade.color.BLACK)
    arcade.draw_circle_filled(435 + x, 300 + y, 7, arcade.color.LAVENDER_GRAY)
    arcade.draw_line(440 + x, 300 + y, 430 + x, 300 + y, arcade.color.BLACK)
    arcade.draw_line(436 + x, 305 + y, 436 + x, 295 + y, arcade.color.BLACK)

    # Drawing the speaker
    arcade.draw_circle_filled(415 + x, 270 + y, 3, arcade.color.BLACK)
    arcade.draw_circle_filled(400 + x, 270 + y, 3, arcade.color.BLACK)
    arcade.draw_circle_filled(385 + x, 270 + y, 3, arcade.color.BLACK)

    arcade.draw_circle_filled(415 + x, 260 + y, 4, arcade.color.BLACK)
    arcade.draw_circle_filled(400 + x, 260 + y, 4, arcade.color.BLACK)
    arcade.draw_circle_filled(385 + x, 260 + y, 4, arcade.color.BLACK)

    arcade.draw_circle_filled(415 + x, 250 + y, 4, arcade.color.BLACK)
    arcade.draw_circle_filled(400 + x, 250 + y, 4, arcade.color.BLACK)
    arcade.draw_circle_filled(385 + x, 250 + y, 4, arcade.color.BLACK)

    arcade.draw_circle_filled(415 + x, 240 + y, 4, arcade.color.BLACK)
    arcade.draw_circle_filled(400 + x, 240 + y, 4, arcade.color.BLACK)
    arcade.draw_circle_filled(385 + x, 240 + y, 4, arcade.color.BLACK)

    arcade.draw_circle_filled(415 + x, 230 + y, 4, arcade.color.BLACK)
    arcade.draw_circle_filled(400 + x, 230 + y, 4, arcade.color.BLACK)
    arcade.draw_circle_filled(385 + x, 230 + y, 4, arcade.color.BLACK)

    arcade.draw_circle_filled(415 + x, 220 + y, 3, arcade.color.BLACK)
    arcade.draw_circle_filled(400 + x, 220 + y, 3, arcade.color.BLACK)
    arcade.draw_circle_filled(385 + x, 220 + y, 3, arcade.color.BLACK)

    # Drawing the 1 button
    arcade.draw_circle_filled(400 + x, 175 + y, 15, arcade.color.LAVENDER_GRAY)
    arcade.draw_text("1", 400 + x, 164 + y,
                     arcade.color.BLACK, font_size=25, anchor_x="center")
    arcade.draw_circle_outline(400 + x, 175 + y, 18, arcade.color.BLACK)

    # Drawing the 2 button
    arcade.draw_circle_filled(400 + x, 125 + y, 15, arcade.color.LAVENDER_GRAY)
    arcade.draw_text("2", 400 + x, 113 + y,
                     arcade.color.BLACK, font_size=25, anchor_x="center")
    arcade.draw_circle_outline(400 + x, 125 + y, 18, arcade.color.BLACK)

    # Drawing the connected lights squares
    arcade.draw_rectangle_filled(348 + x, 75 + y, 15, 15, arcade.color.BLACK_OLIVE)
    arcade.draw_rectangle_filled(383 + x, 75 + y, 15, 15, arcade.color.BLACK_OLIVE)
    arcade.draw_rectangle_filled(418 + x, 75 + y, 15, 15, arcade.color.BLACK_OLIVE)
    arcade.draw_rectangle_filled(453 + x, 75 + y, 15, 15, arcade.color.BLACK_OLIVE)

def on_draw(delta_time):
    draw_wii_remote(on_draw.wii_remote1_x,25)
    draw_wii_remote(-100, -25)

    on_draw.wii_remote1_x += 1
on_draw.wii_remote1_x = 100

def main():
    arcade.open_window(800, 600, "Drawing 2: Now with functions!")
    arcade.set_background_color(arcade.color.BABY_BLUE)
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()

main()