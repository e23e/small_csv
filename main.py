import argparse
import csv
import sys

class CsvHandler:
    def __init__(self, args) -> None:
        self.file_path = args.csv_file
        self.arg_sort_by = args.sort_by
        self.filter_in = self.convert_comma_seperated(args.filter_in)
        self.filter_out = self.convert_comma_seperated(args.filter_out)
        self.field_order = self.convert_comma_seperated(args.field_order)

    def convert_comma_seperated(self, string_value: str) -> list:
        if string_value == None:
            return None
        string_value = string_value.split(",")
        output = []
        for each in string_value:
            output.append(each.strip())
        return output

    def process(self):
        self.validate()
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            if self.filter_in:
                self.filter_in = self.arrange_filters_values(rows,  self.filter_in)
                rows  = self.process_filter_in(rows)
            if self.filter_out:
                self.filter_out = self.arrange_filters_values(rows,  self.filter_out)
                rows  = self.process_filter_out(rows)
            try:    
                columns = rows[0].keys()
            except IndexError:
                return None
            if self.arg_sort_by and self.arg_sort_by in columns:
                rows = self.process_sort_by(rows, self.arg_sort_by)
            if self.field_order:
                rows = self.process_field_order(rows)
            self.show_output(rows)

    def arrange_filters_values(self,rows, filter):
        columns = rows[0].keys()
        output = []
        for each_column in columns:
            if each_column in filter:
                output.append(each_column)
        return output

    def show_output(self, rows):
        writer = csv.DictWriter(
            sys.stdout,
            fieldnames=rows[0].keys(),
            extrasaction='ignore',
            lineterminator='\n'
        )
        writer.writeheader()
        writer.writerows(rows)

    def process_field_order(self, rows):
        headers = rows[0].keys()
        missing_fields = [col for col in headers if col not in self.field_order]
        new_order = self.field_order + missing_fields
        all_outputs = []
        for each_row in rows:
            output = {}
            for column in new_order:
                try:
                    output[column] = each_row[column]
                except KeyError:
                    pass
            all_outputs.append(output)
        return all_outputs

    def process_sort_by(self,rows, sort_column):
        if sort_column:
            if sort_column == 'severity':
                rows.sort(key=lambda row: self.get_severity_index(row[sort_column]))
            else:
                rows.sort(key=lambda row: row[sort_column])
        return rows
    
    def get_severity_index(self,severity):
        severity_order = {'LOW': 0, 'MED': 1, 'HIGH': 2}
        return severity_order.get(severity)

    def process_filter_in(self,rows):
        all_outputs = []
        for each_row in rows:
            output = {}
            for filter_in_column in self.filter_in:
                output[filter_in_column] = each_row[filter_in_column]
            all_outputs.append(output)
        return all_outputs
        
    def process_filter_out(self,rows):
        all_outputs = []
        for each_row in rows:
            for filter_out_column in self.filter_out:
                if self.filter_in and filter_out_column not in self.filter_in:
                    del each_row[filter_out_column]
                if not self.filter_in:
                    del each_row[filter_out_column]
            all_outputs.append(each_row)
        return all_outputs

    def validate(self):
        if not self.file_path.endswith(".csv"):
            raise Exception("File Extension is not supported")
        try:
             with open(self.file_path, 'r') as file:
                reader = csv.DictReader(file)
                rows = list(reader)
                columns = None
                try:
                    columns = rows[0].keys()
                except IndexError:
                    raise Exception("Empty csv file given")
                if self.filter_in:
                    for each_filter_in_arg in self.filter_in:
                        if each_filter_in_arg not in columns:
                            raise Exception("Unknown columns in filter_in")
                if self.filter_out:
                    for each_filter_out_arg in self.filter_out:
                        if each_filter_out_arg not in columns:
                            raise Exception("Unknown columns in filter_out")
                if self.field_order:
                    for each_order_column in self.field_order:
                        if each_order_column not in columns:
                            raise Exception("Unknown columns in field_order")         
        except FileNotFoundError:
            raise Exception("File not found, please check the file path!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sort based on a given column.')
    parser.add_argument('csv_file', help='Path to the CSV file')
    parser.add_argument('--sort_by', help='Column to sort by (Single value)')
    parser.add_argument('--filter_in', help='Show only requested columns (Comma seperated)')
    parser.add_argument('--filter_out', help='Show all columns except mentioned columns (Comma seperated)')
    parser.add_argument('--field_order', help='Helps ordering the column (Comma seperated)')
    args = parser.parse_args()
    csv_obj = CsvHandler(args)
    csv_obj.process()


