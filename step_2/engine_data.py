import pandas as pd
df = pd.read_csv("engine_data.csv")
print(df.head(5))

filtered = df.loc[df["Sicaklik_C"] > 100]
print("\n",
      filtered)
print("\n","Average pressure in atm is: ",
      df["Basinc_atm"].mean())