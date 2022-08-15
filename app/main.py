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
def cards():
    form = request.form
    geometry = Geometry.from_form(form)
    names: list[str] = form['names'].split('\r\n')
    bigger_cut_stroke: bool = 'bigger_preview_stroke' in form and 'preview' in request.args
    cut_stroke_width = '1pt' if bigger_cut_stroke else form['cut_stroke_width']
    svg: str = render_template('cards.svg',
                               cards            =list(Card.create_cards(names, geometry)),
                               font_family      =form['font_family'],
                               text_stroke_color=form['text_stroke_color'],
                               text_fill_color  =form['text_fill_color'],
                               geometry         =geometry,
                               cut_stroke_width =cut_stroke_width,
                               cut_stroke_color =form['cut_stroke_color'],
                               preview          ='preview' in request.args)
    return Response(svg, content_type='image/svg+xml')
