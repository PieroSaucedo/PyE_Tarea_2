from random import randint


def roll_die():
    return randint(1, 6)


def juan_rolls():
    first_die, second_die = roll_die(), roll_die()
    match (first_die, second_die):
        case (4, 1 | 2 | 3):
            second_die = roll_die()
        case (1 | 2 | 3, 4):
            first_die = roll_die()
        case _:
            first_die, second_die = roll_die(), roll_die()
    return first_die, second_die


def calculate_score(first_die, second_die):
    match first_die, second_die:
        case (4, 1):
            return 1
        case (1, 4):
            return 1
        case (4, 2):
            return 2
        case (2, 4):
            return 2
        case (4, 3):
            return 3
        case (3, 4):
            return 3
        case (4, 4):
            return 4
        case (4, 5):
            return 5
        case (5, 4):
            return 5
        case (6, 4):
            return 6
        case (4, 6):
            return 6
        case _:
            return 0


def maria_rolls(score):
    first_die, second_die = roll_die(), roll_die()
    match (first_die, second_die, score):
        case (4, second_die, score) if second_die <= score:
            second_die = roll_die()
        case (first_die, 4, score) if first_die <= score:
            first_die = roll_die()
        case _:
            first_die, second_die = roll_die(), roll_die()
    return first_die, second_die


def determinate_winner(juan_score, maria_score):
    if juan_score > maria_score:
        return 0
    elif juan_score < maria_score:
        return 1
    elif juan_score == maria_score:
        return 2


def calculate_relative_frequencies(times):
    juan_wins = 0
    maria_wins = 0
    draws = 0

    for i in range(times):
        juan_first_die, juan_second_die = juan_rolls()
        juan_score = calculate_score(juan_first_die, juan_second_die)

        maria_first_die, maria_second_die = maria_rolls(juan_score)
        maria_score = calculate_score(maria_first_die, maria_second_die)

        match determinate_winner(juan_score, maria_score):
            case 0:
                juan_wins += 1
            case 1:
                maria_wins += 1
            case 2:
                draws += 1

    total = juan_wins + maria_wins + draws
    juan_wins_relative_frequency = juan_wins/total
    maria_wins_relative_frequency = maria_wins/total
    draws_relative_frequency = draws/total
    return juan_wins_relative_frequency, maria_wins_relative_frequency, draws_relative_frequency


def main():
    relative_frequencies_thousand = calculate_relative_frequencies(int(1000))
    relative_frequencies_ten_thousand = calculate_relative_frequencies(int(10000))
    relative_frequencies_hundred_thousand = calculate_relative_frequencies(int(100000))

    print(f"Frequencia relativa para victorias de Juan (1000 juegos): {relative_frequencies_thousand[0]}")
    print(f"Frequencia relativa para victorias de Maria (1000 juegos): {relative_frequencies_thousand[1]}")
    print(f"Frequencia relativa para empates (1000 juegos): {relative_frequencies_thousand[2]}")
    print("\n")
    print(f"Frequencia relativa para victorias de Juan (10000 juegos): {relative_frequencies_ten_thousand[0]}")
    print(f"Frequencia relativa para victorias de Maria (10000 juegos): {relative_frequencies_ten_thousand[1]}")
    print(f"Frequencia relativa para empates (10000 juegos): {relative_frequencies_ten_thousand[2]}")
    print("\n")
    print(f"Frequencia relativa para victorias de Juan (100000 juegos): {relative_frequencies_hundred_thousand[0]}")
    print(f"Frequencia relativa para victorias de Maria (100000 juegos): {relative_frequencies_hundred_thousand[1]}")
    print(f"Frequencia relativa para empates (100000 juegos): {relative_frequencies_hundred_thousand[2]}")


if __name__ == '__main__':
    main()
