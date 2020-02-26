import pickle
from scripts.open_utdf_all_days import UTdf
from modules.utils import add_dake_key_column
from modules.config import UT_interval


UTdf.sort_index(inplace=True)
final_df = add_dake_key_column(UTdf, UT_interval)

# exporting the df to a binary file
with open('final_output/UTdf.all_days', 'wb') as f:
    pickle.dump(final_df, f)
f.close()
