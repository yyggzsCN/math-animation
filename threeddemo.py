from manim import *
class threeddemo(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=8,
            y_length=6,
            z_length=6,
        )
        def parabola(x):
            return x ** 2

        graph = axes.plot(lambda x: parabola(x), x_range=[-2, 2, 1], color=YELLOW)
        rects = axes.get_riemann_rectangles(
            graph=graph, x_range=[-2, 2], dx=0.1, stroke_color=WHITE
        )

        def curve_func(t):
            return np.array([np.cos(t), np.sin(t), t])

        # Create a parametric curve using ParametricFunction
        curve = ParametricFunction(curve_func, t_range=[-2 * PI, 2 * PI], color=RED)

        self.add(axes, graph)
        self.wait()

        self.move_camera(phi=60 * DEGREES)

        self.wait()
        self.move_camera(theta=45*DEGREES)

        self.begin_ambient_camera_rotation(
            rate=PI/10, about="theta"
        )
        self.wait()
        self.play(Create(rects), run_time=3)
        self.play(Create(curve))
        self.wait()
        self.stop_ambient_camera_rotation()

        self.begin_ambient_camera_rotation(
            rate=PI/10, about="phi"
        )

        self.wait(2)
        self.stop_ambient_camera_rotation

