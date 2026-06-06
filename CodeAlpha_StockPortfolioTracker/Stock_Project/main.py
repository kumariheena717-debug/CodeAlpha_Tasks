# CodeAlpha - Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 300,
    "GOOG": 2800,
    "AMZN": 3300
}

portfolio = {}
total_investment = 0

print("📊 Stock Portfolio Tracker")

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        try:
            quantity = int(input("Enter quantity: "))
            portfolio[stock] = quantity
        except ValueError:
            print("❌ Please enter a valid number!")
    else:
        print("❌ Stock not found in database!")

# Calculation
print("\n📈 Portfolio Summary")
print("-" * 30)

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value

    print(f"{stock}: {qty} x {price} = {value}")

print("-" * 30)
print("💰 Total Investment:", total_investment)

# Save to file (optional but good for internship)
with open("portfolio_result.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-" * 30 + "\n")

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        file.write(f"{stock}: {qty} x {price} = {value}\n")

    file.write("-" * 30 + "\n")
    file.write(f"Total Investment: {total_investment}\n")

print("\n✅ Result saved to portfolio_result.txt")