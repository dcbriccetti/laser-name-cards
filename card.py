from dataclasses import dataclass
from typing import Iterator

from geometry import Geometry

@dataclass
class Card:
    x: str
    y: str
    name: str

    @classmethod
    def create_cards(cls, names: list[str], geom: Geometry) -> Iterator:
        for i, name in enumerate(names):
            row, col = divmod(i, geom.num_cards_per_line)
            x = col * geom.card_width  + geom.half_card_width
            y = row * geom.card_height + geom.half_card_height
            yield Card(f'{x:.2f}mm', f'{y:.2f}mm', name)

