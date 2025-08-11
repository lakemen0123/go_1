import random

def rock_paper_scissors():
    choices = ["камень", "ножницы", "бумага"]
    user = input("Выберите: камень, ножницы, бумага: ").lower()
    if user not in choices:
        return "Неверный выбор!"
    computer = random.choice(choices)
    print(f"Компьютер выбрал: {computer}")
    if user == computer:
        return "Ничья!"
    elif (user == "камень" and computer == "ножницы") or \
         (user == "ножницы" and computer == "бумага") or \
         (user == "бумага" and computer == "камень"):
        return "Вы выиграли!"
    return "Компьютер выиграл!"

print(rock_paper_scissors())