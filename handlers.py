import csv

from helpers import convert_csv_to_table, get_column_headers
from settings import FILE


def search(search_params: dict):
    try:
        with open(FILE, mode='r', newline='') as file:
            res_dict = []
            res_list = []
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                match = True
                for column, value in search_params.items():
                    if row[column] != value:
                        match = False
                        break
                if match:
                    res_dict.append(row)
            for res in res_dict:
                res_list.append([res[key] for key in res])
            header = get_column_headers(FILE)
            table = convert_csv_to_table(header, res_list)
            return table
    except Exception as e:
        return f'error reading a file: {str(e)}'


def edit_record():
    pass


def add_record_to_file(rec: list):
    try:
        with open(FILE, mode='a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(rec)
        return 'the record added to file successfully'
    except Exception as e:
        return f'error adding a record to file: {str(e)}'


def read_file_data():
    try:
        with open(FILE, encoding='utf-8', mode='r', newline='') as file:
            body = []
            reader = csv.reader(file, delimiter=';')
            header = next(reader)
            for row in reader:
                body.append(row)
            table = convert_csv_to_table(header, body)
            return table
    except Exception as e:
        return f'error reading a file: {str(e)}'
