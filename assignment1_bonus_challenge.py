# Function returns true if business is profitable
def is_profitable(revenue, cost):
    return revenue > cost

# Function determines product category using match
def get_category(product):
    product = product.strip().lower()

    match product:
        case "electronics" | "gadget":
            return "High Margin"
        case "clothing" | "apparel":
            return "Medium Margin"
        case "food" | "grocery":
            return "Low Margin"
        case _ if product.startswith("tech"):
            return "High Margin"
        case _:
            return "Uncategorized - Review Needed"
        
# Main Function
def main():
    revenue = float(input("Enter business revenue: "))
    cost = float(input("Enter business cost: "))
    product = input("Enter product name: ")

    category = get_category(product)

    if is_profitable(revenue, cost):
        profit = revenue - cost
        print(f"Profitable! Profit: ${profit:.2f}")

        # investment decision based on category of product
        if category == "High Margin":
            decision = "Reinvest"
        elif category == "Medium Margin":
            decision = "Maintain current strategy"
        elif category == "Low Margin":
            decision = "Consider cost reduction"
        else:
            decision = "Review product strategy"

        print(f"Category: {category} | Suggested Action: {decision}")
    else:
        print("Invalid input. Please enter valid revenue, cost, and product name.")

# Run Program
main()