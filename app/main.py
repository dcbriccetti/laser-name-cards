from flask import Flask, render_template, Response, request

from app.card import Card
from app.geometry import Geometry

app = Flask('Laser Name Card Generator')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cards', methods=['POST'])
def cards():
    form = request.form
    geometry = Geometry.from_form(form)
    names: list[str] = form['names'].split('\r\n')
    svg: str = render_template('cards.svg',
                               cards=list(Card.create_cards(names, geometry)),
                               font_family=form['font_family'],
                               geometry=geometry,
                               cut_stroke_width=form['cut_stroke_width'],
                               cut_stroke_color=form['cut_stroke_color'])
    write_svg_for_debugging(svg)
    return Response(svg, content_type='image/svg+xml')

def write_svg_for_debugging(svg):
    with open('output.svg', 'w') as f:
        f.write(svg)
