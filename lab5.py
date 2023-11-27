class Candidate:

    def __init__(self, name, votes):
        self.__name = name
        self.__votes = votes

    def get_name(self):
        return self.__name

    def get_votes(self):
        return self.__votes

    def set_name(self, new_name):
        self.__name = new_name

    def set_votes(self, new_votes):
        self.__votes = new_votes

    def get_percentage(self, total_votes):
        return self.__votes / total_votes * 100


class Elections:
    def __init__(self, candidates):
        self.__candidates = candidates

    def get_candidates(self):
        return self.__candidates

    def get_winner(self):
        winner = self.__candidates[0]
        for candidate in self.__candidates:
            if candidate.get_votes() > winner.get_votes():
                winner = candidate
        return winner


def main():
    candidates = []
    for i in range(5):
        name = input(f"Введіть ім'я кандидата {i + 1}: ")
        votes = int(input(f"Введіть кількість голосів для кандидата: "))
        candidate = Candidate(name, votes)
        candidates.append(candidate)

    elections = Elections(candidates)
    total_votes = sum(candidate.get_votes() for candidate in candidates)

    for candidate in candidates:
        print(f"Кандидати: {candidate.get_name()}, голосів: {candidate.get_votes()},"
              f" відсоток: {candidate.get_percentage(total_votes):.2f}%")

    winner = elections.get_winner()
    print(f"Переможець виборів: {winner.get_name()},"
          f" з відсотком: {winner.get_percentage(total_votes):.2f}% ")


if __name__ == "__main__":
    main()
