from manim import *
# noinspection PyUnresolvedReferences
from manim_slides import Slide

config.background_color = "#101216"


class Main(Slide):
    def construct(self):
        self.intro()
        self.address_of_operator()

    def intro(self):
        title = Tex(
            r"\textbf{Call by Value and Call by Reference in C}\\[20pt]"
            r"A video presentation by Sujal Singh"
        )
        self.play(Write(title))

        self.next_slide()

        self.play(Unwrite(title))


if __name__ == "__main__":
    import subprocess

    subprocess.run(["./run.sh"])
