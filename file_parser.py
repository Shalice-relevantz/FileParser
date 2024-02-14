import re
from datetime import datetime
import logging 
import os 


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
basedir = os.path.abspath(os.path.dirname(__name__))

header = ['Stat', 'Account', 'No', 'Date', 'Net due dt', 'LC amnt', 'DD', 'CCAr', 'PayT', 'Type']


def update_lc_amt(elem):
    '''updates lc_amount to remove "," in data and adjust integer sign'''
    try:
        elem = elem.replace(",", "")
        if "-" in elem: 
            val = "-" + elem[:-1]
            return val
        else:
            return elem
    except Exception as e:
        logging.info("Error updating LC amount during file parsing")


def parse_file(header_list, input_file, output_file):
    '''Parses input file and writes clean data in outfile. For each file line parses the format, adjusts lc_amt and writes to outfile'''
    try:
        logging.info(f"Starting file parsing. InputFile Provided: {input_file}")
        with open(input_file, "r") as file:
            lines = file.readlines()            
            result_data = []
            for line in lines:
                row_data = line.split("|")
                if len(row_data) >=7:                            
                    row_data = row_data[1:-1]
                    if row_data[0].strip() == 'Stat':
                        continue

                    clean_up_data = [elem.strip() for elem in row_data]
                    clean_up_data[5] = update_lc_amt(clean_up_data[5])
                    result_data.append(clean_up_data)

        with open(output_file, 'w') as outfile:

            result_data.insert(0,header)
            for data in result_data:

                for item in data:
                    outfile.write(item + ',')
                    outfile.write('\n')
            logging.info(f"Outfile generated with cleaned data. Outfile: {output_file}")
    except Exception as e:
        logging.info("Error parsing file", e)


if __name__ == "__main__":
    try:
        print("vdgsvshbvdjb")
        start_time = datetime.now()
        input_file=str(basedir) + "/forParsing_task.xls"
        output_file=str(basedir) + "/cleanedOutputWithoutlib.csv"
        
        parse_file(header, input_file, output_file)
        logging.info(f"Took time: {datetime.now() - start_time}")
    except Exception as e:
        logging.info("Error parsing file")