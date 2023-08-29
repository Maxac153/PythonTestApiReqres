from resources.csv.reader_csv_file import ReaderCsvFile

file_path_one = 'resources/csv/data/create/response_create.csv'
file_path_two = 'resources/csv/data/create/response_create.csv'
data = ReaderCsvFile.read_two_csv_file(file_path_one, file_path_two)
print(data)

for i in data:
    print(i)
