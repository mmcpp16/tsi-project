import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from views.OwnerView import owner_main

class TestOwnerView(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_owner_main_view_products(self, mock_input):
        with patch('views.OwnerView.view_products', MagicMock()) as mock_view_products:
            owner_main()
            self.assertTrue(mock_view_products.called)

    @patch('builtins.input', side_effect=['2'])
    def test_owner_main_view_orders(self, mock_input):
        with patch('views.OwnerView.view_order', MagicMock()) as mock_view_order:
            owner_main()
            self.assertTrue(mock_view_order.called)

    @patch('builtins.input', side_effect=['1', '1', '1'])
    def test_owner_main_product_set_quantity(self, mock_input):
        try:
            with patch('sys.stdout', new=StringIO()) as output:
                owner_main()
        except StopIteration:
            # Since we constantly ask for user input all side effects get consumed and this error gets thrown
            self.assertIn("Product has been updated.", output.getvalue())

    @patch('builtins.input', side_effect=['2'])
    def test_owner_main_view_order(self, mock_input):
        try:
            owner_main()
        except StopIteration:

            # Output only shows inputs for owner_main, there doesn't seem to be a better way to do this
            self.assertEqual('Which order do you wish to view the products for? (0 to exit): ', mock_input.call_args.args[0])

    @patch('builtins.input', side_effect=['2', '1'])
    def test_owner_main_view_order_items(self, mock_input):
        try:
            owner_main()
        except StopIteration:
            # Output only shows inputs for owner_main, there doesn't seem to be a better way to do this
            self.assertIn('Press enter to continue...', mock_input.call_args.args[0])

if __name__ == '__main__':
    unittest.main()
