class BudgetCategory:
    def __init__(self, budget_name, budget):
        self.__budget_name = budget_name
        self.__budget = budget
        self.__expense = 0

    def budget(self):
        return self.__budget_name 

    def budget(self):
        return self.__budget # returning your total budget

    def new_budget(self, new_budget):
        if new_budget >= 0:
            self.__budget = new_budget
        else:
            print("Budget should be a positive number.")

    def adding_expense(self, amount):
        if amount >= 0: # how much you are spending of your total budget
            self.__expense += amount
        else:
            print("spending amount should be a positive number")

    def display_budget(self):
        remaining_budget = self.__budget - self.__expense
        print(f"Category: {self.__budget_name}")
        print(f"Budget: ${self.__budget}")
        print(f"Expenses: ${self.__expense}")
        print(f"Remaining Budget: ${remaining_budget}")

food_category = BudgetCategory("car parts", 2600)
food_category.adding_expense(1345)
food_category.display_budget()
