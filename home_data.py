"""First python tries on machine learing"""
import pandas as pd
# from scikit import LinearRegression oder so was

def get_dataframe(filename: str):
    df = pd.read_csv(filename)
    return df

def get_description(df: pd.Dataframe):
    return df.describe()

