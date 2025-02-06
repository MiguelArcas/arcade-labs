import arcade

arcade.open_window(800, 600, "Drawing")

# Setting the background
arcade.set_background_color(arcade.color.CELESTIAL_BLUE)

# Get ready to draw
arcade.start_render()

# ---Drawing a Wii-remote---

# Drawing the base
arcade.draw_rectangle_filled(400,300,150, 500, arcade.color.WHITE)
arcade.draw_rectangle_outline(400,300,152, 502, arcade.color.BLACK)

# Drawing the power button
arcade.draw_circle_outline(340, 530, 10, arcade.color.BLACK)
arcade.draw_arc_outline(340, 530, 10, 10, arcade.color.RED,
                        0,30,10,0,1)

# Drawing the cross button
arcade.draw_rectangle_filled(400, 460, 25,100, arcade.color.LAVENDER_GRAY)
arcade.draw_rectangle_filled(400, 460, 100,25, arcade.color.LAVENDER_GRAY)
arcade.draw_line(400, 500, 400, 480, arcade.color.BLACK)

# Drawing the A button
arcade.draw_circle_filled(400, 350, 25, arcade.color.LAVENDER_GRAY)
arcade.draw_text("A", 400, 337,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
arcade.draw_circle_outline(400, 350, 27, arcade.color.BLACK)

# Drawing the 1 button
arcade.draw_circle_filled(400, 175, 15, arcade.color.LAVENDER_GRAY)
arcade.draw_text("1", 400, 164,
                         arcade.color.BLACK, font_size=25, anchor_x="center")
arcade.draw_circle_outline(400, 175, 18, arcade.color.BLACK)

# Drawing the 2 button
arcade.draw_circle_filled(400, 125, 15, arcade.color.LAVENDER_GRAY)
arcade.draw_text("2", 400, 113,
                         arcade.color.BLACK, font_size=25, anchor_x="center")
arcade.draw_circle_outline(400, 125, 18, arcade.color.BLACK)

# Drawing the connected lights squares
arcade.draw_rectangle_filled(348, 75, 15, 15, arcade.color.BLACK_OLIVE)
arcade.draw_rectangle_filled(383, 75, 15, 15, arcade.color.BLACK_OLIVE)
arcade.draw_rectangle_filled(418, 75, 15, 15, arcade.color.BLACK_OLIVE)
arcade.draw_rectangle_filled(453, 75, 15, 15, arcade.color.BLACK_OLIVE)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

