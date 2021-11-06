# fileparse.py
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    """
    Parse an iterable into a list of records with type conversion
    """
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the headers row if exist
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for rowno, row in enumerate(rows,start=1):
        if not row:
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [row[index] for index in indices]
        
        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue

        # Make a dictionary if headers of tupe if no headers
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row) 
        records.append(record)

        return records
