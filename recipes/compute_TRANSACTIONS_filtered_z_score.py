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

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
TRANSACTIONS_filtered_z_score = dataiku.Dataset("TRANSACTIONS_filtered_z_score")
TRANSACTIONS_filtered_z_score.write_with_schema(TRANSACTIONS_prepared_df)