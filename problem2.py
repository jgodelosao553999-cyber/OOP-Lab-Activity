from abc import ABC, abstractmethod

class System(ABC):
    @abstractmethod
    def run(self):
        pass


class GradingSystem(System):
    def __init__(self):
        self._grades = []

    def add_grade(self, grade):
        """Adds a valid grade to the list, ignores invalid ones."""
        if 0 <= grade <= 100:
            self._grades.append(grade)
        else:
            print(f"Invalid grade ignored: {grade}")

    def _calculate_average(self):
        """Return average grade (0 if no grades entered)."""
        if not self._grades:
            return 0
        return sum(self._grades) / len(self._grades)

    def _calculate_point_grade(self, avg):
        """Compute point grade formula."""
        return round(((100 - avg) + 10) / 10, 2)

    def _get_remarks(self, avg):
        """Determine remarks based on average."""
        if avg < 50:
            return "Dropped"
        elif avg < 75:
            return "Failed"
        elif 75 <= avg <= 79:
            return "Passed – Satisfactory"
        elif 80 <= avg <= 84:
            return "Passed – Good"
        elif 85 <= avg <= 89:
            return "Passed – Average"
        elif 90 <= avg <= 99:
            return "Passed – Very Good"
        elif avg == 100:
            return "Passed – Excellent"
        else:
            return "Invalid"


    def run(self):
        print("Enter grades (0–100). Enter -1 to finish.")
        while True:
            try:
                grade = int(input("Enter grade: "))
                if grade == -1:
                    break
                self.add_grade(grade)
            except ValueError:
                print("Please enter a valid number.")

        if not self._grades:
            print("No valid grades entered.")
            return

        print("\nGrades Entered:", self._grades)

        avg = self._calculate_average()
        point = self._calculate_point_grade(avg)
        remarks = self._get_remarks(avg)

        print(f"\nAverage Grade: {avg:.2f}")
        print(f"Point Grade: {point:.2f}")
        print(f"Remarks: {remarks}")


if __name__ == "__main__":
    gs = GradingSystem()
    gs.run()
