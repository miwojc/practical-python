# fileparse.py
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    """
    Parse a CSV file into a list of records
    """
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers if exist
        headers = next(rows) if has_headers else []

        # If specific columns have been selected, make indices for filtering
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []
        for row in rows:
            if not row:
                continue

            # If specific column indices are selected, pick them out
            if select:
                row = [row[index] for index in indices]
            
            # Apply type conversion to the row
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # Make a dictionary if headers of tupe if no headers
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row) 
            records.append(record)

        return records
