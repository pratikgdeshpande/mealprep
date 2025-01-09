import random

# ----------------------
# 1. Define food lists
# ----------------------

veg_protein_list = ["Paneer", "Tofu", "Beans", "Chickpeas", "Tempeh"]
non_veg_protein_list = ["Chicken", "Fish", "Eggs", "Turkey"]
dals_list = ["Toor Dal", "Moong Dal", "Masoor Dal", "Chana Dal"]
salads_list = ["Green Salad", "Greek Salad", "Cucumber-Tomato Salad"]
soups_list = ["Tomato Soup", "Mushroom Soup", "Chicken Clear Soup", "Lentil Soup"]
vegetables_list = ["Broccoli", "Spinach", "Cauliflower", "Mixed Veggies", "Bell Peppers"]
fruits_list = ["Apple", "Banana", "Orange", "Watermelon", "Grapes"]
special_items_list = ["Yogurt", "Raita", "Pickle", "Hummus"]

# Optional: For iteration 2 (calorie and macronutrient data) - placeholders
calorie_data = {
    "Paneer": 120, "Tofu": 80, "Beans": 150, "Chickpeas": 160, "Tempeh": 110,
    "Chicken": 200, "Fish": 180, "Eggs": 155, "Turkey": 220,
    "Toor Dal": 170, "Moong Dal": 150, "Masoor Dal": 140, "Chana Dal": 130,
    "Green Salad": 50, "Greek Salad": 100, "Cucumber-Tomato Salad": 40,
    "Tomato Soup": 90, "Mushroom Soup": 110, "Chicken Clear Soup": 120, "Lentil Soup": 100,
    "Broccoli": 50, "Spinach": 40, "Cauliflower": 50, "Mixed Veggies": 70, "Bell Peppers": 40,
    "Apple": 95, "Banana": 105, "Orange": 62, "Watermelon": 85, "Grapes": 70,
    "Yogurt": 80, "Raita": 70, "Pickle": 15, "Hummus": 100
}

macros_data = {
    # macros_data example in grams of protein/fat/carbs per 100g
    "Paneer":   {"protein": 18, "fat": 21,  "carbs": 3},
    "Tofu":     {"protein": 8,  "fat": 5,   "carbs": 2},
    "Beans":    {"protein": 7,  "fat": 0.5, "carbs": 20},
    "Chicken":  {"protein": 27, "fat": 3,   "carbs": 0},
    # ... fill out for others as needed ...
}

# ------------------------------------------------
# 2. Helper functions to generate meal suggestions
# ------------------------------------------------

def generate_lunch(veg_first=True):
    """
    Generate a lunch meal suggestion. 
    - Possibly always include a Dal.
    - Alternate between veg protein and non-veg protein.
    """
    dal_choice = random.choice(dals_list)
    salad_choice = random.choice(salads_list)
    veg_choice = random.choice(vegetables_list)
    fruit_choice = random.choice(fruits_list)

    if veg_first:
        protein_choice = random.choice(veg_protein_list)
    else:
        protein_choice = random.choice(non_veg_protein_list)

    return f"Protein: {protein_choice}, Dal: {dal_choice}, Salad: {salad_choice}, Veg: {veg_choice}, Fruit: {fruit_choice}"

def generate_dinner(veg_first=True):
    """
    Generate a dinner meal suggestion.
    - Possibly include soup, a protein, vegetables, and a special item.
    """
    soup_choice = random.choice(soups_list)
    veg_choice = random.choice(vegetables_list)
    special_item_choice = random.choice(special_items_list)

    if veg_first:
        protein_choice = random.choice(veg_protein_list)
    else:
        protein_choice = random.choice(non_veg_protein_list)

    return f"Soup: {soup_choice}, Protein: {protein_choice}, Veg: {veg_choice}, Special Item: {special_item_choice}"

def generate_snack():
    """
    Generate a simple snack suggestion.
    """
    # Could be a fruit, handful of nuts, or something else
    return random.choice(["Mixed Nuts", "Fruit Bowl", "Protein Bar", "Yogurt"])

# ---------------------------------------------------------
# 3. Generate a plan for X days (e.g., 30) and print output
# ---------------------------------------------------------

def generate_plan(days=5):
    """
    Generate a plan for a given number of days.
    """
    for day in range(1, days+1):
        # Alternate between veg and non-veg daily (just an example)
        # Day 1: veg, Day 2: non-veg, Day 3: veg, etc.
        if day % 2 == 0:
            veg_first = False
        else:
            veg_first = True

        lunch = generate_lunch(veg_first=veg_first)
        dinner = generate_dinner(veg_first=veg_first)
        snack = generate_snack()  # If you want daily snacks

        print(f"Day {day}")
        print(f"  Lunch:  {lunch}")
        print(f"  Dinner: {dinner}")
        print(f"  Snack:  {snack}")

        # (Iteration 2) Example: Approximate calorie count
        # We'll parse items from lunch/dinner, sum up from calorie_data
        items_today = [item.strip().split(": ")[1] for item in lunch.split(", ")]
        items_today += [item.strip().split(": ")[1] for item in dinner.split(", ")]
        if snack in calorie_data:
            items_today.append(snack)

        total_calories = 0
        for item in items_today:
            if item in calorie_data:
                total_calories += calorie_data[item]

        print(f"  ~Approx. Calories: {total_calories}\n")

# ----------------------------
# 4. Main program
# ----------------------------
if __name__ == "__main__":
    # Generate and print a 30-day plan
    generate_plan(days=5)
