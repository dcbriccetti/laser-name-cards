from dataclasses import dataclass

from geometry import Geometry

@dataclass
class Line:
    x1: str
    y1: str
    x2: str
    y2: str

    @classmethod
    def create_lines(cls, num_rows: int, geom: Geometry) -> list:
        horizontal_lines: list[Line] = [
            Line(
                '0',
                f'{y * geom.card_height}mm',
                f'{geom.piece_width}mm',
                f'{y * geom.card_height}mm'
            )
            for y in range(num_rows + 1)
        ]
        vertical_lines: list[Line] = [
            Line(
                f'{x * geom.card_width}mm',
                '0',
                f'{x * geom.card_width}mm',
                f'{num_rows * geom.card_height}mm'
            )
            for x in range(geom.num_cards_per_line + 1)
        ]
        return vertical_lines + horizontal_lines
