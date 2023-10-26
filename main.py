import os
import csv

from handlers import (
    read_file_data,
    search,
    add_record,
    edit_record)
from helpers import get_column_headers
from settings import FILE, HEADERS


def main():
    if not os.path.isfile(FILE):
        with open(FILE, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(HEADERS)
    run = input('what do you want to do (search records - s; open phonebook - o; add record - a; edit record - e): ')
    fields = get_column_headers(FILE)
    if run == 's':
        d = {}
        for field in fields:
            value = input(f'please enter {field.replace("_", " ")}: ')
            if value:
                d[field] = value
        print(search(d))
    if run == 'e':
        print('feature in development')
    if run == 'o':
        print(read_file_data())
    if run == 'a':
        record = [input(f'please enter {field.replace("_", " ")}: ') for field in fields]
        print(add_record(record))


if __name__ == '__main__':
    main()
