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


def get_columns_headers(file_path):
    with open(file_path, 'r') as f:
        first_line = f.readline()
        headers = first_line.strip().split(';')
    return headers


def get_search_results(params: dict) -> list:
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


def get_max_id():
    try:
        with open(FILE, mode='r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            max_id = max(int(row[0]) for row in reader)
            return max_id
    except FileNotFoundError:
        return 0


## TODO: Remove input_data_dict
def input_data_dict(n: int, m: int):
    data = {}
    fields = get_columns_headers(FILE)
    for field in fields[n:m]:
        value = input(f'please enter {field.replace("_", " ")}: ')
        if value:
            data[field] = value
    return data


def input_data(fields: list, start: int | None, stop: int | None) -> str:
    for field in fields[start:stop]:
        value = input(f'please enter {field.replace("_", " ")}: ')
        yield {field: value}
