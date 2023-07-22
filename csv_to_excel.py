import pandas as pd


def csv_to_excel(csv_file, excel_file):
    df = pd.read_csv(csv_file)
    with pd.ExcelWriter(excel_file) as writer:
        df.to_excel(writer)
