from jinja2 import Environment, PackageLoader, select_autoescape
import csv

with open('data/semester_1_clean.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    # this hold the full flashcard data.
    collection = []
    # this hold the data of one double-sided page.
    chunk = {
        'front_rows': [],
        'back_rows': []
    }
    # these two hold data for one row of a double-sided page.
    front_cells = []
    back_cells = []
    for row in csv_reader:
        # data is gathered from the csv.
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
            # when we have enough data for one row  of a page, we add it to the chunks.
            # we have to do it like this, because the back rows have to be reversed to line up with the front side.
            chunk['front_rows'].append(front_cells)
            back_cells.reverse()
            chunk['back_rows'].append(back_cells)
            front_cells = []
            back_cells = []

        if len(chunk['front_rows']) == 4:
            # when we have enough data for one double-side page, we add it to the full collection.
            collection.append(chunk)
            chunk = {
                'front_rows': [],
                'back_rows': []
            }

    # the final page might not be filled completely. we have to add placeholders for everything to line up properly.
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
with open("data/target.html", "w") as fh:
    fh.write(rendered)
