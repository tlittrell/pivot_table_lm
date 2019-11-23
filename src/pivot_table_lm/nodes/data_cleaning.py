import pandas as pd
import numpy as np


def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    # Replace '?' with nans
    cols = ["normalized_losses", "bore", "stroke", "horsepower", "peak_rpm", "price"]
    df[cols] = df[cols].replace(to_replace="?", value=np.nan)

    # Update dtypes
    df = df.astype({col: float for col in cols})

    return df
