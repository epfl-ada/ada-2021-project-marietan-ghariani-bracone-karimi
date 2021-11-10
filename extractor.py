import bz2
import pandas as pd
import numpy as np

if __name__ == '__main__':
    df_reader = pd.read_json('quotes-2020.json.bz2', lines=True, compression='bz2', chunksize=1000000)
    nd_frame = pd.read_csv('us_natural_disasters/us_disaster_declarations.csv')

    nd_frame.drop(nd_frame[nd_frame.incident_type == "Other"].index, inplace = True)

    # print(nd_frame.head())
    nd_names = nd_frame.incident_type.unique()
    # print(nd_names)
