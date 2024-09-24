from dataclasses import dataclass, asdict
from api.models.color_option_model import ColorOption
from typing import List
import json

@dataclass
class Palette:
    original_color: str
    color_options: List[ColorOption]

    def to_json(self):
        return json.dumps(asdict(self))
    
def palettes_to_json(palettes: List[Palette]):
    return json.dumps([asdict(palette) for palette in palettes])