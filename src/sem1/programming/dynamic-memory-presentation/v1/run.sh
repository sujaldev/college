#!/usr/bin/bash


source ../../../../../venv/bin/activate
cd build/
manim -q${1:-l} ../main.py Main
manim-slides convert Main slides.html
