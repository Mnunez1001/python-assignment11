import plotly.express as px
import plotly.data as pldata

# Loading the Plotly wind dataset

df = pldata.wind(return_type="pandas")


# Displaying the first and last 10 rows
print("First 10 rows:")
print(df.head(10))

print("\nLast 10 rows:")
print(df.tail(10))


# Cleaning the strength column

print("\nData types before cleaning:")
print(df.dtypes)


# Removing non-numeric characters and converting to float
df["strength"] = (
    df["strength"]
    .str.replace(r"[^0-9.]", "", regex=True)
    .astype(float)
)


print("\nData types after cleaning:")
print(df.dtypes)

print("\nCleaned Data:")
print(df.head(10))


# Creating an interactive scatter plot

fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Strength vs. Frequency by Direction",
    labels={
        "strength": "Wind Strength",
        "frequency": "Frequency",
        "direction": "Wind Direction"
    }
)


# Saving the plot as an HTML file


fig.write_html("wind.html")


# Displaying the plot
fig.show()


print("\nwind.html created successfully.")