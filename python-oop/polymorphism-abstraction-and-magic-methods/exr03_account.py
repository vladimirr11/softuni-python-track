class Account:
    def __init__(self, owner, amount=0) -> None:
        self.owner = str(owner)
        self.amount = int(amount)
        self._transactions = list()
    
    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')

        self._transactions.append(amount)
    
    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.amount + amount_to_add < 0:
            raise ValueError('sorry cannot go in debt!')
        
        account.add_transaction(amount_to_add)
        return f'New balance: {account.balance}'

    def __str__(self) -> str:
        return f'Account of {self.owner} with starting amount: {self.amount}'
        
    def __repr__(self) -> str:
        return f'{__class__.__name__}({self.owner}, {self.amount})'
    
    def __len__(self):
        return len(self._transactions)
    
    def __getitem__(self, index):
        return self._transactions[index]
    
    def __reversed__(self):
        return reversed(self._transactions)
    
    def __gt__(self, other):
        return self.amount > other.amount
    
    def __ge__(self, other):
        return self.amount >= other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __add__(self, other):
        account = __class__(owner=f'{self.owner}&{other.owner}', amount=self.amount + other.amount)
        account._transactions.extend(self._transactions + other._transactions)

        return account


if __name__ == '__main__':
    acc = Account('bob', 10)
    acc2 = Account('john')

    print(acc)
    print(repr(acc))

    acc.add_transaction(20)
    acc.add_transaction(-20)
    acc.add_transaction(30)

    print(acc.balance)
    print(len(acc))

    for transaction in acc:
        print(transaction)

    print(acc[1])
    print(list(reversed(acc)))

    acc2.add_transaction(10)
    acc2.add_transaction(60)

    print(acc > acc2)
    print(acc >= acc2)
    print(acc < acc2)
    print(acc <= acc2)
    print(acc == acc2)
    print(acc != acc2)

    acc3 = acc + acc2
    print(acc3)
    print(acc3._transactions)
