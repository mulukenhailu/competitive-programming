class ATM:

    def __init__(self):
        self.note = [0, 0, 0, 0, 0]
        self.notes = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, v in enumerate(banknotesCount):
            self.note[i]+=v

    def withdraw(self, amount: int) -> List[int]:
        taken = [0, 0, 0, 0, 0]
        for i in range(4, -1, -1):
            notes = self.notes[i]
            note  = self.note[i]
            if notes > amount:
                pass
            else:
                take = min(note, amount//notes)
                amount -=take*notes
                taken[i]+=take
        if amount > 0:
            return [-1]
        for i, v in enumerate(taken):
            self.note[i]-=v
        return taken

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)