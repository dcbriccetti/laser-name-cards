from math import ceil
from typing import Iterator
from flask import Flask, render_template, Response, request

Card = tuple[str, str, str]       # x, y, name
Line = tuple[str, str, str, str]  # x1, y1, x2, y2

# All units are mm except where explicitly stated
BED_WIDTH = 609.6  # (24″)
NUM_CARDS_PER_LINE = 5
CARD_WIDTH = BED_WIDTH / NUM_CARDS_PER_LINE
HALF_CARD_WIDTH = CARD_WIDTH / 2
CARD_HEIGHT = 40
HALF_CARD_HEIGHT = CARD_HEIGHT / 2

app = Flask('Laser Name Card Generator')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cards', methods=['POST'])
def cards():
    names: list[str] = request.form['names'].split()
    font = request.form['font']
    num_rows = int(ceil(len(names) / NUM_CARDS_PER_LINE))
    svg: str = render_template('cards.svg', cards=list(create_cards(names)), lines=create_lines(num_rows), font=font)
    write_svg_for_debugging(svg)
    return Response(svg, content_type='image/svg+xml')  # todo get content type header working

def create_cards(names: list[str]) -> Iterator[Card]:
    for i, name in enumerate(names):
        row = i // NUM_CARDS_PER_LINE
        col = i %  NUM_CARDS_PER_LINE
        x = col * CARD_WIDTH + HALF_CARD_WIDTH
        y = row * CARD_HEIGHT + HALF_CARD_HEIGHT
        yield f'{x:.2f}mm', f'{y:.2f}mm', name

def create_lines(num_rows: int) -> list[Line]:
    horizontal_lines = [
        (
            '0',
            f'{y * CARD_HEIGHT}mm',
            f'{BED_WIDTH}mm',
            f'{y * CARD_HEIGHT}mm'
        )
        for y in range(num_rows + 1)
    ]
    vertical_lines = [
        (
            f'{x * CARD_WIDTH}mm',
            '0',
            f'{x * CARD_WIDTH}mm',
            f'{num_rows * CARD_HEIGHT}mm'
        )
        for x in range(NUM_CARDS_PER_LINE + 1)
    ]
    return vertical_lines + horizontal_lines

def write_svg_for_debugging(svg):
    with open('output.svg', 'w') as f:
        f.write(svg)

app.run(debug=True)
