import csv

from prettytable import PrettyTable

from settings import FILE


def convert_to_table(th: list, td: list[list]):
    columns = len(th)
    table = PrettyTable(th)
    td_data = td[:]
    while td_data:
        table.add_rows(td_data[:columns])
        td_data = td_data[columns:]
    return table


def get_column_headers(file_path):
    with open(file_path, 'r') as f:
        first_line = f.readline()
        headers = first_line.strip().split(';')
    return headers


def get_search_results(params: dict):
    with open(FILE, mode='r', newline='') as file:
        results = []
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            match = True
            for column, value in params.items():
                if row[column] != value:
                    match = False
                    break
            if match:
                results.append(row)
        return results


def input_data_dict(n: int, m: int):
    data = {}
    fields = get_column_headers(FILE)
    for field in fields[n:m]:
        value = input(f'please enter {field.replace("_", " ")}: ')
        if value:
            data[field] = value
    return data
