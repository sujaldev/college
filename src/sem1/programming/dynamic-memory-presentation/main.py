from typing import Tuple
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
        self.static_and_automatic_allocation()

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

    def static_and_automatic_allocation(self):
        title = Tex(r"\textbf{Static Allocation}}").move_to((4.5 * LEFT) + (3.5 * UP))
        text_size = 30
        text = Tex(
            r"\begin{flushleft}"
            r"\textit{Static Allocation} is what happens when you declare a static or global variable. Each static or "
            r"global variable defines one block of space, of a fixed size. The space is allocated once, when your "
            r"program is executed, and is never freed."
            r"\end{flushleft}",
            font_size=text_size,
        ).move_to((2.25 * UP) + (1.275 * LEFT))

        self.play(Write(VGroup(title, text)))

        demo_code = Code(code="""
int x = 1;
void main(){
    static int y = 2;
}""", language="c").move_to((4 * LEFT) + DOWN)

        self.play(Write(demo_code))

        data_segment = (Rectangle(width=2, height=2)
                        .move_to((4 * RIGHT) + (0.5 * DOWN))
                        .stretch_to_fit_height(4, about_edge=UP))
        ds_label = Tex("Data Segment", font_size=text_size).move_to(data_segment.get_top() + (0.2 * UP))
        x_box, x_label, x_val, x_addr, x_group = generate_memory_box("x", "1", "0x1000")
        y_box, y_label, y_val, y_addr, y_group = generate_memory_box("y", "2", "0x1004")
        y_group.move_to(data_segment.get_center() + UP)
        x_group.move_to(data_segment.get_center() + DOWN)
        self.play(Write(ds_diagram := VGroup(data_segment, ds_label, x_group, y_group)))
        self.play(Indicate(demo_code.code[0]), Indicate(demo_code.code[2]))

        self.next_slide()

        new_text = Tex(
            r"\begin{flushleft}"
            r"\textit{Automatic Allocation} happens when you declare an automatic variable, such as a function argument"
            r" or a local variable. These are stored on the function call stack and are automatically freed when the a "
            r"stack frame is popped out of the stack."
            r"\end{flushleft}",
            font_size=text_size,
        ).move_to((2.25 * UP) + (1.275 * LEFT))
        self.play(
            FadeOut(ds_diagram), FadeOut(demo_code),
            Transform(title, Tex(r"\textbf{Automatic Allocation}}").move_to((3.95 * LEFT) + (3.5 * UP))),
            Transform(text, new_text)
        )

        self.next_slide()

        new_text = Tex(
            r"\begin{flushleft}\begin{itemize}"
            r"\item Static memory is allocated during compile time and thus it's size and location is pre determined, "
            r"and so, it cannot be increased or decreased during compile time."
            r"\item The amount of memory required has to be known at declaration."
            r"\item It can cause wastage of memory if the size of an array is overestimated at declaration."
            r"\item It can cause undefined behaviour if the size of an array is underestimated at declaration."
            r"\end{itemize}\end{flushleft}",
            font_size=text_size,
        ).move_to((1.275 * LEFT) + UP)
        self.play(
            Transform(title, Tex(r"\textbf{Limitations}}").move_to((5 * LEFT) + (3.5 * UP))),
            Transform(text, new_text)
        )

        self.next_slide()

        self.play(
            FadeOut(title),
            Transform(text, Tex(r"\textbf{Dynamic memory allocation} solves these problems."))
        )

        self.next_slide()

        self.play(FadeOut(text))

        self.next_slide()

# noinspection DuplicatedCode
def generate_memory_box(label: str, value: str, addr: str, position=None,
                        font_size=22) -> Tuple[Square, Text, Text, Tex, VGroup]:
    memory_box = Square(1)
    if position is not None:  # yes, the 'is not None` is required
        memory_box.move_to(position)

    box_label = Text(label, font_size=font_size).move_to(memory_box.get_top() + (0.2 * UP))
    box_val = Text(value, font_size=font_size).move_to(memory_box.get_center())
    box_addr = Tex(f"\\texttt{addr}", font_size=font_size).move_to(memory_box.get_bottom() + (0.2 * DOWN))
    group = VGroup(memory_box, box_label, box_val, box_addr)

    return memory_box, box_label, box_val, box_addr, group


if __name__ == "__main__":
    import subprocess

    subprocess.run(["./run.sh", "k"])
