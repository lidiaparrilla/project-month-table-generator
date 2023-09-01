import argparse
from datetime import datetime

def generate_table(start_month, start_year, num_months):
    current_month = start_month
    current_year = start_year
    current_month_count = 1
    
    while num_months > 0:
        table_row = ["|", "|"]
        for month_index in range(1, 13):

            month_name = datetime(year=current_year, month=month_index, day=1).strftime('%b')
            table_row[0] += f" {month_name} |"
            
            if current_month <= 12 and num_months > 0:
                table_row[1] += f" M{current_month_count} |"
                current_month_count += 1
                num_months -= 1
            else:
                table_row[1] += "  |"
                
            current_month += 1
                
        print(f"| {current_year} {table_row[0]}")
        print("|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|")
        print(f"|      {table_row[1]}")
        print(f"\n")
        current_month = 1
        current_year += 1
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a Markdown table for months.')
    parser.add_argument('-m', '--month', type=int, required=True, help='Starting month as a number between 1 and 12.')
    parser.add_argument('-y', '--year', type=int, required=True, help='Starting year as a four-digit number.')
    parser.add_argument('-n', '--num_months', type=int, required=True, help='Number of months to include in the table.')
    
    args = parser.parse_args()
    
    if args.month and args.year and args.num_months:
        generate_table(args.month, args.year, args.num_months)
    else:
        parser.print_help()
