import pandas as pd

data = pd.read_json("quotes.json", encoding="utf-8")
data.to_csv("quotes.csv")
