import random
from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def play(self):
        pass


class LotteryGame(Game):
    def __init__(self):
        self._winning_numbers = set()
        self._player_numbers = set()

    def _generate_winning_numbers(self):
        """Randomly generate 6 unique numbers (1–60)."""
        self._winning_numbers = set(random.sample(range(1, 61), 6))

    def _get_player_numbers(self):
        """Allow player to input 6 unique numbers."""
        print("Enter 6 numbers between 1–60:")
        while len(self._player_numbers) < 6:
            try:
                num = int(input(f"Enter number {len(self._player_numbers)+1}: "))
                if num < 1 or num > 60:
                    print("Number must be between 1 and 60.")
                elif num in self._player_numbers:
                    print("Number already chosen.")
                else:
                    self._player_numbers.add(num)
            except ValueError:
                print("Invalid input. Please enter a number.")

    def _calculate_prize(self, matches):
        """Prize calculation based on matches."""
        if matches == 6:
            return 1_000_000
        return matches * 1000

    def play(self):
        self._generate_winning_numbers()
        self._get_player_numbers()

        matches = len(self._winning_numbers & self._player_numbers)
        prize = self._calculate_prize(matches)

        print("\n Lottery Results ")
        print(f"Winning Numbers: {sorted(self._winning_numbers)}")
        print(f"Your Numbers:    {sorted(self._player_numbers)}")
        print(f"Matches: {matches}")
        print(f"Prize: ₱{prize:,}")


if __name__ == "__main__":
    game = LotteryGame()
    game.play()
