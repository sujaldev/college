# Markdown Test

I recently [discovered](https://caolan.uk/notes/2022-05-13_serving_markdown_direct_from_apache.cm) that apache can serve
markdown files directly as html by calling an external process using the `mod_ext_filter`. This sounds *quite*
convenient, so I'm writing a python script to serve the purpose of this external program and have the generated html
match the same theme as the rest of the website. Maybe even add latex support later if I need it (I doubt I will but
nice to have anyway). This document serves the purpose of testing various markdown features.

## Tables

Let's see if tables work:

|   Day    |   Date    |        Course         |
|:--------:|:---------:|:---------------------:|
| Thursday |  04 Jan   |      Programming      |
|  Friday  |  05 Jan   |      Study Leave      | 
| Saturday |  06 Jan   |  Electrical Science   | 
| Sun-Mon  | 07-08 Jan |    **Study Leave**    | 
| Tuesday  |  09 Jan   | Engineering Mechanics |

## Checkboxes

- [x] Physics viva
- [ ] **Maths viva**
- [ ] R practical file/viva (?)
- [ ] Python practical file/viva (?)
- [ ] Manufacturing presentation
- [ ] Communication classwork submission

## Miscellaneous

Blockquotes:

> Square buildings have more space and are easier to navigate,
> all an arc shape building gets you are bragging rights.

Code:

```{python}
import something

print("Hello, World!")
```