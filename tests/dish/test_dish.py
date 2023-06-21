from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


def test_dish():
    # Teste de inicialização do prato e propriedades básicas
    churrasco = Dish("churrasco", 25.5)
    arroz = Dish("arroz", 15.0)
    assert churrasco.name == "churrasco"
    assert churrasco == churrasco
    assert churrasco != arroz
   
    assert hash(churrasco) != hash(arroz)
    assert hash(churrasco) == hash(churrasco)
   
    assert repr(churrasco) == "Dish('churrasco', R$25.50)"
   
    with pytest.raises(TypeError):
        Dish("churrasco", "25.5")
    with pytest.raises(ValueError):
        Dish("churrasco", -1.0)
    
    ingr1 = Ingredient("queijo mussarela")
    churrasco.add_ingredient_dependency(ingr1, 5)  
    assert churrasco.recipe.get(ingr1) == 5

    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert churrasco.get_restrictions() == expected_restrictions

    # Teste de ingredientes
    expected_ingredients = {ingr1}
    assert churrasco.get_ingredients() == expected_ingredients
