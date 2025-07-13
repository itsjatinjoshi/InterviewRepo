import csv

file = "C:\\Project\\InterviewRepo\\temp.csv"


def test_count_rows_and_column():
    with open(file, 'r') as csv_file:
        file_content = csv.DictReader(csv_file)

        total_column = len(file_content.fieldnames)

        total_row = 0
        for _ in file_content:
            total_row += 1
        print(total_column)
        print(total_row)


def test_rows_by_condition():
    with open(file, 'r') as file_data:
        csv_file = csv.DictReader(file_data)
        conditional_rows = []

        for row in csv_file:
            if int(float(row['amount'])) > 100:
                conditional_rows.append(row)

        for row in conditional_rows:
            print(conditional_rows)


def test_sum_of_quantity_and_amount():
    with open(file, 'r') as file_data:
        csv_data = csv.DictReader(file_data)
        total_quantity = 0
        total_amount = 0
        for row in csv_data:
            quantity = int(float(row['quantity']))
            amount = int(float(row['amount']))
            total_amount += amount
            total_quantity += quantity

        print(f"Total quantities are {total_quantity} and the value is {total_amount}")


def test_unique_value():
    with open(file, 'r') as file_data:
        csv_file = csv.DictReader(file_data)
        uniq_product = set()
        uniq_email = set()
        for row in csv_file:
            product = row.get('product')
            email = row.get('email')
            if product:
                uniq_product.add(product)

            if email:
                uniq_email.add(email)
        print(len(uniq_product))
        print(len(uniq_email))
        print(uniq_product, uniq_email)
#
# # class CsvTestCases:
