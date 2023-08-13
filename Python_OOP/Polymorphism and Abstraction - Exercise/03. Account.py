class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount: int):
        if self.amount + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        self._transactions.append(transaction_amount)
        self.amount += transaction_amount
        return f"New balance: {self.amount}"

    def add_transaction(self, amount):
        if type(amount) != int:
            raise ValueError("please use int for amount")
        return self.handle_transaction(amount)

    def balance(self):
        return self.amount

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __reversed__(self):
        return reversed(self._transactions)

    def __add__(self, other):
        owner = f"{self.owner}&{other.owner}"
        amount = self.amount + other.amount
        transactions = self._transactions + other._transactions
        Account(owner, amount)._transactions.append(transactions)
        return Account(owner, amount)

    def __lt__(self, other):
        return self.amount < other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __ne__(self, other):
        return self.amount != other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

