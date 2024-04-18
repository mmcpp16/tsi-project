import unittest
from unittest.mock import MagicMock, patch
from src.Owner import owner_main

#Patching all external dependencies
@patch('src.Owner.TableBuilder')
@patch('src.Owner.input_validation.get_valid_range')
@patch('src.Owner.DatabaseHandler')
class TestOwnerMain(unittest.TestCase):
    """Mock tests for owner_main functionality"""

    def test_view_products(self, mock_database_handler, mock_input_validation, mock_table_builder):
        mock_input_validation.return_value = 1
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, 'Beach Ball', 5.99, 100)]
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_database_handler.return_value.dbConnection = mock_connection

        owner_main()

        mock_database_handler.assert_called_once()
        mock_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT * FROM Product")
        mock_input_validation.assert_called_once_with("What do you want to view?", 1, 2)
        mock_table_builder.return_value.build.assert_called_once()

    def test_view_order(self, mock_database_handler, mock_input_validation, mock_table_builder):
        mock_input_validation.return_value = 2
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, 'Derek', 'Somerville', 'Tablet', '2024-04-23 12:00:00' )]
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_database_handler.return_value.dbConnection = mock_connection

        owner_main()

        mock_database_handler.assert_called_once()
        mock_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT * FROM CustomerOrder")
        mock_input_validation.assert_called_once_with("What do you want to view?", 1, 2)
        mock_table_builder.return_value.build.assert_called_once()

if __name__ == '__main__':
    unittest.main()