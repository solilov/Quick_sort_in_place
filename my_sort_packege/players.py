class Player:
    """
    Класс описывающий модель игрока.
    """
    __slots__ = ('name', 'solved_problems', 'penalty')

    def __init__(self, name, solved_problems, penalty):
        self.name = name
        self.solved_problems = int(solved_problems) * -1
        self.penalty = int(penalty)

    def __lt__(self, other: 'Player') -> bool:
        if self.solved_problems != other.solved_problems:
            return self.solved_problems < other.solved_problems
        if self.penalty != other.penalty:
            return self.penalty < other.penalty
        return self.name < other.name

    def __repr__(self):
        return self.name
