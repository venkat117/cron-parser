import sys

# Function to expand the minute field
def expand_field(field, min_value, max_value):
    if field == "*":
        return list(range(min_value, max_value + 1))
    
    # Handle step values, like */15
    if field.startswith("*/"):
        step = int(field[2:])
        return list(range(min_value, max_value + 1, step))
    
    # Handle ranges like 1-5
    if "-" in field:
        start, end = map(int, field.split("-"))
        return list(range(start, end + 1))
    
    # Handle comma-separated values like 1,15
    if "," in field:
        return list(map(int, field.split(",")))
    
    # Handle single values
    return [int(field)]

# Function to parse the cron expression
def parse_cron_expression(cron_expr):
    # Split the cron expression into its time fields and command
    fields = cron_expr.split(maxsplit=5)
    
    if len(fields) != 6:
        print("Error: Invalid cron expression. There should be 6 fields.")
        sys.exit(1)
    
    minute_field = fields[0]
    hour_field = fields[1]
    day_of_month_field = fields[2]
    month_field = fields[3]
    day_of_week_field = fields[4]
    command = fields[5]

    # Expand each field
    minute = expand_field(minute_field, 0, 59)
    hour = expand_field(hour_field, 0, 23)
    day_of_month = expand_field(day_of_month_field, 1, 31)
    month = expand_field(month_field, 1, 12)
    day_of_week = expand_field(day_of_week_field, 0, 7)

    # Print the result in table format
    print(f"minute         {' '.join(map(str, minute))}")
    print(f"hour           {' '.join(map(str, hour))}")
    print(f"day of month   {' '.join(map(str, day_of_month))}")
    print(f"month          {' '.join(map(str, month))}")
    print(f"day of week    {' '.join(map(str, day_of_week))}")
    print(f"command        {command}")
    

if __name__ == "__main__":
    # Ensure the user provides the cron expression as an argument
    if len(sys.argv) != 2:
        print("Usage: python cron_parser.py '<cron_expression>'")
        sys.exit(1)
    
    # Get the cron expression from the command-line argument
    cron_expression = sys.argv[1]
    
    # Parse and expand the cron expression
    parse_cron_expression(cron_expression)
