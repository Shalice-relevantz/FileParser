# File Parser

## Parser using pandas

**Script Detail: This Script uses pandas library to parse input file provided and generate a cleaned outfile with structured data in a delimited format. .**

## Installation

# Python Version 3.10.4

# Windows: Environment Setup
```commandline
python3 -m venv ..\fileparser_python_env
..\fileparser_python_env\Scripts\activate
pip install -r src\requirements.txt
```

# Linux: Environment Setup
```commandline
python3 -m venv ../fileparser_python_env
source ../fileparser_python_env/bin/activate
```

Clone this repository to your local machine:
```bash
git clone https://github.com/Shalice-relevantz/FileParser
```

Change into the project directory:

```bash
cd File-parser
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Usage
    
    1. start the application 

        python file_parser_using_pandas.py             

    2. Input/Output file:

        Input Filename: forParsing_task.xls
        Filename: cleanedOutput.csv



# File parser without using third party lib

**Script Details: This script uses  built python libraries to parse input file provided and generate a cleaned outfile with structured data in a delimited format.**


## Usage
    
    1. start the application 

        python file_parser.py 

        Note: Since it doesnt require any exteral package , we do not want to run the `pip install -r reqrirements.txt` 
        

    2. Input/Output file:

        Input Filename: forParsing_task.xls
        Filename: cleanedOutputWithoutlib.csv



## RunTime Comparison

Both scripts were run multiple times and it was observed script without using any thir party lib was always faster than the script which is used pandas by few ms and thus goes to assume would perform better with larger files. 
For 1 such sample local run below timings were observed for opensource and vanilla scripts:

    Script used pandas timing: 0:00:00.004571
    Script without using lib timing: 0:00:00.000814

Note: Time can be observed as the logger output in each script run. 