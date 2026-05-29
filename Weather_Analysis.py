import pandas as pd

print("Welcome to Weather Data Analysis!")

try:
    file_path = input("Enter the path to your CSV file: ")

    data = pd.read_csv(file_path)

    print("\nDataset Loaded Successfully!")

    print("\n========== FIRST 5 ROWS ==========")
    print(data.head())

    print("\n========== SHAPE ==========")
    print(data.shape)

    print("\n========== COLUMN NAMES ==========")
    print(data.columns)

    print("\n========== DATA TYPES ==========")
    print(data.dtypes)

    print("\n========== UNIQUE WEATHER CONDITIONS ==========")
    print(data['Weather'].unique())

    print("\n========== NUMBER OF UNIQUE VALUES ==========")
    print(data.nunique())

    print("\n========== COUNT OF NON-NULL VALUES ==========")
    print(data.count())

    print("\n========== WEATHER VALUE COUNTS ==========")
    print(data['Weather'].value_counts())

    print("\n========== DATASET INFO ==========")
    data.info()

    print("\n========== UNIQUE WIND SPEED COUNT ==========")
    print(data['Wind Speed_km/h'].nunique())

    print("\n========== UNIQUE WIND SPEED VALUES ==========")
    print(data['Wind Speed_km/h'].unique())

    print("\n========== WEATHER = CLEAR ==========")
    print(data[data['Weather'] == 'Clear'])

    print("\n========== WIND SPEED = 4 ==========")
    print(data[data['Wind Speed_km/h'] == 4])

    print("\n========== MISSING VALUES ==========")
    print(data.isnull().sum())

    print("\n========== NON-MISSING VALUES ==========")
    print(data.notnull().sum())

    data.rename(columns={'Weather': 'Weather Condition'}, inplace=True)

    print("\n========== UPDATED COLUMN NAMES ==========")
    print(data.columns)

    print("\n========== AVERAGE VISIBILITY ==========")
    print(data['Visibility_km'].mean())

    print("\n========== PRESSURE STANDARD DEVIATION ==========")
    print(data['Press_kPa'].std())

    print("\n========== RELATIVE HUMIDITY VARIANCE ==========")
    print(data['Rel Hum_%'].var())

    print("\n========== WEATHER CONDITION COUNTS ==========")
    print(data['Weather Condition'].value_counts())

    print("\n========== SNOW RECORDS ==========")
    print(data[data['Weather Condition'] == 'Snow'])

    print("\n========== RECORDS CONTAINING SNOW ==========")
    print(data[data['Weather Condition'].str.contains('Snow', na=False)])

    print("\n========== WIND SPEED > 24 AND VISIBILITY = 25 ==========")
    print(
        data[
            (data['Wind Speed_km/h'] > 24) &
            (data['Visibility_km'] == 25)
        ]
    )

    print("\n========== MEAN BY WEATHER CONDITION ==========")
    print(data.groupby('Weather Condition').mean(numeric_only=True))

    print("\n========== MIN BY WEATHER CONDITION ==========")
    print(data.groupby('Weather Condition').min())

    print("\n========== MAX BY WEATHER CONDITION ==========")
    print(data.groupby('Weather Condition').max())

    print("\n========== FOG RECORDS ==========")
    print(data[data['Weather Condition'] == 'Fog'])

    print("\n========== CLEAR OR VISIBILITY > 40 ==========")
    print(
        data[
            (data['Weather Condition'] == 'Clear') |
            (data['Visibility_km'] > 40)
        ]
    )

    print("\n========== COMPLEX CONDITION ==========")
    print(
        data[
            (
                (data['Weather Condition'] == 'Clear') &
                (data['Rel Hum_%'] > 50)
            )
            |
            (data['Visibility_km'] > 40)
        ]
    )

except FileNotFoundError:
    print("Error: CSV file not found.")

except Exception as e:
    print(f"An error occurred: {e}")