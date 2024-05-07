# Markdown Renderer

I recently [discovered](https://caolan.uk/notes/2022-05-13_serving_markdown_direct_from_apache.cm) that apache can serve
markdown files directly as html by calling an external process using the `mod_ext_filter`. This sounds *quite*
convenient, so I'm writing a python script to serve the purpose of this external program such that the generated html
matches the same theme as the rest of the website. Maybe even add latex support later if I need it (I doubt I will but
nice to have anyway).

## Build

Set up a virtual environment with the dependencies in `requirements.txt` installed and build an executable with the
following:

```{bash}
cd utils/web/markdown
pyinstaller --onefile --name ipu-md --add-data=template.jinja2:. renderer.py
```

## Testing

This section consists of various markdown features to allow using this document as a test input to the rendering script.

### Tables

|   Day    |   Date    |        Course         |
|:--------:|:---------:|:---------------------:|
| Thursday |  04 Jan   |      Programming      |
|  Friday  |  05 Jan   |      Study Leave      | 
| Saturday |  06 Jan   |  Electrical Science   | 
| Sun-Mon  | 07-08 Jan |    **Study Leave**    | 
| Tuesday  |  09 Jan   | Engineering Mechanics |

### Checkboxes

- [x] Physics viva
- [ ] **Maths viva**
- [ ] R practical file/viva (?)
- [ ] Python practical file/viva (?)
- [ ] Manufacturing presentation
- [ ] Communication classwork submission

### Blockquotes

> Square buildings have more space and are easier to navigate, all an arc shape building gets you are bragging rights.
> *&ndash; probably not the architect of this building*

### Code

```{python}
import something

print("Hello, World!")
```