from jinja2 import Environment, PackageLoader, select_autoescape
import csv

collection = []
with open('data/semester_1_clean.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    chunk = {
        'front_rows': [],
        'back_rows': []
    }
    front_cells = []
    back_cells = []
    for row in csv_reader:
        front_cells.append(row[0])
        back_cells.append(
            {
                'on': row[1],
                'kun': row[2],
                'meaning': row[3],
                'vocabulary': row[4].split('|')
            }
        )

        if len(front_cells) == 3:
            chunk['front_rows'].append(front_cells)
            back_cells.reverse()
            chunk['back_rows'].append(back_cells)
            front_cells = []
            back_cells = []

        if len(chunk['front_rows']) == 4:
            collection.append(chunk)
            chunk = {
                'front_rows': [],
                'back_rows': []
            }

    # remaining cells are appended with placeholders, then added to chunk as usual.
    cell_count = len(front_cells)
    if cell_count == 1:
        front_cells.append('')
        front_cells.append('')
        chunk['front_rows'].append(front_cells)
        back_cells.append('')
        back_cells.append('')
        back_cells.reverse()
        chunk['back_rows'].append(back_cells)
    elif cell_count == 2:
        front_cells.append('')
        chunk['front_rows'].append(front_cells)
        back_cells.append('')
        back_cells.reverse()
        chunk['back_rows'].append(back_cells)

    chunk_size = len(chunk['front_rows'])
    if chunk_size > 0:
        for x in range(4 - chunk_size):
            chunk['front_rows'].append(['', '', ''])
            chunk['back_rows'].append([[], [], []])
        collection.append(chunk)

env = Environment(
    loader=PackageLoader('flashcards', 'templates'),
    autoescape=select_autoescape(['html'])
)

template = env.get_template('template.html')
rendered = template.render(collection=collection)
with open("flashcards/templates/rendered.html", "w") as fh:
    fh.write(rendered)
