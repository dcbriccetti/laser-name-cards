from dataclasses import dataclass, field, Field

@dataclass
class Geometry:
    'Hold project geometry. All units are mm except where stated otherwise.'

    piece_width: float
    num_cards_per_line: int
    card_height: int
    font_size: int
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

        def field_to_variable(name: str) -> str:
            'Replace hyphens in form element names with underscores to make Python variable names'

            return name.replace('-', '_')

        def get_numeric_value(name: str) -> int | float:
            'Given a form element name, find the expected type (int, float) and convert the string value to that type'

            variable_name: str = field_to_variable(name)
            variable_string_value: str = form[name]
            dataclass_field: Field = Geometry.__dataclass_fields__[variable_name]
            field_type = dataclass_field.type  # int or float
            numeric_value: int | float = field_type(variable_string_value)
            return numeric_value

        form_element_names = 'piece-width num-cards-per-line card-height font-size'.split()

        args: dict[str, any] = {
            field_to_variable(name): get_numeric_value(name)
            for name in form_element_names
        }

        return Geometry(**args)
