import pandas as pd

def cleanStats(df):
    """
    Cleans shooting stats columns like FG, 3PT, and FT from 'made-attempts' format
    into separate made/attempted columns and calculates shooting percentages.
    """
    stats_to_clean = {
        'FG': ('FGM', 'FGA', 'FG%'),
        '3PT': ('3PTM', '3PTA', '3PT%'),
        'FT': ('FTM', 'FTA', 'FT%')
    }

    for stat, (made_col, att_col, pct_col) in stats_to_clean.items():
        if stat in df.columns:
            split_data = df[stat].str.split('-', expand=True)
            df[made_col] = pd.to_numeric(split_data[0], errors='coerce')
            df[att_col] = pd.to_numeric(split_data[1], errors='coerce')
            df[pct_col] = (df[made_col] / df[att_col]) * 100
            df.drop(columns=[stat], inplace=True)

    return df
