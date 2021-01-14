import csv
dict_data = [
{ 'Name': 'Alex', 'DOB': '20/11/1999'},
{ 'Name': 'Ben', 'DOB': '23/10/2010'}

]new={'Name': Name,'DOB':Date}
if new not in dict_data:
    dict_data.append(new)
import csv
csv_columns = ['Name','DOB']
csv_file = "Storage.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")
