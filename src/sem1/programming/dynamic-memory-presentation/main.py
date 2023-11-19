from pathlib import Path

from memory_layout import MemoryLayout

from manim import *
# noinspection PyUnresolvedReferences
from manim_slides import Slide

config.background_color = "#101216"


class Main(Slide):
    def construct(self):
        self.intro()
        self.background()

    def intro(self):
        # temporary setup to deal with the logo that I don't want to check into version control.
        logo_file = (Path(__file__).parent / "favicon.png").resolve()
        if logo_file.exists():
            logo = ImageMobject(logo_file).scale(0.1).move_to(2.5 * UP)
        else:
            logo = Square(fill_opacity=0, stroke_opacity=0)

        title = Tex(
            r"{\centering \textbf{\Large Dynamic Memory Allocation in C}\\[10pt]"
            r"--- \{Dhruv Grover, Pranav Bisht, Sujal Singh\}}"
        ).move_to(0.5 * DOWN)
        self.play(AnimationGroup(Write(title), FadeIn(logo)))

        self.next_slide()

        self.play(AnimationGroup(Unwrite(title), FadeOut(logo)), Wait(0.2))

        self.next_slide()

    def background(self):
        title = Tex(r"\textbf{\Huge Background}}")
        self.play(Write(title))

        self.next_slide()

        self.play(Transform(
            title, Tex(r"\textbf{Background}").move_to((5.35 * LEFT) + (3.5 * UP))
        ))

        text_size = 30
        text = Tex(
            r"\begin{flushleft}"
            r"When you run a process, the operating system will \\"
            r"assign some memory to your process which is laid out\\"
            r"as shown in the figure:"
            r"\end{flushleft}",
            font_size=text_size
        ).move_to(3 * LEFT)

        memory_layout = MemoryLayout(origin=3.5 * RIGHT)
        ml_group = memory_layout.generate_group()

        self.play(Write(text), FadeIn(ml_group))

        self.next_slide()

        arrow = Arrow(
            end=(arrow_end := memory_layout.code.box.get_left()),
            start=arrow_end + LEFT
        )
        self.play(
            Transform(text, Tex(
                r"\begin{flushleft}"
                r"The code section stores the instructions that\\"
                r"are to be executed on the CPU."
                r"\end{flushleft}",
                font_size=text_size
            ).move_to(3 * LEFT)),
            GrowArrow(arrow)
        )

        self.next_slide()

        self.play(
            Transform(text, Tex(
                r"\begin{flushleft}"
                r"All static data will be stored here.\\"
                r"\end{flushleft}",
                font_size=text_size
            ).move_to(3 * LEFT)),
            arrow.animate.shift(UP)
        )

        self.next_slide()

        self.play(
            Transform(text, Tex(
                r"\begin{flushleft}"
                r"This is where the the function call stack is stored,\\"
                r"function calls are pushed onto the stack as they are\\"
                r"called in ``stack frames'' containing various data\\"
                r"such as the variables declared in it's scope, which\\"
                r"are automatically destroyed once the function call \\"
                r"is complete."
                r"\end{flushleft}",
                font_size=text_size
            ).move_to(3 * LEFT)),
            arrow.animate.shift(3 * UP)
        )

        self.next_slide(auto_next=True)

        self.play(
            Transform(text, Tex(
                r"\begin{flushleft}"
                r"The stack grows downwards as needed."
                r"\end{flushleft}",
                font_size=text_size
            ).move_to(3 * LEFT)),
        )

        self.next_slide(loop=True)

        for i in range(1, 3):
            self.play(memory_layout.stack.box.animate.stretch_to_fit_height(
                1 if i % 2 == 0 else 1.5,
                about_edge=UP
            ))

        self.next_slide(auto_next=True)

        self.play(
            Transform(text, Tex(
                r"\begin{flushleft}"
                r"This is where the dynamic memory allocation\\"
                r"happens, the topic of this presentation."
                r"\end{flushleft}",
                font_size=text_size
            ).move_to(3 * LEFT)),
            arrow.animate.shift(2 * DOWN)
        )

        self.next_slide(loop=True)

        for i in range(1, 3):
            self.play(memory_layout.heap.box.animate.stretch_to_fit_height(
                1 if i % 2 == 0 else 1.5,
                about_edge=DOWN
            ))

        self.next_slide()

        self.play(FadeOut(VGroup(title, text, arrow, *ml_group)), Write(end_text := Tex(
            r"Let's dive a bit deeper into how these\\"
            r"different types of memory storage works.",
            font_size=text_size
        )))

        self.next_slide()

        self.play(Unwrite(end_text))

        self.next_slide()


if __name__ == "__main__":
    import subprocess

    subprocess.run(["./run.sh", "k"])
