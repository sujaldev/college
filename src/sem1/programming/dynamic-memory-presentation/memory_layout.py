from dataclasses import dataclass

from manim import *


@dataclass
class Layer:
    box: Rectangle
    text: Text | Tex

    @property
    def attrs(self):
        return self.box, self.text


class MemoryLayout:
    def __init__(self, height: int | float = 1, width: int | float = 3, font_size=20, origin=ORIGIN):
        self.height = height
        self.width = width
        self.font_size = font_size
        self.origin = origin

        self.outline = Rectangle(height=height * 5, width=width).move_to(origin)
        self.code = self.init_box("Code", self.outline.get_bottom())
        self.data = self.init_box("Data", self.code.box.get_top())
        self.heap = self.init_box("Heap", self.data.box.get_top())
        self.stack = self.init_box("Stack", self.heap.box.get_top() + UP)

    def generate_group(self) -> VGroup:
        return VGroup(
            *self.code.attrs,
            *self.data.attrs,
            *self.heap.attrs,
            *self.stack.attrs,
            self.outline
        )

    def init_box(self, text: str, location=None) -> Layer:
        layer = Layer(Rectangle(height=self.height, width=self.width), Text(text, font_size=self.font_size))
        if location is not None:
            layer.box = layer.box.move_to(location + (0.5 * layer.box.height * UP))
            layer.text.move_to(layer.box.get_center())
        return layer
