class Geometry:
    # All units are mm except where stated otherwise
    piece_width: float
    num_cards_per_line: int
    card_height: int
    font_size: int
    half_card_height: int
    card_width: float
    half_card_width: float

    def __init__(self, piece_width: float, num_cards_per_line: int, card_height: int, font_size: int) -> None:
        self.piece_width = piece_width
        self.num_cards_per_line = num_cards_per_line
        self.card_height = card_height
        self.font_size = font_size
        self.half_card_height = card_height // 2
        self.card_width = piece_width / num_cards_per_line
        self.half_card_width = self.card_width / 2
