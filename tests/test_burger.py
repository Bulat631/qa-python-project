import pytest
from praktikum.burger import Burger
from unittest.mock import Mock 

class TestBurger:
    def test_burger_set_buns(self, burger):
        mock_bun = Mock()
        mock_bun.name = 'ржанная'
        mock_bun.price = 50
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_burger_add_ingredient(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.type = 'Начинка'
        mock_ingredient.name = 'Лук'
        mock_ingredient.price = 10

        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_burger_remove_ingredient(self, burger):
        mock_ingredient1 = Mock()
        mock_ingredient1.type = 'Начинка'
        mock_ingredient1.name = 'Лук'
        mock_ingredient1.price = 10
        burger.add_ingredient(mock_ingredient1)

        mock_ingredient2 = Mock()
        mock_ingredient2.type = 'Соус'
        mock_ingredient2.name = 'Сосиска'
        mock_ingredient2.price = 20
        burger.add_ingredient(mock_ingredient2)

        burger.remove_ingredient(1)
        assert burger.ingredients == [mock_ingredient1]

    def test_burger_move_ingredient(self, burger):
        mock_ingredient1 = Mock()
        mock_ingredient1.type = 'Начинка'
        mock_ingredient1.name = 'Лук'
        mock_ingredient1.price = 10
        burger.add_ingredient(mock_ingredient1)

        mock_ingredient2 = Mock()
        mock_ingredient2.type = 'Соус'
        mock_ingredient2.name = 'Сосиска'
        mock_ingredient2.price = 20
        burger.add_ingredient(mock_ingredient2)

        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_ingredient2

    def test_burger_get_price(self, burger):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 20
        burger.bun = mock_bun

        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 40

        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 30

        burger.ingredients = [mock_ingredient1, mock_ingredient2]

        assert burger.get_price() == 110

    def test_burger_get_receipt(self, burger):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Ржанная'
        mock_bun.get_price.return_value = 20
        burger.bun = mock_bun

        mock_ingredient1 = Mock()
        mock_ingredient1.get_type.return_value = 'Начинка'
        mock_ingredient1.get_name.return_value = 'сосиска'
        mock_ingredient1.get_price.return_value = 40

        mock_ingredient2 = Mock()
        mock_ingredient2.get_type.return_value = 'Соус'
        mock_ingredient2.get_name.return_value = 'какой-то'
        mock_ingredient2.get_price.return_value = 30

        burger.ingredients = [mock_ingredient1, mock_ingredient2]
    

        assert burger.get_receipt() == '\n'.join(['(==== Ржанная ====)', '= начинка сосиска =', '= соус какой-то =', '(==== Ржанная ====)\n', 'Price: 110'])


