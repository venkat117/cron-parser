# Cron Expression Parser

This is a command-line application that parses a cron string and expands each field to show the times at which it will run.

## Features
- Expands cron fields including `*`, `*/step`, `range`, and `list`.
- Provides output in a formatted table.
- Supports simple command handling.

## Requirements

You will need **Python 3** to run this project. Install Python if it's not already installed.

## Installation

Clone this repository:

    git clone https://github.com/venkat117/cron-parser.git
    cd cron-parser

## Usage
Run the script from the command line, passing the cron string as a single argument:
    
    python cron_parser.py "<cron_string>"
For example:
    
    python cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"
Make sure to replace the cron expression and command as needed.


## Output

 The output is formatted as a table with the field name.

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
- Additional functionality such as calculating the next run time based on the current time.
- Human-readable translation of cron fields into sentences.
- Build a graphical user interface (GUI) for easier usage.


