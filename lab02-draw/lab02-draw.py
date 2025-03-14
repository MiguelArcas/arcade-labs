import arcade
import arcade.color

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
arcade.draw_text("POWER", 340, 510,
                         arcade.color.BLACK, font_size=5, anchor_x="center")
arcade.draw_circle_outline(340, 530, 10, arcade.color.BLACK)
arcade.draw_circle_outline(340,530,6,arcade.color.RED)
arcade.draw_line(340,537,340,529, arcade.color.RED)

# Drawing the cross button
arcade.draw_rectangle_filled(400, 460, 25,100, arcade.color.LAVENDER_GRAY)
arcade.draw_rectangle_filled(400, 460, 100,25, arcade.color.LAVENDER_GRAY)
arcade.draw_line(400, 500, 400, 480, arcade.color.BLACK)
arcade.draw_line(360, 460, 380, 460, arcade.color.BLACK)
arcade.draw_line(400, 440, 400, 420, arcade.color.BLACK)
arcade.draw_line(420, 460, 440, 460, arcade.color.BLACK)

# Drawing the A button
arcade.draw_circle_filled(400, 350, 25, arcade.color.LAVENDER_GRAY)
arcade.draw_text("A", 400, 337,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
arcade.draw_circle_outline(400, 350, 27, arcade.color.BLACK)

#Drawing the house button
arcade.draw_circle_outline(400, 300, 12, arcade.color.BLACK)
arcade.draw_rectangle_filled(396,298,4,10, arcade.color.BABY_BLUE)
arcade.draw_rectangle_filled(404,298,4,10, arcade.color.BABY_BLUE)
arcade.draw_triangle_filled(400,310,390,298,410,298, arcade.color.BABY_BLUE)
arcade.draw_text("HOME",400,280,
                 arcade.color.BLACK, font_size=5, anchor_x="center")

#Drawing the + and - buttons
arcade.draw_circle_outline(365, 300, 8, arcade.color.BLACK)
arcade.draw_circle_filled(365, 300, 7, arcade.color.LAVENDER_GRAY)
arcade.draw_line(370,300,360,300, arcade.color.BLACK)
arcade.draw_circle_outline(435, 300, 8, arcade.color.BLACK)
arcade.draw_circle_filled(435, 300, 7, arcade.color.LAVENDER_GRAY)
arcade.draw_line(440,300,430,300, arcade.color.BLACK)
arcade.draw_line(436,305,436,295, arcade.color.BLACK)

#Drawing the speaker
arcade.draw_circle_filled(415,270,3, arcade.color.BLACK)
arcade.draw_circle_filled(400,270,3, arcade.color.BLACK)
arcade.draw_circle_filled(385,270,3, arcade.color.BLACK)

arcade.draw_circle_filled(415,260,4, arcade.color.BLACK)
arcade.draw_circle_filled(400,260,4, arcade.color.BLACK)
arcade.draw_circle_filled(385,260,4, arcade.color.BLACK)

arcade.draw_circle_filled(415,250,4, arcade.color.BLACK)
arcade.draw_circle_filled(400,250,4, arcade.color.BLACK)
arcade.draw_circle_filled(385,250,4, arcade.color.BLACK)

arcade.draw_circle_filled(415,240,4, arcade.color.BLACK)
arcade.draw_circle_filled(400,240,4, arcade.color.BLACK)
arcade.draw_circle_filled(385,240,4, arcade.color.BLACK)

arcade.draw_circle_filled(415,230,4, arcade.color.BLACK)
arcade.draw_circle_filled(400,230,4, arcade.color.BLACK)
arcade.draw_circle_filled(385,230,4, arcade.color.BLACK)

arcade.draw_circle_filled(415,220,3, arcade.color.BLACK)
arcade.draw_circle_filled(400,220,3, arcade.color.BLACK)
arcade.draw_circle_filled(385,220,3, arcade.color.BLACK)

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

