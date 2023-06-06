import pandas as pd
import re

search_pattern = r'\b\d{1,3}[xX][pP]\b'

df = pd.read_csv(r'C:\Users\1948NM\Documents\Technische bedrijfskunde\Jaar 2 - 2017 -2019\Blok 1\Programmeren en visualiseren\VolgordeFinal.csv', delimiter=';')

matched_rows = pd.DataFrame(columns=df.columns)
for col in df.columns:
    matches = df[col].str.findall(search_pattern, flags=re.IGNORECASE)
    for i, match_list in matches.iteritems():
        if match_list:
            matched_rows = matched_rows.append(df.loc[i])

matched_rows.to_csv('matched_rows.csv', index=False)

import pandas as pd
import re

search_pattern = r'\b\d{1,3}(?:XP|xp)\b'

df = pd.read_csv(r'C:\Users\1948NM\Documents\Technische bedrijfskunde\Jaar 2 - 2017 -2019\Blok 1\Programmeren en visualiseren\VolgordeFinal.csv', delimiter=';')

matched_rows = pd.DataFrame(columns=df.columns)
for col in df.columns:
    matches = df[col].str.findall(search_pattern, flags=re.IGNORECASE)
    for i, match_list in matches.iteritems():
        if match_list:
            matched_rows = matched_rows.append(df.loc[i])

matched_rows.to_csv('matched_rows2.csv', index=False)
