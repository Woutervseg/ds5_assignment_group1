import pandas as pd

#2.1 read the excel file
df = pd.read_excel('hotelBookings.xlsx')

#2.2 inspect the data
# print(df.shape)
# print(df.dtypes)

#er zijn missing values, bijv arrival_date_month, July
print(df.isna().values.any())

#er zijn outliers, bijv 3500 adults

#verkeerde data
#bijv meal, B ipv BB, er staat een 2 bij country ipv obj
#column 'agent', null en NULL zijn niet consistent gebruikt
#stays_in_week_night, staat een float van '4.3' tussen al die integers
#onder binaire colomn, zijn er niet alleen 0 en 1, ook 2 tussen
print(set(df['required_car_parking_spaces']))

#er zijn duplicaties
aantal_duplicaties = len(df[df.duplicated()])






#2.3 
# drop de duplicated rows
df = df.drop_duplicates()
print(len(df))

# afwijking van de outliers zijn te groot



