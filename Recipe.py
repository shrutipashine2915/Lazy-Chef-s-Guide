import streamlit as st
from typing import List

# 🍳 RECIPE DATABASE
recipe_base = {
    "pasta": [
        "1: Boil pasta with salt and a little oil.",
        "2: Saute garlic and onions in olive oil.",
        "3: Add chopped tomatoes and cook into a sauce.",
        "4: Mix in the pasta and add herbs & cheese!"
    ],

    "omelette": [
        "1: Beat the eggs with salt and pepper.",
        "2: Add chopped onions, tomatoes, and green chilies.",
        "3: Pour into a heated pan and cook evenly.",
        "4: Flip and serve with toast!"
    ],

    "salad": [
        "1: Chop cucumber, tomato, onion, and lettuce.",
        "2: Add olive oil, lemon juice, and salt.",
        "3: Toss well and chill before serving.",
        "4: Optionally add nuts or feta cheese!"
    ],

    "sandwich": [
        "1: Spread butter or mayo on bread slices.",
        "2: Add sliced veggies or boiled egg.",
        "3: Sprinkle pepper, salt, and oregano.",
        "4: Toast or grill if desired!"
    ],

    "fried rice": [
        "1: Cook and cool rice beforehand.",
        "2: Saute garlic, onion, and veggies in soy sauce.",
        "3: Add rice and mix well on high heat.",
        "4: Garnish with spring onions and serve hot!"
    ],

    "maggi": [
        "1: Boil 1.5 cups of water.",
        "2: Add Maggi noodles and the tastemaker.",
        "3: Stir occasionally and cook for 2-3 minutes.",
        "4: Optionally add veggies or cheese for extra flavor!"
    ],

    "tea": [
        "1: Add water and milk in a pot (ratio 2:1).",
        "2: Add tea powder, sugar, and crushed ginger/cardamom.",
        "3: Let it boil for 5–6 minutes.",
        "4: Strain and serve hot!"
    ],

    "cold coffee": [
        "1: Add 1 tbsp instant coffee and sugar to a glass.",
        "2: Pour 2 tbsp warm water and mix well.",
        "3: Add chilled milk and ice cubes.",
        "4: Blend or stir vigorously and serve cold!"
    ]
}

# 🧠 RECIPE RECOMMENDER LOGIC
def recommend(ingredients: List[str]):
    matched_recipes = []

    recipe_ingredients = {
        "omelette": ["eggs", "onion", "tomato"],
        "salad": ["lettuce", "cucumber", "tomato"],
        "sandwich": ["bread", "butter", "tomato", "cucumber"],
        "pasta": ["pasta", "onion", "tomato", "cheese"],
        "fried rice": ["rice", "onion", "garlic", "soy sauce", "carrot"],
        "maggi": ["maggi noodles", "water", "tastemaker"],
        "tea": ["milk", "tea powder", "sugar"],
        "cold coffee": ["milk", "coffee", "sugar", "ice cubes"]
    }

    for recipe, required_ingredients in recipe_ingredients.items():
        match_count = len(set(ingredients) & set(required_ingredients))
        if match_count >= 2:  # You can change this threshold
            matched_recipes.append((recipe, match_count))

    if matched_recipes:
        matched_recipes.sort(key=lambda x: x[1], reverse=True)
        st.success("🎉 Based on your ingredients, here are the best recipe matches:")

        for recipe, count in matched_recipes:
            emoji = "🍳" if recipe in ["omelette", "pasta", "fried rice", "maggi"] else "☕" if recipe in ["tea", "cold coffee"] else "🥗"
            st.write(f"{emoji} **{recipe.title()}** — matched {count} ingredients!")
            for step in recipe_base[recipe]:
                st.write(step)
    else:
        st.warning("🤔 No good matches found. Want to add a new recipe?")
        recipe = st.text_input("🍽️ Suggest a recipe name:")
        steps = st.text_area("✍️ Write the recipe steps (each step on new line):")
        add = st.button("➕ Add recipe")
        if add and recipe and steps:
            recipe_base[recipe.lower()] = steps.split('\n')
            st.success("✅ Your recipe has been added! Thank you 💖")


# 🌟 STREAMLIT UI
st.title("🍽️ What's Cooking? – Easy and Quick Recipe  🌟 ")
st.markdown("Select the ingredients you have, and we’ll tell you what you can cook!")

# 🍅 INGREDIENT OPTIONS
options = st.multiselect(
    '🛒 What ingredients do you have?',
    [
        "eggs", "onion", "tomato", "cheese", "pasta", "lettuce", "cucumber", "carrot",
        "bread", "butter", "garlic", "soy sauce", "rice", "olive oil", "green chili",
        "milk", "tea powder", "coffee", "maggi noodles", "sugar", "water", "ice cubes", "cardamom", "ginger", "tastemaker"
    ],
    []
)

# 🎛️ BUTTONS
col1, col2 = st.columns([1, 0.3])
with col1:
    ask = st.button("🍳 Get Recipe")
with col2:
    quit = st.button("❌ Exit")

# 🔍 RESPONSE
if ask:
    recommend(options)
if quit:
    st.write("👋 Thank you for using the Recipe Recommendation System! Come back hungry 😄")
