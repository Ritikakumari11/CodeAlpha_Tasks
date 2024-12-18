# Create a stock portfolio tracking tool that allows users to add, remove, and track the performance of their stock investments. Utilize financial APIs for real-time stock data.

def get_stock_data(ticker):
    # Placeholder function to simulate fetching stock data
    # In a real application, this function would fetch data from an API
    return {"currentPrice": 100}  # Placeholder value for current price

def add_stock(portfolio, ticker, shares):
    stock_data = get_stock_data(ticker)
    portfolio[ticker] = {"ticker": ticker, "shares": shares, "price": stock_data["currentPrice"]}

def remove_stock(portfolio, ticker):
    if ticker in portfolio:
        del portfolio[ticker]
    else:
        print(f"{ticker} not found in the portfolio.")

def update_portfolio(portfolio):
    total_value = 0
    for ticker, stock in portfolio.items():
        stock_data = get_stock_data(ticker)
        stock["price"] = stock_data["currentPrice"]
        stock["value"] = stock.get("shares", 0) * stock.get("price", 0)  # Calculate and add 'value' key
        total_value += stock["value"]
    return total_value

def display_portfolio(portfolio):
    print("Portfolio:")
    for stock in portfolio.values():
        print(f"{stock['ticker']} ({stock['shares']} shares) - ${stock['price']:.2f} - ${stock['value']:.2f}")
    print(f"Total value: ${update_portfolio(portfolio):.2f}")

def main():
    portfolio = {}

    while True:
        print("\nOptions:")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. Update portfolio")
        print("4. Display portfolio")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            ticker = input("Enter the stock ticker: ")
            shares = float(input("Enter the number of shares: "))
            add_stock(portfolio, ticker, shares)
            print(f"{ticker} added to the portfolio.")

        elif choice == "2":
            ticker = input("Enter the stock ticker to remove: ")
            remove_stock(portfolio, ticker)

        elif choice == "3":
            update_portfolio(portfolio)
            print("Portfolio updated.")

        elif choice == "4":
            update_portfolio(portfolio)  # Ensure portfolio is updated before displaying
            display_portfolio(portfolio)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__== "__main__":
     main()
     