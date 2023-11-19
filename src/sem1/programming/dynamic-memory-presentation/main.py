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
        self.dynamic_memory_allocation()

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

    def dynamic_memory_allocation(self):
        title = Tex(r"\textbf{Dynamic Memory Allocation}").move_to((3 * LEFT) + (3.5 * UP))
        text_size = 30
        text = Tex(
            r"\begin{flushleft}"
            r"It allows a program to dynamically request memory from the operating system at runtime. The standard "
            r"library in C provides a few functions to be able to perform dynamic memory allocation. These are listed "
            r"below along with suitable mnemonics."
            r"\begin{itemize}"
            r"\item \textbf{\textit{malloc()}} \hfill \parbox{160pt}{(memory allocate)}"
            r"\item \textbf{\textit{calloc()}} \hfill \parbox{160pt}{(clear allocate)}"
            r"\item \textbf{\textit{realloc()}} \hfill \parbox{160pt}{(re-allocate)}"
            r"\item \textbf{\textit{free()}}"
            r"\end{itemize}"
            r"\end{flushleft}",
            font_size=text_size
        ).move_to((1.275 * LEFT) + UP)
        self.play(Write(title), Write(text))

        self.next_slide()

        new_text = Tex(
            r"\begin{flushleft}"
            r"Allocates a specified number of contiguous bytes and returns a void pointer to the first byte."
            r"\end{flushleft}",
            font_size=text_size
        ).move_to((1.275 * LEFT) + (2.75 * UP))

        demo_code = (Code(code="int *ptr = (int*) malloc(2 * sizeof(int));", language="c", insert_line_no=False)
                     .move_to(1.5 * UP))

        ptr_box, ptr_label, ptr_val, ptr_addr, ptr_group = generate_memory_box("ptr", "0x2000", "0x1000")
        heap_box = Rectangle(width=4, height=4).move_to((3 * RIGHT) + (1.5 * DOWN))
        heap_label = Tex("Heap", font_size=text_size).move_to(heap_box.get_top() + (0.2 * UP))

        allocated_address = Tex(r"\texttt{0x2000}", font_size=text_size).move_to(heap_box.get_top() + (0.4 * DOWN))
        ptr_group.move_to(allocated_address.get_bottom() + (6 * LEFT) + (0.6 * DOWN))
        arrow = Arrow(
            start=ptr_label.get_right(), end=allocated_address.get_left(),
            max_tip_length_to_length_ratio=0.05
        )

        block1 = Rectangle(width=2, height=1).move_to(allocated_address.get_bottom() + (0.8 * DOWN))
        b1_text = Tex(r"10110101", font_size=text_size).move_to(block1.get_center())
        block2 = Rectangle(width=2, height=1).move_to(block1.get_bottom() + (0.5 * DOWN))
        b2_text = Tex(r"01101010", font_size=text_size).move_to(block2.get_center())

        self.play(
            Transform(title, Tex(r"\textbf{\textit{malloc()}}").move_to((5.5 * LEFT) + (3.5 * UP))),
            Transform(text, new_text),
        )
        self.play(Write(VGroup(
            demo_code, ptr_group, heap_box, heap_label, allocated_address
        )))
        self.play(Write(VGroup(
            block1, b1_text,
            block2, b2_text
        )))
        self.play(GrowArrow(arrow))

        self.next_slide()

        new_text = Tex(
            r"\begin{flushleft}"
            r"Similar to \texttt{malloc()} but ensures that the initialized values are zero."
            r"\end{flushleft}",
            font_size=text_size
        ).move_to((1.8 * LEFT) + (2.75 * UP))

        new_code = (Code(code="int *ptr = (int*) calloc(2, sizeof(int));", language="c", insert_line_no=False)
                    .move_to(1.5 * UP))

        new_b1 = Tex(r"00000000", font_size=text_size).move_to(block1.get_center())
        new_b2 = Tex(r"00000000", font_size=text_size).move_to(block2.get_center())
        self.play(
            Transform(title, Tex(r"\textbf{\textit{calloc()}}").move_to((5.5 * LEFT) + (3.5 * UP))),
            Transform(text, new_text),
            Transform(demo_code, new_code),
            Transform(b1_text, new_b1),
            Transform(b2_text, new_b2),
        )

        self.next_slide()

        new_text = Tex(
            r"\begin{flushleft}"
            r"Used to resize a memory area already created by \texttt{malloc()} or \texttt{calloc()}. If enough space "
            r"isn't available, it will copy the existing data onto a new location where more space is available."
            r"\end{flushleft}",
            font_size=text_size
        ).move_to((1.275 * LEFT) + (2.6 * UP))

        new_code = Code(
            code="int *new_ptr = (int*) realloc(ptr, sizeof(int) * 3);", language="c", insert_line_no=False
        ).move_to(1.5 * UP)

        block3 = Rectangle(width=2, height=1).move_to(block2.get_bottom() + (0.5 * DOWN))
        b3_text = Tex(r"01101010", font_size=text_size).move_to(block3.get_center())
        self.play(
            Transform(title, Tex(r"\textbf{\textit{realloc()}}").move_to((5.48 * LEFT) + (3.5 * UP))),
            Transform(text, new_text),
            Transform(demo_code, new_code),
            Transform(ptr_label, Text("new_ptr", font_size=18).move_to(ptr_box.get_top() + (0.2 * UP))),
            Write(VGroup(block3, b3_text)),
        )

        self.next_slide()

        new_text = Tex(
            r"\begin{flushleft}"
            r"Used to free up memory, as in to mark it available for use in further dynamic memory allocation calls."
            r"\end{flushleft}",
            font_size=text_size
        ).move_to((1.275 * LEFT) + (2.6 * UP))

        new_code = Code(code="free(ptr);", language="c", insert_line_no=False).move_to(1.5 * UP)

        self.play(
            Transform(title, Tex(r"\textbf{\textit{free()}}").move_to((5.75 * LEFT) + (3.5 * UP))),
            Transform(text, new_text),
            Transform(demo_code, new_code),
            FadeOut(VGroup(
                ptr_group, arrow, heap_label, heap_box, allocated_address,
                block1, b1_text,
                block2, b2_text,
                block3, b3_text,
            )),
        )

        self.next_slide()

        self.play(FadeOut(VGroup(title, text, demo_code)))

        self.play(Write(end := Tex(r"\textbf{\LARGE Thank you for listening!}")))

        self.next_slide()

        self.play(FadeOut(end))


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
