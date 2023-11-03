import csv
import pandas as pd

from helpers import (
    convert_to_table,
    get_columns_headers,
    get_search_results,
    get_max_id)
from settings import FILE


def search(search_params: dict):
    try:
        res_list = []
        search_result = get_search_results(search_params)
        for res in search_result:
            res_list.append([res[key] for key in res])
        header = get_columns_headers(FILE)
        table = convert_to_table(header, res_list)
        return table
    except Exception as e:
        return f'error reading a file: {str(e)}'


def edit_record(rec_id: str, data_to_update: dict):
    df = pd.read_csv(FILE, delimiter=';', dtype=pd.StringDtype()).set_index('id')
    df.loc[rec_id, [x for x in data_to_update.keys()]] = data_to_update
    df.to_csv(FILE, sep=';')
    return 'data updated'


def add_record(rec: dict):
    try:
        next_id = get_max_id() + 1
        new_rec = {'id': next_id} | rec
        with open(FILE, mode='a', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, delimiter=';', fieldnames=new_rec.keys())
            writer.writerow(new_rec)
        return new_rec
    except Exception as e:
        return f'error adding a record to file: {str(e)}'


def read_file_data():
    try:
        with open(FILE, encoding='utf-8', mode='r', newline='') as file:
            body = []
            reader = csv.reader(file, delimiter=';')
            next(reader)
            for row in reader:
                body.append(row)
            header = get_columns_headers(FILE)
            table = convert_to_table(header, body)
            return table
    except Exception as e:
        return f'error reading a file: {str(e)}'
