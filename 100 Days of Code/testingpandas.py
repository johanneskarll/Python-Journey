import pandas as pd
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield'])
print(f"df =\n{df}")
print("")
print(f"df.iloc['viper'] =\n{df['viper']}")
print(f"type(df.loc['viper']) =\n{type(df.loc['viper'])}")