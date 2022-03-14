import argparse
from hashlib import new
from sqlalchemy import desc

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

exercise_pattern = re.compile(r".*\*\*(Task[ \d]*|Question[ \d]*):(.*)\*\*")
exercise_replacement = '````{exercise} \\1\n\\2\n````'
solution_pattern = re.compile(r".*\*\*(?:Solution|Answer):(.*)\*\*")



def annotate_lines(lines):
    i = 0
    new_lines = []
    while i < len(lines):
        line = lines[i]
        m = re.match(solution_pattern, line)
        if m is not None:
            line = "`"*4 + "{solution}\n"
            new_lines.append(line)
            new_lines.extend(lines[i+1:-1])
            new_lines.append(lines[-1] + '\n')
            new_lines.append("`"*4)
            break
        else:
            m = re.match(exercise_pattern, line)
            if m is not None:
                line = re.sub(exercise_pattern, exercise_replacement, line)
            new_lines.append(line)
        i += 1

    return new_lines


def annotate_solutions(cells):
    # Since we might want to consume many cells, we use a while instead of foor loop
    i = 0
    annotated_cells = []
    while i < len(cells):
        cell = cells[i] 
        if cell['cell_type'] == 'markdown':
            lines = annotate_lines(cell['source'])
            cell['source'] = lines
        annotated_cells.append(cell)
        i += 1
    return annotated_cells
        


def main():
    parser = argparse.ArgumentParser(description="Convert embedding images as markdown directives to html img tags")    
    parser.add_argument('notebook_directory', help='Directory containing notebooks to convert', type=Path)
    
    args = parser.parse_args()

    notebooks = list(args.notebook_directory.glob('**/*.ipynb'))
    for notebook_path in notebooks:
        with open(notebook_path, encoding='utf8') as notebook_fp:
            notebook_json = json.load(notebook_fp)
        converted_cells = [convert_cell(cell) for cell in notebook_json['cells']]
        annotated_cells = annotate_solutions(converted_cells)
        
        notebook_json['cells'] = annotated_cells
        if 'widgets' in notebook_json['metadata']:
            del notebook_json['metadata']['widgets']


        #output_dir = args.notebook.parent / 'converted'
        #output_dir.mkdir(exist_ok=True)
        #output_file = output_dir / args.notebook.name
        with open(notebook_path, 'w') as fp:
            json.dump(notebook_json, fp)



if __name__ == '__main__':
    main()