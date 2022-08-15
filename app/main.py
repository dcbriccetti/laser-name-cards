from flask import Flask, render_template, Response, request

from app.card import Card
from app.geometry import Geometry
from app.fonts import family_names, default_family_name
from app.names import random_names

app = Flask('Laser Name Card Generator')

@app.route('/')
def index():
    return render_template('index.html', font_family_names=family_names, default_font=default_family_name,
                           sample_names=random_names(24))

@app.route('/cards', methods=['POST'])
def create_cards_svg():
    form = request.form
    geometry = Geometry.from_form(form)
    keys: list[str] = 'font_family text_stroke_color text_fill_color cut_stroke_width cut_stroke_color'.split()
    options = {k: v for k, v in form.items() if k in keys}  # Copy what we need from the form
    if 'bigger_preview_stroke' in form and 'preview' in request.args:
        options['cut_stroke_width'] = '1pt'
    cards = list(Card.create_cards(form['names'].split('\r\n'), geometry))
    svg: str = render_template('cards.svg',
                               preview='preview' in request.args,
                               cards=cards,
                               geometry=geometry,
                               **options)
    return Response(svg, content_type='image/svg+xml')
