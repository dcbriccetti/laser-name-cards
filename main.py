from math import ceil
from typing import Iterator
from flask import Flask, render_template, Response, request

from geometry import Geometry

Card = tuple[str, str, str]       # x, y, name
Line = tuple[str, str, str, str]  # x1, y1, x2, y2

app = Flask('Laser Name Card Generator')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cards', methods=['POST'])
def cards():
    f = request.form
    geom = Geometry(piece_width=float(f['piece-width']), num_cards_per_line=int(f['num-cards-per-line']),
                    card_height=int(f['card-height']), font_size=int(f['font-size']))
    font_family = f['font-family']
    names: list[str] = f['names'].split()
    num_rows = int(ceil(len(names) / geom.num_cards_per_line))
    svg: str = render_template('cards.svg', cards=list(create_cards(names, geom)),
                               lines=create_lines(num_rows, geom), font_family=font_family, font_size=geom.font_size)
    write_svg_for_debugging(svg)
    return Response(svg, content_type='image/svg+xml')

def create_cards(names: list[str], geom: Geometry) -> Iterator[Card]:
    for i, name in enumerate(names):
        row = i // geom.num_cards_per_line
        col = i %  geom.num_cards_per_line
        x = col * geom.card_width  + geom.half_card_width
        y = row * geom.card_height + geom.half_card_height
        yield f'{x:.2f}mm', f'{y:.2f}mm', name

def create_lines(num_rows: int, geom: Geometry) -> list[Line]:
    horizontal_lines: list[Line] = [
        (
            '0',
            f'{y * geom.card_height}mm',
            f'{geom.piece_width}mm',
            f'{y * geom.card_height}mm'
        )
        for y in range(num_rows + 1)
    ]
    vertical_lines: list[Line] = [
        (
            f'{x * geom.card_width}mm',
            '0',
            f'{x * geom.card_width}mm',
            f'{num_rows * geom.card_height}mm'
        )
        for x in range(geom.num_cards_per_line + 1)
    ]
    return vertical_lines + horizontal_lines

def write_svg_for_debugging(svg):
    with open('output.svg', 'w') as f:
        f.write(svg)

app.run(debug=True)
