products = ([(1, 'Beach Towel', 100, 15.99),
             (2, 'Pedal Boat', 50, 1899.99),
             (3, 'Sunglasses', 75, 25.5),
             (4, 'Beach Umbrella', 30, 29.99),
             (5, 'Beach Chair', 40, 24.99),
             (6, 'Flip Flops', 80, 12.5),
             (7, 'Volley Ball', 60, 19.99),
             (8, 'Surf Board (Adult)', 25, 121.99),
             (9, 'Surf Board (Child)', 20, 104.99),
             (10, 'Inflatable Pool Float', 50, 18.99)])

customer_orders = [(1, 'Ayan', 'Ahmad', 'banana', '2024-04-26 12:00:00'),
                (2, 'Andrew', 'Mckelvey', 'abra kadabra', '2024-04-27 12:00:00')]

product_orders = [[('Beach Towel', 5, 0, 15.99), ('Sunglasses', 2, 5, 25.5), ('Volley Ball', 1, 5, 19.99), ('Surf Board (Adult)', 1, 0, 121.99), ('Inflatable Pool Float', 1, 5, 18.99)],
        [('Pedal Boat', 1, 0, 1899.99), ('Sunglasses', 2, 5, 25.5), ('Volley Ball', 1, 5, 19.99), ('Inflatable Pool Float', 1, 5, 18.99)]]


class DatabaseHelperStub:

    def get_all_products(self):
        return products

    def get_all_customer_orders(self):
        return customer_orders

    def get_customer_products(self, order_id):
        return product_orders[order_id-1]

    def add_customer_order(self, first_name, last_name, passphrase, collection_date, products):
        customer_order_id = customer_orders[-1][0]+1
        customer_orders.append((customer_order_id, first_name, last_name, passphrase, collection_date))
        product_orders.extend([(customer_order_id, *product) for product in products])