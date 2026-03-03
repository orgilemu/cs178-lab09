
import boto3
from boto3.dynamodb.conditions import Key

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Foods"


def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_food(food):
    FoodName = food.get("FoodName", "Unknown Food")
    Category = food.get("Category", "Unknown Category")
    Calories = food.get("Calories", "Unknown Calories")

    print(f"  FoodName  : {FoodName}")
    print(f"  Category   : {Category}")
    print(f"  Calories: {Calories}")
    print()



def print_all_foods():
    """Scan the entire Foods table and print each item."""
    table = get_table()
    
    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No foods found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} food(s):\n")
    for food in items:
        print_food(food)



def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_foods()


if __name__ == "__main__":
    main()