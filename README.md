# Create printable HTML flashcards

Your teacher gave you learning material in form of a CSV file, but you prefer to learn with physical flashcards? This package can create a printable HTML file for you!

Currently, this package only works with a very specific format. Each entry of the input list has to look like this:
```
[
    'Flashcard Front Text', 
    'Flashcard Back Text Row 1', 
    'Flashcard Back Text Row 2', 
    'Flashcard Back Text Row 3', 
    [
        'Flashcard Back Text Row n',
        ...
    ]
]
```

I might make this package more generic, if interest arises.