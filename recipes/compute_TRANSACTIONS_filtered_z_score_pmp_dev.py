# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
from feature_engineering.column_transformations import filter_df_by_zscore

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
TRANSACTIONS_prepared = dataiku.Dataset("TRANSACTIONS_prepared")
TRANSACTIONS_prepared_df = TRANSACTIONS_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
TRANSACTIONS_prepared_df = filter_df_by_zscore(TRANSACTIONS_prepared_df, "purchase_amount", zscore_threshold = 3)

print("hi bundle v2")
# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
# Dataset TRANSACTIONS_filtered_z_score renamed to TRANSACTIONS_filtered_z_score_pmp_dev by patrick.masi-phelps@dataiku.com on 2023-09-12 01:05:45
TRANSACTIONS_filtered_z_score = dataiku.Dataset("TRANSACTIONS_filtered_z_score_pmp_dev")
TRANSACTIONS_filtered_z_score.write_with_schema(TRANSACTIONS_prepared_df)