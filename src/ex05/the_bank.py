class Account:
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        self.__odd_args = len(kwargs) % 2 != 0
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError('Attribute value cannot be negative.')
        if not isinstance(self.name, str):
            raise AttributeError('Attribute name must be a str object.')

    def transfer(self, amount):
        self.value += amount

    def is_corrupted(self):
        return not self.__odd_args \
               or any([a.startswith('b') for a in dir(self)]) \
               or all([not a.startswith(('zip', 'addr')) for a in dir(self)]) \
               or not all(a in dir(self) for a in ('name', 'id', 'value')) \
               or not isinstance(self.name, str) \
               or not isinstance(self.id, int) \
               or not isinstance(self.value, (int, float))


class Bank:
    """
    The bank
    """

    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """
        Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occurred
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code ...
        if not isinstance(new_account, Account) or new_account.name in self.accounts:
            return False
        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        """
        Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occurred
        """
        # ... Your code ...
        if not isinstance(origin, str) or not isinstance(dest, str):
            return False
        origin_account = self.get_account_by_name(origin)
        dest_account = self.get_account_by_name(dest)
        if origin_account.is_corrupted() or dest_account.is_corrupted() \
                or amount < 0 or origin_account.value < amount:
            return False
        if origin != dest:
            dest_account.transfer(amount)
            origin_account.transfer(-amount)
        return True

    def fix_account(self, name):
        """
        fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occurred
        """
        # ... Your code ...
        if not isinstance(name, str):
            return False
        account = self.get_account_by_name(name)
        if account is None:
            return False
        if not account.is_corrupted():
            return True
        if not any(attr.startswith(('zip', 'addr')) for attr in dir(account)):
            account.zip = None
        b_attr = [a for a in dir(account) if a.startswith('b')]
        for attr in b_attr:
            account.__dict__[f'_{attr}'] = account.__dict__.pop(attr)
        return not account.is_corrupted()

    def get_account_by_name(self, name: str) -> Account:
        if not isinstance(name, str):
            return None
        for account in self.accounts:
            if name == account.name:
                return account
        return None


if __name__ == '__main__':
    print('--- 01.05.01 ---')
    bank = Bank()
    john = Account('John', zip='1234', brother='James', value=6460.0, ref='23432f32234f324g425542g', info=None,
                   other='This is ...', lol='hihi')
    bank.add(john)
    print(f' Is corrupted john? {john.is_corrupted()}')
    bank.fix_account('John')
    print(f' Fixed: Is corrupted john? {john.is_corrupted()}')
    print('--- 01.05.02 ---')
    james = Account('James', zip='1234', rother='James', value=6460.0, ref='23432f32234f324g425542g', info=None,
                    other='This is ...')
    print(f' Is corrupted james? {james.is_corrupted()}')
    print('--- 01.05.03 ---')
    jeff = Account('Jeff', zip='1234', rother='James', ref='23432f32234f324g425542g', info=None,
                   other='This is ...')
    print(f' Is corrupted jeff? {jeff.is_corrupted()}')
    print('--- 01.05.04 ---')
    bank = Bank()
    bank.add(Account('Jane', zip='911-475', value=1000.0, ref='23432f32234f324f425542f'))
    john = Account('John', zip='911-475', value=1000.0, ref='23432f32234f324c425542b')
    bank.add(john)
    print(' testing a valid transfer')
    print(f'  John value={john.value}')
    print(f"  transfer worked? {bank.transfer('Jane', 'John', 500)}")
    print(f'  John value={john.value}')
    print('--- 01.05.05 ---')
    print(f" transfer worked? {bank.transfer('Jane', 'John', 1000)}")
    print(f' John value={john.value}')
