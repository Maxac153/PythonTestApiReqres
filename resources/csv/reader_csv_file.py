import csv


class ReaderCsvFile:
    @staticmethod
    def read_csv_file(file_path: str):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            data = list(reader)
        return data

    @staticmethod
    def read_two_csv_file(file_path_one: str, file_path_two: str):
        with open(file_path_one, 'r') as file_one, open(file_path_two, 'r') as file_two:
            reader_one = csv.reader(file_one)
            reader_two = csv.reader(file_two)
            next(reader_one)
            next(reader_two)
            data = zip(list(reader_one), list(reader_two))
        return data
