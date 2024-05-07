class BudgetCategory:
    def __init__(self, budget_name, budget):
        self.__budget_name = budget_name
        self.__budget = budget
        self.__expense = 0

    def budget(self):
        return self.__budget_name # here I can give the category any name I like according to what I am buying
    
    def budget(self):
        return self.__budget # returning your total budget

    def adding_expense(self, amount):
        if amount >= 0: # how much you are spending of your total budget
            self.__expense += amount
        else:
            print("spending amount should be a positive number")

    def display_budget(self):
        remaining_budget = self.__budget - self.__expense # getting all my budgets and expense so I can subtract them together to get my remaining budget.
        print(f"Category: {self.__budget_name}")
        print(f"Budget: ${self.__budget}")
        print(f"Expenses: ${self.__expense}")
        print(f"Remaining Budget: ${remaining_budget}")

budget_category = BudgetCategory("car parts", 2600)
budget_category.adding_expense(1345)
budget_category.display_budget()
