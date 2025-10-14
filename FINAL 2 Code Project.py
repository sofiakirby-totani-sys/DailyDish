import tkinter as tk
from tkinter import messagebox
import random
import webbrowser

# List of recipes and their ingredients
recipes = {
    "Bangers and Mash": ["sausages", "potatoes", "butter", "milk", "salt", "pepper", "beefstock", "garlic","onion", "flour"],
    "Lasagna": ["lasagna sheets", "ground beef", "onionn", "garlic", "tomato paste", "carrot", "celery","canned crushed tomato" "beef cubes", " bay leaves", "Worcestershire Sauce", "mozzarella cheese", "parmisan", "milk", "flour", "butter"],
    "Honey Soy Chicken Fried Rice": ["chicken", "rice", "soy sauce", "honey", "eggs", "peas", "carrot", "onion", "garlic", "hoisin sauce"],
    "Beef Stirfry": ["beef strips", "cornstarch", "soy sauce", "oyster sauce", "mirin", "seasame oil", "peanut oil", "garlic", "capsicum", "onion","carrot", "bok choy", "shallot", "noodles"],
    "Chicken Curry": ["chicken", "garlic", "chopped tomatoes", "onion", "spice paste", "ginger", "greek yoghurt", "oil"]
}

# Corresponding recipe links
links = {
    "Bangers and Mash": "https://www.recipetineats.com/bangers-and-mash-sausage-with-onion-gravy/#recipe",
    "Lasagna": "https://www.recipetineats.com/lasagna/",
    "Honey Soy Chicken Fried Rice": "https://robinmillercooks.com/f/honey-soy-chicken-fried-rice",
    "Beef Stirfry": "https://www.recipetineats.com/easy-classic-chinese-beef-stir-fry/",
    "Chicken Curry": "https://www.bbcgoodfood.com/recipes/easy-chicken-curry",
}
#randonly selects a recipe from the list of recipes
def get_recipe():
    """Randomly select a recipe."""
    return random.choice(list(recipes.keys()))
# this code gets the ingredients for the selected recipe
def get_ingredients(recipe):
    """Retrieve ingredients for a given recipe."""
    return recipes.get(recipe, [])

def get_link(recipe):
    """Retrieve link for a given recipe."""
    return links.get(recipe, "#")
# This is what creates the GUI for the user to interact with and see the recipe suggestions, its the visual display for the code to be intereacted with.
class RecipeApp:
    def __init__(self, master):
        self.master = master
        master.title("DailyDish")

        self.selected_recipe = None

        # This is what customises the prompt label colours and size 
        self.prompt_label = tk.Label(
            master,
            text="Your prompt text here",
            wraplength=600,
            justify=tk.LEFT,
            fg="White",        # This is the text that asks the user if they would like to keep the recipe
            bg="Light pink"  # This the background colour of the prompt label
        )
        self.prompt_label.pack(padx=10, pady=10)

        # The box for typing yes/no to the recipe suggestion
        self.entry = tk.Entry(master, width=20, bg="#ffe6f2", fg="black", insertbackground="white")
        self.entry.pack(padx=10, pady=5)
        self.entry.bind("<Return>", self.on_submit)

        # Submit button
        self.btn_submit = tk.Button(master, text="Submit", command=self.on_submit)
        self.btn_submit.pack(padx=10, pady=5)

        # Result label (ingredients)
        self.result_label = tk.Label(master, text="", justify=tk.LEFT, anchor="w")
        self.result_label.pack(padx=10, pady=10)

        # Recipe link label this is where the hand curser appears to show its clickable
        self.link_label = tk.Label(master, text="", fg="pink", cursor="hand2", justify=tk.LEFT)
        self.link_label.pack(padx=10, pady=5)

        self.ask_new_recipe()
# This function suggests a new recipe to the user and the prompt is dependent based on the users iput that is handled in the on_submit function (yes/no)
    def ask_new_recipe(self):
        """Suggest a new recipe."""
        self.selected_recipe = get_recipe()
        self.prompt_label.config(
            text=f"How about making *{self.selected_recipe}* for dinner tonight?\n"
                 "Would you like to keep this recipe? (yes / no):"
        )
        self.entry.delete(0, tk.END)
        self.entry.config(state=tk.NORMAL)
        self.btn_submit.config(state=tk.NORMAL)
        self.result_label.config(text="")
        self.link_label.config(text="")
        self.entry.focus_set()

    def on_submit(self, event=None):
        """Handle yes/no responses."""
        user_response = self.entry.get().strip().lower()
        if user_response == "yes":
            ingredients = get_ingredients(self.selected_recipe)
            link = get_link(self.selected_recipe)

            text = f"For dinner tonight you're having: {self.selected_recipe}\n\nIngredients you'll need:\n"
            for ing in ingredients:
                text += f" - {ing}\n"

            self.result_label.config(text=text)

            # This is where people can click to access the website with the full recipe for their meal. The link is stored in the links dictionary at the start of the code.
            self.link_label.config(text="Click here for the full recipe with instructions", fg="purple", cursor="hand2")
            self.link_label.bind("<Button-1>", lambda e: webbrowser.open_new(link))

            self.entry.config(state=tk.DISABLED)
            self.btn_submit.config(state=tk.DISABLED)

        elif user_response == "no":
            self.ask_new_recipe()

        else:
            messagebox.showwarning("Invalid Input", "Please enter 'yes' or 'no'.")
            self.entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()