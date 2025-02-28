# DMDX-JSON

Convert DMDX AZK output to JSON
This project was created to simplify the processing and analysis of DMDX experiment data. DMDX is widely used in psychological and linguistic research, but its AZK output format can be difficult to work with in modern data analysis tools. By converting AZK files to JSON, researchers can easily import their experimental data into spreadsheet applications, statistical packages, and data visualization tools without manual reformatting.

## Dependencies
* Python 3.9
* DMDX 6.1.5.2

## How to use
Simply run the script. Select the AZK file to convert. 
The output JSON file can be loaded to Excel using Power Queries.
If there are no errors in the conversion, an information message will be displayed at the end. Otherwise, a warning message will be displayed.

Please set:
* Record Clock On Time \<rcot\>
* Output AZK \<azk\>