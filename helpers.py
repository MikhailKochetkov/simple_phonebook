from prettytable import PrettyTable


def convert_csv_to_table(th: list, td: list[list]):
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
