import random

def generate_number(min_val=1, max_val=100):
    return random.randint(min_val, max_val)

def check_guess(secret, guess):
    if guess == secret:
        return "Угадал!"
    elif guess < secret:
        return "Меньше"
    else:
        return "Больше"

def play_game():
    print("Добро пожаловать в игру 'Угадай число'!")
    secret_number = generate_number(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Введите число от 1 до 100: "))
        except ValueError:
            print("Пожалуйста, введите целое число!")
            continue

        attempts += 1
        result = check_guess(secret_number, user_guess)
        
        if result == "Угадал!":
            print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток!")
            break
        else:
            print(f"Ваше число {result} загаданного. Попробуйте ещё раз!")

if __name__ == "__main__":
    play_game()