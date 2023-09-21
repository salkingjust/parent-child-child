# P
class Sport:
    def __init__(self, name, players):
        self.name = name
        self.players = players

    def describe(self):
        print(f"This is {self.name}.")
        print(f"It is played by {self.players} players.")

class Football(Sport):
    def __init__(self, name, players, pitch_size):
        super().__init__(name, players)
        self.pitch_size = pitch_size

    def describe(self):
        super().describe()
        print(f"It is played on a {self.pitch_size} meter long field.")

class Basketball(Football):
    def __init__(self, name, players, pitch_size, court_size):
        super().__init__(name, players, pitch_size)
        self.court_size = court_size

    def describe(self):
        super().describe()
        print(f"It is also played on a {self.court_size} square meter court.")

soccer = Football("Soccer", 11, 100)
basketball = Basketball("Basketball", 5, 90, 28)

soccer.describe()
print("\n")
basketball.describe()
