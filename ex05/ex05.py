import csv
from collections import defaultdict


def process_shopping_list(file):
    id_is_changed = False
    previous_id = 1
    shopping_list_data_one = defaultdict(list)
    id = 0

    with open(file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        current_id = 1

        for row in reader:

            if not row:
                continue

            client_id, *products = [item.strip() for item in row]

            if current_id != client_id:
                id_is_changed = True
                current_id = client_id
                previous_id = current_id
                id += 1
            else:
                id_is_changed = False
            shopping_list_data_one[id].extend(products)

    return shopping_list_data_one


def print_shopping_list(shopping_list):
    for client_id, products in shopping_list.items():
        print(f"{client_id}: {', '.join(products)}")


if __name__ == "__main__":
    input_file = "dataanal.csv"
    shopping_list_data = process_shopping_list(input_file)

    print_shopping_list(shopping_list_data)
