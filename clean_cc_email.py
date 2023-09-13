import pandas as pd

df = pd.read_excel("C:/Users/patrick/OneDrive - Prime Prime International Limited/ContactList.xlsx")

print("Email")
count = 0
for index, row in df.iterrows():
    if row[7] != 'Yes':
        continue;

    if str(row[2]).find("cinemacity.com.hk") != -1:
        print("Skipping:", row[2])
        continue

    if str(row[2]).find("pegasusmovie.com") != -1:
        print("Skipping:", row[2])
        continue

    count += 1

print ("Total:", count)

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 121301 entries, 0 to 121300
Data columns (total 13 columns):
 #   Column                  Non-Null Count   Dtype
---  ------                  --------------   -----
 0   Member ID               121301 non-null  int64
 1   English Name            96465 non-null   object
 2   Email                   120513 non-null  object
 3   Mobile                  38764 non-null   object
 4   Member Type             121300 non-null  object
 5   Gender                  40367 non-null   object
 6   Birthday                33255 non-null   object
 7   Receive Promotion Mail  121301 non-null  object
 8   Member Card ID          26289 non-null   object
 9   Points                  48693 non-null   float64
 10  Status                  121301 non-null  object
 11  Register Date           121301 non-null  datetime64[ns]
 12  Expiry Date             121301 non-null  datetime64[ns]
dtypes: datetime64[ns](2), float64(1), int64(1), object(9)
memory usage: 12.0+ MB
'''