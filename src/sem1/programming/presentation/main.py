from typing import Tuple

from manim import *
# noinspection PyUnresolvedReferences
from manim_slides import Slide

config.background_color = "#101216"


class Main(Slide):
    def construct(self):
        self.intro()
        self.pointers()
        self.call_by_value()

    def intro(self):
        title = Tex(
            r"\textbf{Call by Value and Call by Reference in C}\\[20pt]"
            r"A presentation by Sujal Singh"
        )
        self.play(Write(title))

        self.next_slide()

        self.play(Unwrite(title))

        self.next_slide()

    def pointers(self):
        title = Tex(r"First, let's see what the \& character does:").move_to(3 * UP)
        self.play(Write(title))

        demo_code = Code(code="int x = 2;\nint *px = &x;", insert_line_no=False, language="c").move_to(3 * LEFT)
        self.play(FadeIn(demo_code))

        self.next_slide()

        x_rect, x_label, x_val, x_addr, x_group = generate_memory_box("x", "2", "0x1000", 2.5 * RIGHT)
        self.play(Write(VGroup(x_rect, x_label, x_val, x_addr)))

        self.next_slide()

        px_rect, px_label, px_val, px_addr, px_group = generate_memory_box("px", "0x1000", "0x1100", 5 * RIGHT)
        self.play(Write(VGroup(px_rect, px_label, px_val, px_addr)))

        self.next_slide()

        self.play(Transform(
            title, Tex(r"Now, let's see what the * operator does:").move_to(3 * UP)
        ))

        pointer = Arrow(start=px_label.get_left(), end=x_label.get_right(), max_tip_length_to_length_ratio=0.1)
        self.play(GrowArrow(pointer))

        self.next_slide()

        self.play(FadeOut(VGroup(title, demo_code, x_group, px_group, pointer)))

        self.next_slide()

    def call_by_value(self):
        title = Tex(r"Now that we know that, let's look at\\how \textbf{call by value} works:").move_to(3 * UP)
        self.play(Write(title))

        demo_code = Code(code="""
void my_func(int a) {
    a = 22;
}

void main() {
    int x = 11;
    my_func(x);
}""", language="c").move_to(3 * LEFT)
        self.play(FadeIn(demo_code))

        self.next_slide()

        x_rect, x_label, x_val, x_addr, x_group = generate_memory_box("x", "11", "0x1000", 2.5 * RIGHT)
        self.play(AnimationGroup(Write(x_group), Indicate(demo_code.code[5])))

        self.next_slide()

        a_rect, a_label, a_val, a_addr, a_group = generate_memory_box("a", "11", "0x1100", 2.5 * RIGHT)
        self.play(AnimationGroup(
            FadeIn(a_label),
            FadeIn(a_addr),
            a_group.animate.move_to(5 * RIGHT),
            Indicate(demo_code.code[6]))
        )

        self.next_slide()

        self.play(AnimationGroup(
            Transform(a_val, Text("22", font_size=22).move_to(a_rect.get_center())),
            Indicate(demo_code.code[1])
        ))

        self.next_slide()

        self.play(Transform(
            title, Tex(
                r"As we can see, \textit{my\_func} function creates a new variable local \\"
                r"to its scope having the same value as the passed argument. \\"
                r"And so, changes to this variable do not reflect in \textit{x}"
            ).move_to(3 * UP)
        ))

        self.next_slide()

        self.play(Transform(
            title, Tex(
                r"But what if we wanted to change the value of \textit{x}?"
            ).move_to(3 * UP)
        ))

        self.next_slide()

        self.play(Transform(
            title, Tex(
                r"This is where \textbf{call by reference} comes into play."
            ).move_to(3 * UP)
        ))

        self.next_slide()

        self.play(Transform(
            title, Tex(
                r"It's important to point out that all function calls in \\"
                r"C pass arguments by value. But we can simulate call by \\"
                r"reference by using pointers!"
            ).move_to(3 * UP)
        ))

        self.next_slide()

        self.play(Transform(
            title,
            Tex(
                r"Let's see how. We change our function call statement and \\"
                r"function declaration a bit to use pointers instead:"
            ).move_to(3 * UP)
        ))

        self.play(Transform(demo_code, Code(code="""
void my_func(int *a) {
    *a = 22;
}

void main() {
    int x = 11;
    my_func(&x);
}""", language="c").move_to(3 * LEFT)))

        self.next_slide()

        pointer = Arrow(start=a_label.get_left(), end=x_label.get_right(), max_tip_length_to_length_ratio=0.1)
        self.play(AnimationGroup(
            Transform(a_val, Tex(r"\texttt{0x1000}", font_size=22).move_to(a_rect.get_center())),
            GrowArrow(pointer)
        ))

        self.next_slide()

        self.play(AnimationGroup(
            Transform(x_val, Text("22", font_size=22).move_to(x_rect.get_center())),
            Indicate(demo_code.code[1])
        ))

        self.next_slide()

        self.play(Transform(
            title,
            Tex(r"Calling \textit{my\_func} now causes the value of \textit{x} to also update.").move_to(3 * UP)
        ))

        self.next_slide()

        self.play(
            FadeOut(a_group, x_group, demo_code, pointer),
            Transform(title, Tex(r"Thank you for listening!").move_to(ORIGIN))
        )

        self.next_slide()


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
