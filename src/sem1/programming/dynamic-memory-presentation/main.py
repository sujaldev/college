from pathlib import Path

from memory_layout import MemoryLayout

from manim import *
# noinspection PyUnresolvedReferences
from manim_slides import Slide

config.background_color = "#101216"


class Main(Slide):
    def construct(self):
        self.intro()

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

if __name__ == "__main__":
    import subprocess

    subprocess.run(["./run.sh", "k"])
