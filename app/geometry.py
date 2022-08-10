from dataclasses import dataclass, field

@dataclass
class Geometry:
    'Hold project geometry. All units are mm except where stated otherwise.'

    piece_width: float
    piece_height: float
    num_cards_per_line: int
    card_height: int
    font_size: int
    corner_radius: int

    half_card_height: int  = field(init=False)
    card_width: float      = field(init=False)
    half_card_width: float = field(init=False)

    def __post_init__(self) -> None:
        self.half_card_height = self.card_height // 2
        self.card_width       = self.piece_width / self.num_cards_per_line
        self.half_card_width  = self.card_width / 2

    @classmethod
    def from_form(cls, form: dict):
        'Extract string data from form, convert to int or float as needed and return a new Geometry object'

        number = int | float

        def get_numeric_value(name: str) -> number:
            'Given a form element name, find the expected type (int, float) and convert the string value to that type'

            field_type = fields[name].type  # int or float
            return field_type(form[name])

        def make_geometry_constructor_args() -> dict[str, number]:
            form_variable_names = [name for name, f in fields.items() if f.init]

            return {
                name: get_numeric_value(name)
                for name in form_variable_names
            }

        fields = Geometry.__dataclass_fields__
        return Geometry(**make_geometry_constructor_args())
