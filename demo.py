from manim import *

class DeltaBraceScene(Scene):
    def construct(self):
        # Create the dashed lines
        left_line_start = UP * 2
        left_line_end = DOWN * 2
        right_line_start = left_line_start + RIGHT * 4
        right_line_end = left_line_end + RIGHT * 4

        left_dashed_line = DashedLine(left_line_start, left_line_end, dash_length=0.1)
        right_dashed_line = DashedLine(right_line_start, right_line_end, dash_length=0.1)

        # Create deltas at the top of the dashed lines
        delta_left = MathTex(r"\delta", color=WHITE).next_to(left_dashed_line, UP)
        delta_right = MathTex(r"\delta", color=WHITE).next_to(right_dashed_line, UP)

        # Create a brace between the dashed lines, at the bottom
        brace = Brace(Line(left_line_end, right_line_end), direction=DOWN)
        brace_label = brace.get_tex(r"\text{Width of the interval}")

        # Add everything to the scene
        self.play(FadeIn(left_dashed_line), FadeIn(right_dashed_line), 
                  Write(delta_left), Write(delta_right))
        self.play(GrowFromCenter(brace), Write(brace_label))

        self.wait()

