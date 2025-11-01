
# DailyDish is a meal plan suggestion tool using GUI with Tkinter.

#This code chooses a random recipe from a predefined dictionary,and prompts the user with a GUI window with options for recipes to make and the ingredients needed, with a checklist to tick off ingredients as they are gathered.

import tkinter as tk
from tkinter import messagebox
import random
import webbrowser

# this dictionary holds recipe names as keys and lists of ingredients as values

recipes = {
    "Banger and Mash": ["sausages", "potatoes", "butter", "milk", "salt", "pepper",
                            "beefstock", "garlic", "onion", "flour"],
    "Lasagna": ["lasagna sheets", "ground beef", "onion", "garlic", "tomato paste",
                    "carrot", "celery", "canned crushed tomato", "beef cubes",
                    "bay leaves", "Worcestershire Sauce", "mozzarella cheese",
                    "parmesan", "milk", "flour", "butter"],
    "Honey Soy Chicken Fried Rice": ["chicken", "rice", "soy sauce", "honey", "eggs",
                                        "peas", "carrot", "onion", "garlic", "hoisin sauce"],
    "Beef Stirfry": ["beef strips", "cornstarch", "soy sauce", "oyster sauce", "mirin", 
                    "sesame oil", "peanut oil", "garlic", "capsicum", "onion",
                    "carrot", "bok choy", "shallot", "noodles"], 
    "Chicken Curry": ["chicken", "garlic", "chopped tomatoes", "onion", "spice paste",
                        "ginger", "greek yoghurt", "oil"],
    "Pasta Carbonara": ["spaghetti", "eggs", "parmesan cheese", "pancetta", "black pepper",
                        "garlic", "olive oil", "salt"  ]      
}

# this dictionary holds recipe names as keys and URL links as values

links = {
    "Bangers and Mash": "https://www.recipetineats.com/bangers-and-mash-sausage-with-onion-gravy/#recipe",
    "Lasagna": "https://www.recipetineats.com/lasagna/",
    "Honey Soy Chicken Fried Rice": "https://robinmillercooks.com/f/honey-soy-chicken-fried-rice",
    "Beef Stirfry": "https://www.recipetineats.com/easy-classic-chinese-beef-stir-fry/",
    "Chicken Curry": "https://www.bbcgoodfood.com/recipes/easy-chicken-curry",
}

# This is what randomly selects a recipe from the dictionary above, it retrieves the ingredients and correspnding link when the user input states 'yes'.

def get_recipe():
    # retrives the ingreidents for the corresponding recipe 
    return random.choice(list(recipes.keys()))

def get_ingredients(recipe):
    """Retrieve ingredients for a given recipe."""
    return recipes.get(recipe, [])

def get_link(recipe):
    """Retrieve link for a given recipe."""
    return links.get(recipe, "#")

class RecipeApp:
    def __init__(self, master):
        self.master = master
        master.title("DailyDish")

        self.selected_recipe = None
        self.check_vars = []    
        #this is what creates the checkbutton that will be the checkbox widget imported from tkinter

        self.checkbuttons = []  

        #this is the prompt label that will display the recipe suggestion to the user, which can be customised further

        self.prompt_label = tk.Label(
            master,
            text="Your prompt text here",
            wraplength=600,
            justify=tk.LEFT,
            fg="White",
            bg="orange"
        )
        self.prompt_label.pack(padx=10, pady=10)

        self.entry = tk.Entry(master, width=20, bg="#ffe6f2", fg="black", insertbackground="white")
        self.entry.pack(padx=10, pady=5)
        self.entry.bind("<Return>", self.on_submit)

        self.btn_submit = tk.Button(master, text="Submit", command=self.on_submit)
        self.btn_submit.pack(padx=10, pady=5)

        self.result_label = tk.Label(master, text="", justify=tk.LEFT, anchor="w")
        self.result_label.pack(padx=10, pady=10)

    # Frame that will hold the checklist of ingredients
        self.checklist_frame = tk.Frame(master)
        self.checklist_frame.pack(padx=10, pady=10, fill=tk.X)

    # Link label at the bottom
        self.link_label = tk.Label(master, text="", fg="purple", cursor="hand2", justify=tk.LEFT)
        self.link_label.pack(padx=10, pady=5)

        self.ask_new_recipe()

# this function is what asks the user if they want to keep the suggested recipe or not 

    def ask_new_recipe(self):
        """Suggest a new recipe."""
        self.selected_recipe = get_recipe()
        self.prompt_label.config(
            text=f"How about making *{self.selected_recipe}* for dinner tonight?\n"
                 "Would you like to keep this recipe? (yes / no):"
        )

# the entry box is cleared and re enabled for the user input to type their response 

        self.entry.delete(0, tk.END)
        self.entry.config(state=tk.NORMAL)
        self.btn_submit.config(state=tk.NORMAL)
        self.result_label.config(text="")
        self.link_label.config(text="")
    # Clear any existing checkboxes
        self.clear_checklist()
        self.entry.focus_set()

# this removes the old checkboxes that were created from the recipe prior 

    def clear_checklist(self):
    # this removes the old checkboxes that were created from the recipe prior 
        for cb in self.checkbuttons:
            cb.destroy()
        self.checkbuttons.clear()
        self.check_vars.clear()
# this is what builds the checklist for the ingredients needed for the selected recipe

    def build_checklist(self, ingredients):
        
    # this creates the checkboxes for the ingredients in the list     
        self.clear_checklist()

# the for ing in loop means that for each ingredient in the ingredients list, a new checkbox will be created with an associated control variable to track its state (checked or unchecked).
        for ing in ingredients:
            var = tk.IntVar()
            chk = tk.Checkbutton(self.checklist_frame, text=ing, variable=var)
            chk.pack(anchor="w")
            self.check_vars.append((ing, var))
            self.checkbuttons.append(chk)
# this function responds to the user input when the submit button is clicked, or enter is pressed on keyboard. 
    def on_submit(self, event=None):

#this
        user_response = self.entry.get().strip().lower()
        if user_response == "yes":
            ingredients = get_ingredients(self.selected_recipe)
            link = get_link(self.selected_recipe)

            # Build checklist
            self.build_checklist(ingredients)
#this displays the relavent information to the user about the recipe thats been selected           

            text = f"For dinner tonight you're having: {self.selected_recipe}\n" \
                   "Click the checkboxes below to mark which ingredients you have or will buy."
            self.result_label.config(text=text)

    
            self.link_label.config(text="Click here for the full recipe with instructions")
            self.link_label.bind("<Button-1>", lambda e: webbrowser.open_new(link))

            self.entry.config(state=tk.DISABLED)
            self.btn_submit.config(state=tk.DISABLED)
# this is the else if statement that handles the input from user of either yes or no 
        elif user_response == "no":
            self.ask_new_recipe()

        else:
            messagebox.showwarning("Invalid Input", "Please enter 'yes' or 'no'.")
            self.entry.delete(0, tk.END)

# this defines the main function to start the program with the tkinter GUI window
def main():
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()

if __name__ == "_main_":
    main()

