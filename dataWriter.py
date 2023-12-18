import csv
from scraper import scrape_area_codes
area_codes_data = scrape_area_codes()


output_csv_file = 'area_codes.csv'

with open(output_csv_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(['state', 'area_code'])

    for state, codes in area_codes_data.items():
        for code in codes:
            csvwriter.writerow([state, code])

print(f"CSV file '{output_csv_file}' created successfully.")