import customtkinter as ctk

class TaxCalculator:
    def __init__(self):

        # Initialize Our Window
        self.window = ctk.CTk()
        self.window.title('Tax Calculator')
        self.window.geometry('280x280')
        self.window.resizable(False, False)
        self.padding: dict = {'padx': 20, 'pady': 10}

        # Income Label & Entry
        self.income_label = ctk.CTkLabel(self.window, text='Income:')
        self.income_label.grid(column=0, row=0, **self.padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(column=1, row=0, **self.padding)

        # Tax Label & Entry
        self.tax_rate_label = ctk.CTkLabel(self.window, text='Percent:')
        self.tax_rate_label.grid(column=0, row=1, **self.padding)
        self.tax_rate_entry = ctk.CTkEntry(self.window)
        self.tax_rate_entry.grid(column=1, row=1, **self.padding)

        # Result Label & Entry
        self.result_label = ctk.CTkLabel(self.window, text='Tax:')
        self.result_label.grid(column=0, row=2, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0,0)
        self.result_entry.grid(column=1, row=2, **self.padding)

        # Calculate Button
        self.calculate_button = ctk.CTkButton(self.window, text='Calculate', command=self.calculate_tax)
        self.calculate_button.grid(column=1, row=3, **self.padding)

    def update_result(self, text: str):
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def calculate_tax(self):
        try:
            income: float = float(self.income_entry.get())
            tax_rate: float = float(self.tax_rate_entry.get())
            self.update_result(f'${income * (tax_rate / 100):,.2f}')
        except ValueError:
            self.update_result('Invalid Input')

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()


# Potential add-ons
  # 1. Add log messages
  # 2. What is happening during the CTK generation
  # 3. Add some extra functionality