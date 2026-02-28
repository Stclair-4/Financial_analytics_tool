class FinancialRatioAgent:
    def __init__(self, financial_statements):
        self.financial_statements = financial_statements

    def calculate_current_ratio(self):
        current_assets = self.financial_statements['current_assets']
        current_liabilities = self.financial_statements['current_liabilities']
        if current_liabilities == 0:
            return float('inf')  # To handle division by zero
        return current_assets / current_liabilities

    def calculate_debt_to_equity_ratio(self):
        total_liabilities = self.financial_statements['total_liabilities']
        shareholder_equity = self.financial_statements['shareholder_equity']
        if shareholder_equity == 0:
            return float('inf')  # To handle division by zero
        return total_liabilities / shareholder_equity

    def calculate_quick_ratio(self):
        quick_assets = self.financial_statements['quick_assets']
        current_liabilities = self.financial_statements['current_liabilities']
        if current_liabilities == 0:
            return float('inf')  # To handle division by zero
        return quick_assets / current_liabilities

# Example usage:
# financial_data = {
#     'current_assets': 100000,
#     'current_liabilities': 50000,
#     'total_liabilities': 70000,
#     'shareholder_equity': 30000,
#     'quick_assets': 70000
# }
# agent = FinancialRatioAgent(financial_data)
# print(agent.calculate_current_ratio())  # Example method call
