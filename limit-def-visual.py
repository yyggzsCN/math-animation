from manim import *

class limit(Scene):
    def construct(self):

        axies = (Axes(
            x_range=[0, 10, 1],
            y_range=[0, 20, 5],
            x_length=12,
            y_length=5,
            axis_config={"include_numbers": False, "include_tip": False}
        )
        .scale(0.85)
        .set_color(GREY)
        )

        axies_labels = axies.get_axis_labels(x_label='x', y_label='y')

        # sample function
        func = axies.plot(lambda x: 0.5 * (x - 2) * (x - 5) * (x - 7) + 10, x_range=[1, 8],color=ORANGE)

        # write down the definition of limit
        limit_def = (Tex(
            "We say that ", "$f$ has a limit ", "$L$", " as ", "$x$", " approach to ", "$a$",
            ", Given any ", "$\epsilon$ ", "$ > 0$", ", there exists ", 
            "$\delta$ ","$ > 0$", " such that if ", "$0 < |x - a| < \delta$", 
            ", then ", "$|f(x) - L| <$ ", "$\epsilon$"
            )
        .to_edge(UP)
        .scale(0.70)
        )
        
        title = Tex("The Definition of Limit")

        L = limit_def[2].copy()
        L_value = 10
        L_point = axies.c2p(5, L_value)
        L_dot = Dot(point=L_point, color=WHITE, fill_opacity=0.5, stroke_width=1)
        
        L_line_left = axies.c2p(axies.x_range[0],10)
        L_line_right = axies.c2p(axies.x_range[1],10)
        L_line = Line(start=L_line_left, end=L_line_right, color=WHITE)

        self.add(title)
        self.wait(3)
        self.play(FadeOut(title))
        self.play(Write(limit_def))
        self.wait()
        self.play(Create(axies), Create(axies_labels))
        self.play(Create(func))
        self.play(FadeIn(L_dot))
        self.play(FadeIn(L_line), L.animate.move_to(L_line.get_left() + LEFT * 0.5).set_color(BLUE_A))
        

        # Alpha play
        Alpha = limit_def[6].copy()
        Alpha_start = axies.c2p(5, 20)
        Alpha_end = axies.c2p(5, 0)
        Alpha_indication = Line(start=Alpha_start, end=Alpha_end, color=WHITE)
        self.play(FadeIn(Alpha_indication), Alpha.animate.move_to(Alpha_indication.get_bottom() + DOWN * 0.3))
        self.wait()

        # epsilon animation
        EpsilonU = limit_def[8].copy()
        EpsilonD = limit_def[8].copy()
       
        epsilon_dashesl = DashedLine(
            axies.c2p(0, 15), 
            axies.c2p(10, 15),
            dash_length=0.1, 
            dashed_ratio=0.5, 
            color=WHITE)
        epsilon_dashesr = DashedLine(
            axies.c2p(0, 5),
            axies.c2p(10, 5),
            dash_length=0.1,
            dashed_ratio=0.5,
            color=WHITE
        )
        Epsilon1 = Tex("$L +$", "$\epsilon$").next_to(epsilon_dashesl, LEFT, buff=0.1).scale(0.75)
        Epsilon2 = Tex("$L -$", "$\epsilon$").next_to(epsilon_dashesr, LEFT, buff=0.1).scale(0.75)
        brace3 = Brace(Line(start=axies.c2p(9.5, 10), end=axies.c2p(9.5, 15)), direction=RIGHT)
        brace4 = Brace(Line(start=axies.c2p(9.5, 10), end=axies.c2p(9.5, 5)), direction=RIGHT)
        self.play(
            FadeIn(epsilon_dashesl, epsilon_dashesr),
            GrowFromCenter(brace3), GrowFromCenter(brace4),
            EpsilonD.animate.move_to(brace3.get_tip() + RIGHT * 0.2),
            EpsilonU.animate.move_to(brace4.get_tip() + RIGHT * 0.2),
            FadeIn(Epsilon1, Epsilon2)
        )
        self.wait()

        #Delta animation
        Delta = limit_def[11].copy()
        Delta1= limit_def[11].copy()
        a1 = Alpha.copy()
        a2 = Alpha.copy()
        
        delta_dashesl = DashedLine(
            axies.c2p(4, 0), 
            axies.c2p(4, 20),
            dash_length=0.1, 
            dashed_ratio=0.5, 
            color=WHITE)
        delta_dashesr = DashedLine(
            axies.c2p(6, 0),
            axies.c2p(6, 20),
            dash_length=0.1,
            dashed_ratio=0.5,
            color=WHITE
        )
        Adelta1 = Tex("$a -$", "$\delta$").next_to(delta_dashesl, DOWN, buff=0.1).scale(0.75)
        Adelta2 = Tex("$a +$", "$\delta$").next_to(delta_dashesr, DOWN, buff=0.1).scale(0.75)
        brace1 = Brace(Line(start=axies.c2p(4, 18), end=axies.c2p(5, 18)), direction=UP)
        brace2 = Brace(Line(start=axies.c2p(5, 18), end=axies.c2p(6, 18)), direction=UP)
        self.play(
            FadeIn(delta_dashesl, delta_dashesr),
            GrowFromCenter(brace1), GrowFromCenter(brace2),
            Delta.animate.move_to(brace1.get_tip() + UP * 0.2),
            Delta1.animate.move_to(brace2.get_tip() + UP * 0.2),
            a1.animate.move_to(delta_dashesl.get_bottom() + DOWN * 0.3),
            a2.animate.move_to(delta_dashesr.get_bottom() + DOWN * 0.3),
            Transform(a2, Adelta2),
            Transform(a1, Adelta1),
        )

        #fill in some color
        fill_area = VMobject(
            color=GREEN,
            fill_opacity=0.5,
            stroke_opacity=0,
        ).set_points_as_corners([
            axies.c2p(4, 15),
            axies.c2p(6, 15),
            axies.c2p(6, 5),
            axies.c2p(4, 5),]
        )
        
        # Close the path back to the start
        self.play(FadeIn(fill_area))
        self.wait(5)

        
