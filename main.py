import os
import csv

from handlers import (
    read_file_data_output,
    search_output,
    add_record,
    update_record)
from helpers import (
    get_columns_headers,
    get_search_results,
    input_data,
    dict_generator,
    get_record_by_id,
    get_max_id)
from settings import FILE

HEADERS = [
    'id',
    'last_name',
    'first_name',
    'middle_name',
    'organization',
    'work_number',
    'personal_number']


def main():
    if not os.path.isfile(FILE):
        with open(FILE, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(HEADERS)
    choice = input('what do you want to do '
                   '(search records - s; open phonebook - o; '
                   'add record - a; update record - u): ')
    fields = get_columns_headers(FILE)
    if choice == 's':
        data_to_search = input_data(fields, start=1, stop=None)
        search_result = dict_generator(data_to_search)
        print(f'search results:\n{search_output(search_result)}')
    if choice == 'u':
        print('whose data do you want to update?')
        data_to_update = input_data(fields, start=1, stop=4)
        update_result = dict_generator(data_to_update)
        count = len(get_search_results(update_result))
        if count == 0:
            print('no data was found matching the search parameters')
        else:
            print(f'found records to your request: {count}')
            print(search_output(update_result))
            if count > 1:
                rec_id = input('which record do you want to update?: ')
            else:
                rec_id = get_search_results(update_result)[0]['id']
            print('what data do you want to change?')
            fields_to_change = input_data(fields, start=4, stop=None)
            change_result = dict_generator(fields_to_change)
            update_record(rec_id, change_result)
            updated_record = get_record_by_id(int(rec_id))
            print(f'updated record:\n{search_output(updated_record)}')
    if choice == 'o':
        print(f'result:')
        open_result = read_file_data_output()
        for table in open_result:
            print(table)
    if choice == 'a':
        add_result = {}
        add_rec = input_data(fields, start=1, stop=None)
        for val in add_rec:
            add_result.update(val)
        if not dict(filter(lambda x: x[1], add_result.items())):
            print('no data to added')
        else:
            add_record(add_result)
            max_id = get_max_id()
            new_record = get_record_by_id(max_id)
            print(f'added record:\n{search_output(new_record)}')


if __name__ == '__main__':
    main()
