# Власні помилки гри. Усі вони успадковуються від GameError,
# тому їх можна ловити разом: except GameError.


class GameError(Exception):
    """Базова помилка гри."""


class InventoryFullError(GameError):
    """В інвентарі немає місця."""


class ItemNotFoundError(GameError):
    """Предмета немає в інвентарі (або його замало)."""


class NotEnoughIngredientsError(GameError):
    """Не вистачає інгредієнтів для рецепта."""


class InvalidChoiceError(GameError):
    """Гравець зробив некоректний вибір."""
