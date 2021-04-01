import pandas as pd
import re
from spacy_annotator.pandas_annotations import annotate as pd_annotate

df = pd.read_json('/content/drive/MyDrive/indeed_com-indeed_com_usa_jobs__20200101_20200331/indeed_com-indeed_com-indeed_com_usa_jobs__20200101_20200331_deduped_n_merged_20201027_052329839673037.ldjson', lines=True)
descriptions_train = df['job_description'][0::15]

pd_dd = pd_annotate(df,
            col_text = 'full_text',     # Column in pandas dataframe containing text to be labelled
            labels = ['SKILL'], # List of labels
            sample_size=1,              # Size of the sample to be labelled
            delimiter='~',              # Delimiter to separate entities in GUI
            model = None,               # spaCy model for noisy pre-labelling
            regex_flags=re.IGNORECASE   # One (or more) regex flags to be applied when searching for entities in text
            )