import csv

# Set the path to your budget_data.csv file
csvpath = r'Resources\budget_data.csv'

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

# Read the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)

    # Loop through the rows in the dataset
    for row in csvreader:
        # Extract data from the row
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total months and net total
        total_months += 1
        net_total += profit_loss

        # Calculate profit/loss changes
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)
            months.append(date)

        # Update previous profit/loss
        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Find the greatest increase and decrease
greatest_increase = max(profit_loss_changes)
greatest_increase_date = months[profit_loss_changes.index(greatest_increase)]
greatest_decrease = min(profit_loss_changes)
greatest_decrease_date = months[profit_loss_changes.index(greatest_decrease)]

# Format the results
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${round(average_change, 2)}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"
)

# Print the results
print(output)