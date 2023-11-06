import csv
import pandas as pd

from helpers import (
    convert_to_table,
    get_columns_headers,
    get_search_results,
    get_max_id)
from settings import FILE, LINES_PER_PAGE


def search_output(search_params: dict) -> object:
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


def update_record(rec_id: str, data_to_update: dict) -> None:
    try:
        df = pd.read_csv(FILE, delimiter=';', dtype=pd.StringDtype()).set_index('id')
        df.loc[rec_id, [x for x in data_to_update.keys()]] = data_to_update
        df.to_csv(FILE, sep=';')
    except Exception as e:
        print(f'data update error: {str(e)}')


def add_record(rec: dict) -> None:
    try:
        next_id = get_max_id() + 1
        new_rec = {'id': next_id} | rec
        with open(FILE, mode='a', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, delimiter=';', fieldnames=new_rec.keys())
            writer.writerow(new_rec)
    except Exception as e:
        print(f'error adding a record to file: {str(e)}')


def read_file_data_output() -> object:
    try:
        with open(FILE, encoding='utf-8', mode='r', newline='') as file:
            body = []
            reader = csv.reader(file, delimiter=';')
            next(reader)
            for row in reader:
                body.append(row)
            total_lines = len(body)
            total_pages = (total_lines + LINES_PER_PAGE - 1) // LINES_PER_PAGE
            current_page = 1
            while True:
                start = (current_page - 1) * LINES_PER_PAGE
                end = start + LINES_PER_PAGE
                page_lines = body[start:end]
                header = get_columns_headers(FILE)
                table = convert_to_table(header, page_lines)
                if current_page == total_pages:
                    yield table
                    break
                yield table
                user_input = input('press Enter (or "q" to quit) to continue: ')
                if user_input.lower() == 'q':
                    break
                current_page += 1
    except Exception as e:
        return f'error reading a file: {str(e)}'
