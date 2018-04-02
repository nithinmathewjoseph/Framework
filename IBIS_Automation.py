import pandas as pd
import argparse
from string import Template
from collections import OrderedDict


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('-input', action='store', dest='input', required=True, help='Please provide the input file')
    args.add_argument('-golden', action='store', dest='template', required=True,
                      help='Please provide the golden template file')
    args.add_argument('-output', action='store', dest='output', required=True, help='Please provide the output file')
    opts = args.parse_args()
    modified = []
    ibis_dataframe = pd.read_excel(opts.input)
    ibis_master_dictionary = OrderedDict((str(row["IDENTIFIER"]),str(row["INFO"])) for index, row in ibis_dataframe.iterrows())
    golden_template = open(opts.template, 'r').readlines()
    for line in golden_template:
        for key, value in ibis_master_dictionary.items():
            if key in line:
                line = Template(line).safe_substitute(**{key: value})
        modified.append(line)
    with open(opts.output, 'w') as output_config:
        modified_str = ''.join(modified)
        output_config.write(modified_str)
    pass