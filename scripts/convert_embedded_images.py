import argparse
from sqlalchemy import desc

from sympy import arg
import re
from pathlib import Path
import json


# This horrible thing matches out the data image part and whatever name was in the brackets. It only supports
# png at the moment. The directive to look for is something along the line 
# of '![some random text](data:image/png;base64,...base64 encoded data...)'
# The first pattern \[([^\]]*)\] looks for the starting bracket and matches anything except 
# an end bracked to the first group.
# The second group catches the data. Base64 can contain any characted between A-Z, a-z, 0-9, +, /. 
# The equals sign is used to bad incomplete quartets and should also be matched.
full_pattern = r'\!\[([^\]]*)\]\((data:image/png;base64,[A-Za-z0-9+/=]*)\)'
compiled_pattern = re.compile(full_pattern)
replacement = r'<img src="\2" alt="\1">'
def convert_line(line):
    converted_line = re.sub(compiled_pattern, replacement, line)
    
    return converted_line

def convert_cell(cell):
    if cell['cell_type'] == 'markdown':
        converted_source = [convert_line(line) for line in cell['source']]
        cell['source'] = converted_source
    return cell

def main():
    parser = argparse.ArgumentParser(description="Convert embedding images as markdown directives to html img tags")    
    parser.add_argument('notebook_directory', help='Directory containing notebooks to convert', type=Path)
    
    args = parser.parse_args()

    notebooks = list(args.notebook_directory.glob('**/*.ipynb'))
    for notebook_path in notebooks:
        with open(notebook_path, encoding='utf8') as notebook_fp:
            notebook_json = json.load(notebook_fp)
        converted_cells = [convert_cell(cell) for cell in notebook_json['cells']]
        notebook_json['cells'] = converted_cells
        if 'widgets' in notebook_json['metadata']:
            del notebook_json['metadata']['widgets']
        #output_dir = args.notebook.parent / 'converted'
        #output_dir.mkdir(exist_ok=True)
        #output_file = output_dir / args.notebook.name
        with open(notebook_path, 'w') as fp:
            json.dump(notebook_json, fp)



if __name__ == '__main__':
    main()