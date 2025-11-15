from enum import Enum
from .attack_acre_crop import AttackAcreCrop
from .attack_acre_sprout import AttackAcreSprout
from .attack_acre_seed import AttackAcreSeed
from .defender_acre import DefenderAcre
from .empty_acre import EmptyAcre

class CropType(Enum):
    defender = DefenderAcre
    empty = EmptyAcre
    seed = AttackAcreSeed
    sprout = AttackAcreSprout
    crop = AttackAcreCrop