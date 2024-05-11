from random import randint


# Esta función devuelve un número aleatorio entre 1 y 6, simulando la tirada
# de un solo dado.
def roll_die():
    return randint(1, 6)


# Esta función simula una tirada de dados de Juan, si al menos uno de los
# dados es un 4, Juan vuelve a tirar el dado que no es un 4, en caso contrario,
# vuelve a tirar ambos dados (una única vez).
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


# Esta función simula una tirada de dados de María siguiendo su estrategia.
# Si alguno de los dados es menor o igual a la puntuación de Juan,
# María puede volver a tirar ese dado. De lo contrario, vuelve a tirar ambos
# dados.
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


# Esta función se encarga de calcular y retornar el puntaje obtenido luego de
# que los dados son tirados.
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


# Esta función toma el puntaje de Juan y María respectivamente, y devuelve:
# Un 0 si Juan es el ganador, un 1 si María es la ganadora o un 2 si hay un
# empate.
def determinate_winner(juan_score, maria_score):
    if juan_score > maria_score:
        return 0
    elif juan_score < maria_score:
        return 1
    elif juan_score == maria_score:
        return 2


# Esta función simula el juego una cantidad especificada de veces por el
# parámetro "times", y calcula la frecuencia relativa de cada evento
# requerido por la letra de la tarea, y por último devuelve una tupla
# conteniendo los tres valores.
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

    return (juan_wins_relative_frequency,
            maria_wins_relative_frequency,
            draws_relative_frequency)


# La función main simplemente llama a "calculate_relative_frequencies" en tres
# ocasiones, en donde cada llamada toma por parámetro el número de veces que
# se quiera realizar la simulación, 1000, 10000 y 100000 veces, almacena los
# resultados en 3 variables respectivamente y luego los imprime.
def main():
    relative_frequencies_thousand = (
        calculate_relative_frequencies(int(1000)))

    relative_frequencies_ten_thousand = (
        calculate_relative_frequencies(int(10000)))

    relative_frequencies_hundred_thousand = (
        calculate_relative_frequencies(int(100000)))

    print(f"Frecuencia relativa para victorias de Juan (1000 juegos): "
          f"{relative_frequencies_thousand[0]}")
    print(f"Frecuencia relativa para victorias de María (1000 juegos): "
          f"{relative_frequencies_thousand[1]}")
    print(f"Frecuencia relativa para empates (1000 juegos): "
          f"{relative_frequencies_thousand[2]}")

    print("\n")

    print(f"Frecuencia relativa para victorias de Juan (10000 juegos): "
          f"{relative_frequencies_ten_thousand[0]}")
    print(f"Frecuencia relativa para victorias de María (10000 juegos): "
          f"{relative_frequencies_ten_thousand[1]}")
    print(f"Frecuencia relativa para empates (10000 juegos): "
          f"{relative_frequencies_ten_thousand[2]}")

    print("\n")

    print(f"Frecuencia relativa para victorias de Juan (100000 juegos): "
          f"{relative_frequencies_hundred_thousand[0]}")
    print(f"Frecuencia relativa para victorias de MaríDa (100000 juegos): "
          f"{relative_frequencies_hundred_thousand[1]}")
    print(f"Frecuencia relativa para empates (100000 juegos): "
          f"{relative_frequencies_hundred_thousand[2]}")


if __name__ == '__main__':
    main()
