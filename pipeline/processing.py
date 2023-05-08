import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Return the Dataframe created from the csv other input cleaning steps would be done here."""
    data = pd.read_csv(path, parse_dates=["registration_date", "last_active"])
    return data


def verify_data(path: str):
    """Verifies the null values in the table and calculates the days without registrations per year"""
    # Years to count days for
    years_to_count = range(2015, 2022)

    df = load_data(path)
    print(df[["user_id", "country", "registration_date"]].iloc[:5])

   # Calculate the percentage of null values in each column
    pct_null_values = df.isnull().mean() * 100

    print("**************************************************")
    print("                   Data Report                   \n")
    
    # Output the result
    print("Percentage of null values in each column:")
    print(pct_null_values)

    print("\n\n")

    for year_to_count in years_to_count:
        # Filter DataFrame to rows with registration date in the specified year
        df_filtered = df[df["registration_date"].dt.year == year_to_count]

        # Count the number of unique days with registrations
        num_registered_days = len(df_filtered["registration_date"].dt.date.unique())

        # Count the total number of days in the year
        num_days = pd.Timestamp(year_to_count + 1, 1, 1) - pd.Timestamp(
            year_to_count, 1, 1
        )

        # Output the result
        print(
            f"Number of days in {year_to_count} without registrations: {num_days.days - num_registered_days}"
        )


if __name__ == "__main__":
    table_path = "data/table.csv"
    verify_data(table_path)
