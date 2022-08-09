from math import ceil

from flask import Flask, render_template, Response, request

from card import Card
from geometry import Geometry
from line import Line

app = Flask('Laser Name Card Generator')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cards', methods=['POST'])
def cards():
    geom = Geometry.from_form(request.form)
    names = request.form['names'].split('\r\n')
    num_rows = int(ceil(len(names) / geom.num_cards_per_line))
    svg: str = render_template('cards.svg',
                               cards=Card.create_cards(names, geom),
                               lines=Line.create_lines(num_rows, geom),
                               font_family=request.form['font_family'],
                               font_size=geom.font_size)
    write_svg_for_debugging(svg)
    return Response(svg, content_type='image/svg+xml')

def write_svg_for_debugging(svg):
    with open('output.svg', 'w') as f:
        f.write(svg)

app.run(debug=True)
