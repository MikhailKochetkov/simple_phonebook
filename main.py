from handlers import (
    read_file_data,
    search,
    add_record_to_file,
    edit_record)
from helpers import get_column_headers
from settings import FILE


def main():
    run = input('what do you want to do (search - s; open phonebook - o; add record - a; edit record - e): ')
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
        print(add_record_to_file(record))


if __name__ == '__main__':
    main()