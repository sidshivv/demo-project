import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Department": ["HR", "IT", "Finance", "Marketing"],
}
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)


# Filter employees older than 30
older_than_30 = df[df["Age"] > 30]

print("\nEmployees older than 30:")
print(older_than_30)

# Calculate the average age
average_age = df["Age"].mean()
print(f"\nAverage Age: {average_age:.2f}")
