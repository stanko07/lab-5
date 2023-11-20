class Candidate:

    def __init__(self, name, votes):
        self.name = name
        self.votes = votes

    def get_name(self):
        return self.name

    def get_votes(self):
        return self.votes

    def get_percentage(self, total_votes):
        return self.votes / total_votes * 100

class Elections:
    def __init__(self, candidates):
        self.candidates = candidates

    def get_winner(self):
        winner = self.candidates[0]
        for candidate in self.candidates:
            if candidate.get_votes() > winner.get_votes():
                winner = candidate
        return winner

def main():
    candidates = []
    for i in range(5):
        name = input(f"Введіть ім'я кандидата {i + 1}: ")
        votes = int(input(f"Введіть кількість голосів для кандидата : "))
        candidate = Candidate(name, votes)

    elections = Elections(candidates)
    total_votes = sum(candidate.get_votes() for candidate in candidates)

    for candidate in candidates:
        print(f"Кандидати: {candidate.get_name()}, голосів: {candidate.get_votes()},"
              f" відсоток: {candidate.get_percentage(total_votes):.2f}%")

    print(f"Переможець виборів: {elections.get_winner().get_name()},"
          f" з відсотком : {candidate.get_percentage(total_votes):.2f}% ")

if __name__ == "__main__":
    main()