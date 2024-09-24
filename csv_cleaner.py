import csv
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def clean_csv(input_file, output_file):
    seen_user_ids = set()
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            if row['user_id'] not in seen_user_ids and is_valid_email(row['email']):
                writer.writerow(row)
                seen_user_ids.add(row['user_id'])

if __name__ == "__main__":
    clean_csv('input.csv', 'cleaned_output.csv')
