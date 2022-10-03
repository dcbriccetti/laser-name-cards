from dataclasses import dataclass
from typing import Iterator

from app.geometry import Geometry

@dataclass
class Card:
    x: int
    y: int
    name: str

    @classmethod
    def create_cards(cls, names: list[str], geom: Geometry) -> Iterator:
        for i, name in enumerate(names):
            row, col = divmod(i, geom.num_cards_per_line)
            x = geom.piece_margin + col * geom.card_width  + geom.half_card_width
            y = geom.piece_margin + row * geom.card_height + geom.half_card_height
            yield Card(x, y, name)
