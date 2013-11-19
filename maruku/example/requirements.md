## Requirements ##

reqdef(ID001.001.001, `When the Coffee Maker is not in use it waits for user input. There are six different options of user input: 1) add recipe, 2) delete a recipe, 3) edit a recipe, 4) add inventory, 5) check inventory, and 6) purchase beverage.')

reqdef(ID001.001.002, `Only three recipes may be added to the CoffeeMaker. A recipe consists of a name, price, units of coffee, units of milk, units of sugar, and units of chocolate. Each recipe name must be unique in the recipe list. Price must be handled as an integer. A status message is printed to specify if the recipe was successfully added or not. Upon completion, the CoffeeMaker is returned to the waiting state.')

reqdef(ID001.001.003, `A recipe may be deleted from the CoffeeMaker if it exists in the list of recipes in the CoffeeMaker. The recipes are listed by their name. Upon completion, a status message is printed and the Coffee Maker is returned to the waiting state.')

reqdef(ID001.001.004, `A recipe may be edited in the CoffeeMaker if it exists in the list of recipes in the CoffeeMaker. The recipes are listed by their name. After selecting a recipe to edit, the user will then enter the new recipe information. A recipe name may not be changed. Upon completion, a status message is printed and the Coffee Maker is returned to the waiting state.')

reqdef(ID001.001.005, `Inventory may be added to the machine at any time from the main menu, and is added to the current inventory in the CoffeeMaker. The types of inventory in the CoffeeMaker are coffee, milk, sugar, and chocolate. The inventory is measured in integer units. Inventory may only be removed from the CoffeeMaker by purchasing a beverage. Upon completion, a status message is printed and the CoffeeMaker is returned to the waiting state.')

reqdef(ID001.001.006, `Inventory may be checked at any time from the main menu. The units of each item in the inventory are displayed. Upon completion, the Coffee Maker is returned to the waiting state.')

reqdef(ID001.001.007, `The user selects a beverage and inserts an amount of money. The money must be an integer. If the beverage is in the RecipeBook and the user paid enough money the beverage will be dispensed and any change will be returned. The user will not be able to purchase a beverage if they do not deposit enough money into the CoffeeMaker. A user's money will be returned if there is not enough inventory to make the beverage. Upon completion, the Coffee Maker displays a message about the purchase status and is returned to the main menu.')

