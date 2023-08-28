import csv


class ReaderCsvFile:
    @staticmethod
    def read_csv_file(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            data = list(reader)
        return data
