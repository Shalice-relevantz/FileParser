import pandas as pd
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

def parse_file(input_file, output_file):
    ''' parses input_file and writes clean data to output_file. Uses pandas to do the parsing'''
    try:
        logging.info(f"Starting file parsing. InputFile Provided: {input_file}")

        df = pd.read_csv(input_file, delimiter="~", names=["temp"])
        result_data = []
        df_datas = df["temp"].str.split("|")

        for df_data in df_datas:
        	if len(df_data) >=7:        		       		
        		df_data = df_data[1:-1]
        		if df_data[0].strip() == 'Stat':
        			continue

        		clean_up_data = [elem.strip() for elem in df_data]
        		clean_up_data[5] = update_lc_amt(clean_up_data[5])
        		result_data.append(clean_up_data)

        df = pd.DataFrame(result_data, columns=header)
        df.to_csv(output_file, index=False)
        logging.info(f"Outfile generated with cleaned data. Outfile: {output_file}")
    except Exception as e:
        logging.info("Error parsing file-----", e)


if __name__ == "__main__":
    try:
        input_file = str(basedir) + "/forParsing_task.xls"
        output_file = str(basedir) + "/cleanedOutput.csv"
        start_time = datetime.now()
        parse_file(input_file, output_file)
        print(f"Took time: {datetime.now() - start_time}")
    except Exception as e:
        logging.info("Error parsing file")