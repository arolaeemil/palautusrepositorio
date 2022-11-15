class Player:
    def __init__(self, name, goals, assists, nationality):
        self.name = name
        self.goals = goals
        self.assists = assists
        self.nationality = nationality
        self.sorthelp = goals + assists
    
    def __str__(self):
        return f"{self.name:20}" + " goals: " + f"{self.goals:2}" + " assists: " + f"{self.assists:2}"

    def __lt__(self, other):
         return self.sorthelp < other.sorthelp