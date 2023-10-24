import pandas as pd

df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                     'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})

other = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K6'],
                      'B': ['B0', 'B1', 'B2', 'B6']})


xxx = df.join(other.set_index('key'), on='key', how='outer', validate='m:1')

print(xxx)
