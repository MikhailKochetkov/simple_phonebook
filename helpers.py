import csv

from prettytable import PrettyTable

from settings import FILE


def convert_to_table(th: list, td: list[list]) -> object:
    columns = len(th)
    table = PrettyTable(th)
    td_data = td[:]
    while td_data:
        table.add_rows(td_data[:columns])
        td_data = td_data[columns:]
    return table


def get_columns_headers(file_path) -> list[str]:
    with open(file_path, 'r') as f:
        first_line = f.readline()
        headers = first_line.strip().split(';')
    return headers


def get_search_results(params: dict) -> list[str]:
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


def get_max_id() -> int:
    try:
        with open(FILE, mode='r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            max_id = max(int(row[0]) for row in reader)
            return max_id
    except FileNotFoundError:
        return 0


def input_data(fields: list, start: int | None, stop: int | None) -> str:
    for field in fields[start:stop]:
        value = input(f'please enter {field.replace("_", " ")}: ')
        yield {field: value}


def dict_generator(generator):
    result = {}
    for data in generator:
        if any(data.values()):
            result.update({k: v for k, v in data.items() if v})
    return result


def get_record_by_id(record_id: int) -> dict | None:
    with open(FILE, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        headers = next(reader)
        for row in reader:
            if row[0] == str(record_id):
                return dict(zip(headers, row))
    return None
