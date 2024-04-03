"""
Functions which you might not know and their functions:
- Extend: Appends a list
- Enumerate: Provides an entry of index and value of a list
- LJust: Puts spacing on the right to left justify the text but keeps in count the length of the text
- Zip: Makes parallel lists into entries

(Calling key-value pairs entries for simplicity)
"""


class TableBuilder:
    def __init__(self, max_content_per_page=10):
        self.headers = []
        self.rows = []
        self.max_content_per_page = max_content_per_page

    def add_header(self, header):
        self.headers.append(header)
        return self

    def add_headers(self, headers):
        self.headers.extend(headers)
        return self

    def add_row(self, row_data):
        self.rows.append(row_data)
        return self

    def add_rows(self, rows_data):
        self.rows.extend(rows_data)
        return self

    def build(self, page_number=None):
        # Check values are provided
        if not self.headers:
            raise ValueError("Headers must be added before building the table.")
        if not self.rows:
            raise ValueError("Rows must be added before building the table.")

        # Calculate max column widths
        col_widths = [len(header) for header in self.headers]  # Initialise values with header length
        for row in self.rows:
            for i, data in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(data)))

        # Get constants
        num_columns = len(self.headers)
        total_width = sum(col_widths) + num_columns * 3 + 1  # Magic numbers for the padding and seperators
        num_pages = -(-len(self.rows) // self.max_content_per_page)

        # Do page and offset calculations
        if page_number is not None:
            if page_number < 1 or page_number > num_pages:
                raise ValueError("Invalid page number.")
            start_index = (page_number - 1) * self.max_content_per_page
            end_index = min(page_number * self.max_content_per_page, len(self.rows))
        else:
            start_index = 0
            end_index = min(self.max_content_per_page, len(self.rows))

        # Print headers
        header_str = "|"
        for header, width in zip(self.headers, col_widths):
            header_str += f" {header.ljust(width)} |"
        print("-" * total_width)
        print(header_str)
        print("-" * total_width)

        # Print rows
        for row in self.rows[start_index:end_index]:
            row_str = "|"
            for data, width in zip(row, col_widths):
                row_str += f" {str(data).ljust(width)} |"
            print(row_str)
            print("-" * total_width)


"""
#Example of how it works:

if __name__ == "__main__":
    table = TableBuilder(max_content_per_page=5)\
        .add_headers(["Row Number", "Item Name", "Item Price", "Available Quantity"])\
        .add_rows([[1, "Beach Towel", 15.99, 100],
            [2, "Sunscreen SPF 50", 8.99, 50],
            [3, "Sunglasses", 25.50, 75],
            [4, "Beach Umbrella", 29.99, 30],
            [5, "Beach Chair", 24.99, 40],
            [6, "Flip Flops", 12.50, 80],
            [7, "Volley Ball", 19.99, 60],
            [8, "Surf Board (Adult)", 121.99, 25],
            [9, "Surf Board (Child)", 104.99, 20],
            [10, "Inflatable Pool Float", 18.99, 50]])
    table.build(page_number=1)
    input("Press enter for next page")
    table.build(page_number=2)
"""