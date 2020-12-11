import random

import flashburner


def run():
    """
    Generate an HTML file with a random amount of flashcards (up to 2 full pages).
    """
    test_list = []
    for i in range(random.randint(1, 24)):
        test_list.append([
            f'Card {i}',
            f'Card {i} Backside Information',
            f'Card {i} Backside Second Information',
            f'Card {i} Backside Third Information',
            f'Card {i} Backside Multiline 1\nBackside Multiline 2\nBackside Multiline 3\nBackside Multiline 4'
        ])

    result = flashburner.build_flashcards(test_list)
    with open("target.html", "w") as fh:
        fh.write(result)


if __name__ == '__main__':
    run()
