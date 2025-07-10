"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd



def main():
    # Use a raw string for Windows file path
    frame = pd.read_csv(r'C:\Users\juliu\CPE106L-4_E03_GRP5-LabExercisesRepo\LAB7\POSTLAB\PE6\cleanbrogdonstats.csv')
    frame = cleanStats(frame)
    view = HoopStatsView(frame)
    view.mainloop()

def cleanStats(df):
    import numpy as np
    stats_to_clean = [
        ('FG', 'FGM', 'FGA', 'FG%'),
        ('3PT', '3PTM', '3PTA', '3PT%'),
        ('FT', 'FTM', 'FTA', 'FT%')
    ]
    for stat, made_col, att_col, pct_col in stats_to_clean:
        if stat in df.columns:
            # Split the <makes-attempts> string into two columns
            split_data = df[stat].str.split('-', expand=True)
            df[made_col] = pd.to_numeric(split_data[0], errors='coerce')
            df[att_col] = pd.to_numeric(split_data[1], errors='coerce')
            # Calculate percentage, handle division by zero
            df[pct_col] = np.where(df[att_col] > 0, (df[made_col] / df[att_col]) * 100, np.nan)
            # Remove the original column
            df.drop(columns=[stat], inplace=True)
    return df

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
