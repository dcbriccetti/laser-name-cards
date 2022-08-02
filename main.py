from math import ceil
from typing import Iterator
from flask import Flask, render_template, Response, request

Card = tuple[str, str, str]

# All units are mm except where explicitly stated
BED_WIDTH = 609.6  # (24″)
NUM_CARDS_PER_LINE = 5
CARD_WIDTH = BED_WIDTH / NUM_CARDS_PER_LINE
HALF_CARD_WIDTH = CARD_WIDTH / 2
CARD_HEIGHT = 40
HALF_CARD_HEIGHT = CARD_HEIGHT / 2
HALF_TEXT_HEIGHT = 7  # For vertical centering.  Todo Calculate this from the font size.

app = Flask('Laser Name Card Generator')

def create_cards(names: list[str]) -> Iterator[Card]:
    for i, name in enumerate(names):
        row = i // NUM_CARDS_PER_LINE
        col = i % NUM_CARDS_PER_LINE
        yield f'{col * CARD_WIDTH + HALF_CARD_WIDTH:.2f}mm', \
              f'{row * CARD_HEIGHT + HALF_CARD_HEIGHT + HALF_TEXT_HEIGHT:.2f}mm', name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cards', methods=['POST'])
def cards():
    names = request.form['names'].split()
    cards = list(create_cards(names))
    num_rows = int(ceil(len(cards) / NUM_CARDS_PER_LINE))
    horz_lines = [
        (
            '0',
            f'{y * CARD_HEIGHT}mm',
            f'{BED_WIDTH}mm',
            f'{y * CARD_HEIGHT}mm'
        )
        for y in range(num_rows + 1)
    ]
    vert_lines = [
        (
            f'{x * CARD_WIDTH}mm',
            '0',
            f'{x * CARD_WIDTH}mm',
            f'{num_rows * CARD_HEIGHT}mm'
        )
        for x in range(NUM_CARDS_PER_LINE + 1)
    ]
    svg: str = render_template('cards.svg', cards=cards, lines=vert_lines + horz_lines)
    write_svg_for_debugging(svg)
    return Response(svg, content_type='image/svg+xml')  # todo get content type header working

def write_svg_for_debugging(svg):
    with open('output.svg', 'w') as f:
        f.write(svg)

app.run(debug=True)
