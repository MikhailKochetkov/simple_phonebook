import os
import csv

from handlers import (
    read_file_data,
    search,
    add_record,
    edit_record)
from helpers import get_column_headers, get_search_results, input_data_dict
from settings import FILE, HEADERS


def main():
    if not os.path.isfile(FILE):
        with open(FILE, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(HEADERS)
    run = input('what do you want to do (search records - s; open phonebook - o; add record - a; edit record - e): ')
    fields = get_column_headers(FILE)
    if run == 's':
        sd = input_data_dict(0, len(HEADERS))
        print(search(sd))
    if run == 'e':
        rec_num = 0
        print('whose data do you want to update?')
        ed = input_data_dict(0, len(HEADERS[:3]))
        count = len(get_search_results(ed))
        print(f'found records to your request: {count}')
        print(search(ed))
        if count > 1:
            rec_num = int(input('which record do you want to update?: ')) - 1
        print('what data do you want to change?')
        fields_to_change = input_data_dict(3, len(HEADERS))
        print(edit_record(get_search_results(ed)[rec_num], fields_to_change))
        print(search(ed))
    if run == 'o':
        print(read_file_data())
    if run == 'a':
        record = [input(f'please enter {field.replace("_", " ")}: ') for field in fields]
        print(add_record(record))


if __name__ == '__main__':
    main()
