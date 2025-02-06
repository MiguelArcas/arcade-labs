import arcade

arcade.open_window(800, 600, "Drawing")

# Setting the background
arcade.set_background_color(arcade.color.CELESTIAL_BLUE)

# Get ready to draw
arcade.start_render()
# --Drawing a Wii-remote--

# Drawing the base
arcade.draw_rectangle_filled(400,300,150, 500, arcade.color.WHITE)
arcade.draw_rectangle_outline(400,300,152, 502, arcade.color.BLACK)

# Drawing the A button
arcade.draw_circle_filled(400, 335, 35, arcade.color.LAVENDER_GRAY)
arcade.draw_text("A", 400, 317,
                         arcade.color.BLACK, font_size=40, anchor_x="center")

# Drawing the cross button
arcade.draw_rectangle_filled(400, 460, 25,100, arcade.color.LAVENDER_GRAY)
arcade.draw_rectangle_filled(400, 460, 100,25, arcade.color.LAVENDER_GRAY)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

