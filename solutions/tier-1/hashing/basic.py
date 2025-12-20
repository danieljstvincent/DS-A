import requests

# Endpoint URLs
CATEGORIES_ENDPOINT = "https://www.themealdb.com/api/json/v1/1/categories.php"
FILTER_BY_CATEGORY_ENDPOINT = "https://www.themealdb.com/api/json/v1/1/filter.php?c="
MEAL_DETAILS_ENDPOINT = "https://www.themealdb.com/api/json/v1/1/lookup.php?i="

def fetch_categories():
    """
    Fetches a list of meal categories from the API.
    Returns:
        list: A sorted list of category names (strings).
    """

    response = requests.get(CATEGORIES_ENDPOINT)
    print(response)
    data = response.json()
    
    # Extract category names and sort them alphabetically
    categories = sorted([category['strCategory'] for category in data['categories']])
    return categories

def fetch_meals_by_category(category):
    """
    Fetches meals for a given category.
    Args:
        category (str): The category name.
    Returns:
        list: A list of dictionaries with meal information (sorted alphabetically by meal name).
    """
    url = FILTER_BY_CATEGORY_ENDPOINT + category
    response = requests.get(url)
    data = response.json()
    
    # Filter out null or empty meal names and sort alphabetically by name
    meals = sorted(
        [meal for meal in data['meals'] if meal['strMeal']], 
        key=lambda meal: meal['strMeal']
    )
    return meals

def fetch_meal_details(meal_id):
    """
    Fetches detailed information for a given meal by its ID.
    Args:
        meal_id (str): The meal ID.
    Returns:
        dict: A dictionary containing the meal's name, instructions, ingredients, and measurements.
    """
    url = MEAL_DETAILS_ENDPOINT + meal_id
    response = requests.get(url)
    data = response.json()
    
    # Extract meal details
    meal_data = data['meals'][0]
    meal_details = {
        "name": meal_data.get("strMeal", "N/A"),
        "instructions": meal_data.get("strInstructions", "N/A"),
        "ingredients": []
    }
    
    # Gather ingredients and measurements, filtering out null/empty values
    for i in range(1, 21):
        ingredient = meal_data.get(f"strIngredient{i}")
        measurement = meal_data.get(f"strMeasure{i}")
        
        if ingredient and ingredient.strip():  # Check if ingredient is not null or empty
            meal_details["ingredients"].append({
                "ingredient": ingredient.strip(),
                "measurement": measurement.strip() if measurement else ""
            })
    
    return meal_details

def display_meal_details(meal_id):
    """
    Displays the details of a meal including its name, instructions, and ingredients.
    Args:
        meal_id (str): The ID of the meal.
    """
    meal_details = fetch_meal_details(meal_id)
    
    # Print meal name
    print("Meal Name:", meal_details["name"])
    print("\nInstructions:\n", meal_details["instructions"])
    print("\nIngredients:")
    for ingredient in meal_details["ingredients"]:
        print(f"{ingredient['ingredient']} - {ingredient['measurement']}")

def main():
    # Step 1: Fetch and display categories
    categories = fetch_categories()
    print("Categories:\n", categories)
    
    # Step 2: Fetch and display meals for each category
    for category in categories:
        print(f"\nCategory: {category}")
        meals = fetch_meals_by_category(category)
        for meal in meals:
            print("  -", meal["strMeal"])

    # Step 3: Fetch and display details for a specific meal (Example with a sample ID)
    sample_meal_id = "52772"  # You can replace this with any valid meal ID
    print("\nDetails of Selected Meal:")
    display_meal_details(sample_meal_id)
# Run the main function to execute the program

if __name__ == "__main__":
    main()
