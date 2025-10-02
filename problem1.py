from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def play(self):
        pass

class FlamesGame(Game):
    def __init__(self, name1, name2):

        self._name1 = name1.lower().replace(" ", "")
        self._name2 = name2.lower().replace(" ", "")

    def _remove_common_letters(self):
        """Remove common letters and return total count of remaining letters."""
        name1_list = list(self._name1)
        name2_list = list(self._name2)

        for char in self._name1:
            if char in name2_list:
                name1_list.remove(char)
                name2_list.remove(char)

        return len(name1_list) + len(name2_list)

    
    def play(self):
        count = self._remove_common_letters()

        if count == 0:
            return "Not compatible! Single forever </3"

        flames = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Sibling"]
        idx = 0

        while len(flames) > 1:
            idx = (idx + count - 1) % len(flames)
            flames.pop(idx)

        return flames[0]


if __name__ == "__main__":
    name1 = input("Enter your name: ")
    name2 = input("Enter partner's name: ")

    game = FlamesGame(name1, name2)
    result = game.play()

    print(f"\nResult: {result}")
