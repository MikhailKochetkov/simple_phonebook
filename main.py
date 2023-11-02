import os
import csv

from handlers import (
    read_file_data,
    search,
    add_record,
    edit_record)
from helpers import (
    get_column_headers,
    get_search_results,
    input_data_dict,
    input_data)
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
                   'add record - a; edit record - e): ')
    fields = get_column_headers(FILE)
    if choice == 's':
        result = {}
        generator = input_data(fields, start=1, stop=None)
        for data in generator:
            if any(data.values()):
                result.update({k: v for k, v in data.items() if v})
        print(f'search result:\n{search(result)}')
    if choice == 'e':
        print('whose data do you want to update?')
        ed = input_data_dict(1, len(HEADERS[:4]))
        count = len(get_search_results(ed))
        print(f'found records to your request: {count}')
        print(search(ed))
        if count > 1:
            rec_id = input('which record do you want to update?: ')
        else:
            rec_id = get_search_results(ed)[0]['id']
        print('what data do you want to change?')
        fields_to_change = input_data_dict(4, len(HEADERS))
        print(edit_record(rec_id, fields_to_change))
        print(search(ed))
    if choice == 'o':
        print(f'result:\n{read_file_data()}')
    if choice == 'a':
        res = {}
        gen = input_data(fields, start=1, stop=None)
        for val in gen:
            res.update(val)
        print(add_record(res))


if __name__ == '__main__':
    main()
