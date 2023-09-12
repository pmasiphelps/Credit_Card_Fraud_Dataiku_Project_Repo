# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
TRANSACTIONS_prepared = dataiku.Dataset("TRANSACTIONS_prepared")
TRANSACTIONS_prepared_df = TRANSACTIONS_prepared.get_dataframe()


TRANSACTIONS_filtered_z_score_df = TRANSACTIONS_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
TRANSACTIONS_filtered_z_score = dataiku.Dataset("TRANSACTIONS_filtered_z_score")
TRANSACTIONS_filtered_z_score.write_with_schema(TRANSACTIONS_filtered_z_score_df)
