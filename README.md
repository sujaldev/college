# College

A repository for college related stuff and the tools to manage them.

## C Programming Practical File

<img align=right alt="c practical preview" width=300px src="https://github.com/sujaldev/college/assets/75830554/d57be35a-a7a1-44a5-8f86-8c954e21cba4">

The practical file is automatically generated from the programs organized in the `src/c-practical` directory, $\LaTeX$
is used to typeset the document with a custom document class `tools/pdf/template/ipu-c.cls`. The generated PDF will be
automatically published [here](https://ipu.sujal.dev/replace/when/website/is/done).

The generated $\TeX$ files are stored in a separate orphan branch `pdf`, the reason to track automatically generated
files is to be able to go in and make manual changes for unforeseen circumstances.

Every program should begin with a comment declaring the question it answers, the comment can also specify an optional
$\LaTeX$ representation like in the following example (multiple single-line comments may also be used).

```c
/*
Program to print "Hello, World!".
%latex%
Program to print ``Hello, World!''.
*/
```