import unittest
from src.stub_view_products import view_products
from src.BuyOrRent import add_to_cart
from src.ViewStock import select_item
from unittest.mock import patch

class MyTestCase(unittest.TestCase):
    #tests if the stub itself works
    def test_view_products(self):
        products = view_products(self)

        self.assertEqual(products, [
            [1, 'Beach Towel', 14, 14],
            [2, "Sunscreen SPF 50", 10, 20],
            [3, "Sunglasses", 5, 7],
            [4, "Beach Umbrella", 9, 3],
        ])



    @patch('builtins.input', side_effect="3")
    #using both mock and stub to test that an item from products can be selected
    def test_select_item(self, mock_input):
        products = view_products(self)
        selected_item = select_item(products)
        self.assertEqual(selected_item, [3, "Sunglasses", 5, 7])

        if __name__ == '__main__':
            unittest.main()

    #tests the adding to cart/price calc
    def test_add_to_cart(self):
        products = view_products(self)
        assert add_to_cart(cart=[],id=products[0][0],name=products[0][1],purchase_quantity=2,price=products[0][2],purchase_duration=2) == [[1, 'Beach Towel', 2, 2.0, 2]]


if __name__ == '__main__':
    unittest.main()

