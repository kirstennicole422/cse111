# My program exceeds requirements because I added the 30 day return by date to
# the bottom of the receipt.

import csv
from datetime import datetime, timedelta

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
    filename: the name of the CSV file to read.
    key_column_index: the index of the column
        to use as the keys in the dictionary.
    Return: a compound dictionary that contains
    the contents of the CSV file.
    """
    dict = {}
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            key = row[key_column_index]
            dict[key] = row
    return dict

def main():
    products_dict = {}
    try: 
        products_dict = read_dictionary("products.csv", 0)
    except FileNotFoundError as not_found_err:
        print("Error: missing file")
        print(not_found_err)
    
    # print(products_dict)
    request_list = []
    item_quantity = 0
    item_subtotal = 0.00
    sales_tax_rate = 0.06
    sales_tax_amount = 0.00
    total = 0.00

    store_name = "Snakes and Co"
    print(store_name)

    with open ("request.csv") as request:
        reader = csv.reader(request)
        next(reader)
        for row in request:
            request_list.append(row.strip().split(","))
        for i in request_list:
            try:
                print(f"{products_dict[i[0]][1]}: {i[1]} @ ${products_dict[i[0]][2]} ea")
                item_subtotal += float(i[1]) * float(products_dict[i[0]][2])
                item_quantity += int(i[1])
            except KeyError as key_err:
                print("Error: unknown product ID in request.csv file")
                print(key_err)
                

    sales_tax_amount = sales_tax_rate * item_subtotal
    total = item_subtotal + sales_tax_amount
    print (f"Number of Items: {item_quantity}")
    print(f"Subtotal: ${item_subtotal:.2f}")
    print(f"Sales Tax: ${sales_tax_amount:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Thank you for shopping at {store_name}.")
    print(f"{datetime.now():%a %b  %w %H:%M:%S %Y}")
    return_date = datetime.now() + timedelta(days = 30);
    # print(return_date)
    print(f"Return by: {(return_date):%a %b %d %Y} at 9:00 PM")
if __name__ == "__main__":
    main()