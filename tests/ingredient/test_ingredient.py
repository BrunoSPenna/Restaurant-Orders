
from src.models.ingredient import Ingredient, Restriction

# Req 1

def test_ingredient():
    bacon = Ingredient("bacon")
    bacon_2 = Ingredient("bacon")
    assert bacon == bacon_2

    bacon = Ingredient("bacon")
    bacon_2 = Ingredient("bacon")
    assert hash(bacon) == hash(bacon_2)

    bacon = Ingredient("bacon")
    queijo = Ingredient("queijo")
    assert not bacon == queijo

    bacon = Ingredient("bacon")
    queijo = Ingredient("queijo")
    assert hash(bacon) != hash(queijo)

    bacon = Ingredient("bacon")
    assert bacon.name == "bacon"

    bacon = Ingredient("bacon")
    assert repr(bacon) == "Ingredient('bacon')"

    bacon = Ingredient("bacon")
    bacon_restriction = {Restriction.ANIMAL_DERIVED, Restriction.ANIMAL_MEAT}
    assert bacon.restrictions == bacon_restriction
