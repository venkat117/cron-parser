# Cron Expression Parser

This is a command-line application that parses a cron string and expands each field to show the times at which it will run.

## Requirements

    - Python3 3.x

## Usage

1. Run the script from the command line, passing the cron string as a single argument:

        python cron_parser.py "<cron_string>"

2. For example:

        python cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"


## Output

 The output is formatted as a table with the field name taking the first 14 columns and the times as a space-separated list following it.

## Limitations

 This parser only handles the standard cron format with five time fields plus a command. It does not support special time strings such as "@yearly".

## Project Structure

     cron-parser/
     │
     ├── cron_parser.py        # The main script for parsing the cron expression
     └── README.md             # Project documentation

## Future Improvements

 - Support for special cron strings like @yearly, @monthly, @daily, etc.
- Enhanced error handling to provide more detailed messages for invalid cron expressions.
 -- Additional functionality such as calculating the next run time based on the current time.


