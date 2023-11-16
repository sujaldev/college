from typing import Tuple

from manim import *
# noinspection PyUnresolvedReferences
from manim_slides import Slide

config.background_color = "#101216"


class Main(Slide):
    def construct(self):
        self.intro()
        self.pointers()

    def intro(self):
        title = Tex(
            r"\textbf{Call by Value and Call by Reference in C}\\[20pt]"
            r"A presentation by Sujal Singh"
        )
        self.play(Write(title))

        self.next_slide()

        self.play(Unwrite(title))

    def pointers(self):
        title = Tex(r"First, let's see what the \& character does:").move_to(3 * UP)
        self.play(Write(title))

        demo_code = Code(code="int x = 2;\nint *px = &x;", insert_line_no=False, language="c").move_to(3 * LEFT)
        self.play(FadeIn(demo_code))

        self.next_slide()

        x_rect, x_label, x_val, x_addr = generate_memory_box("x", "2", "0x1000", 2.5 * RIGHT)
        self.play(Write(VGroup(x_rect, x_label, x_val, x_addr)))

        self.next_slide()

        px_rect, px_label, px_val, px_addr = generate_memory_box("px", "0x1000", "0x1100", 5 * RIGHT)
        self.play(Write(VGroup(px_rect, px_label, px_val, px_addr)))

        self.next_slide()

        self.play(Transform(
            title, Tex(r"Now, let's see what the * operator does:").move_to(3 * UP)
        ))

        pointer = Arrow(start=px_label.get_left(), end=x_label.get_right(), max_tip_length_to_length_ratio=0.1)
        self.play(GrowArrow(pointer))

        self.next_slide()

        self.play(FadeOut(VGroup(
            title, demo_code, x_rect, x_label, x_val, x_addr, px_rect, px_label, px_val, px_addr, pointer
        )))

        self.next_slide()


def generate_memory_box(label: str, value: str, addr: str, position=None,
                        font_size=22) -> Tuple[Square, Text, Text, Tex]:
    memory_box = Square(1)
    if position is not None:  # yes, the 'is not None` is required
        memory_box.move_to(position)

    box_label = Text(label, font_size=font_size).move_to(memory_box.get_top() + (0.2 * UP))
    box_val = Text(value, font_size=font_size).move_to(memory_box.get_center())
    box_addr = Tex(f"\\texttt{addr}", font_size=font_size).move_to(memory_box.get_bottom() + (0.2 * DOWN))

    return memory_box, box_label, box_val, box_addr


if __name__ == "__main__":
    import subprocess

    subprocess.run(["./run.sh"])
