import pandas as pd

# Sample data
data = {
    'ship_mode': ["Same Day", "First Class", "Standard Class", "Second Class"],
    'sales': [1000, 2000, 1500, 1200],
    'profit': [200, 300, 250, 150]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Define a function to calculate the surcharge based on ship_mode
def calculate_surcharge(ship_mode):
    if ship_mode == "Same Day":
        return 0.2
    elif ship_mode == "First Class":
        return 0.1
    elif ship_mode == "Standard Class":
        return 0.05
    else:
        return 0

# Create a new column 'surcharge' based on the ship_mode
df['surcharge'] = df['ship_mode'].apply(calculate_surcharge)

# Calculate the total cost
df['total_cost'] = (df['sales'] - df['profit']) * (1 + df['surcharge'])

# Print the resulting DataFrame
print(df)