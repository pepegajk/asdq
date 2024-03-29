import json
import csv

class Game:
    def __init__(self):
        self.data = {}

    def save_game(self, username, score):
        self.data[username] = score
        with open('data.json', 'w') as file:
            json.dump(self.data, file)

    def delete_save(self, username):
        if username in self.data:
            del self.data[username]
            with open('data.json', 'w') as file:
                json.dump(self.data, file)

    def export_to_csv(self):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Username", "Score"])
            for username, score in self.data.items():
                writer.writerow([username, score])

game = Game()
game.save_game('user1', 100)
game.save_game('user2', 150)
game.export_to_csv()
game.delete_save('user1')
game.export_to_csv()
def introduction():
    print("Добро пожаловать в текстовую игровую новеллу!")
    print("В этой игре вы будете принимать решения, которые определяют исход истории.")
    print("Давайте начнем!")

def make_choice(options):
    print("Выберите вариант:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    choice = input("Введите номер вашего выбора: ")
    return int(choice) - 1

def play_game():
    player_name = input("Введите ваше имя: ")
    print(f"Привет, {player_name}!")
    print("Однажды, в далекой стране...")
    print("Вы оказываетесь в загадочном лесу.")
    print("Что вы делаете?")
    
    choices = ["Исследовать лес", "Вернуться домой"]
    choice = make_choice(choices)
    
    if choice == 0:
        explore_forest()
    else:
        go_back_home()

def explore_forest():
    print("Вы решаете исследовать лес.")
    print("Продвигаясь глубже в лес, вы натыкаетесь на развилку.")
    
    choices = ["Пойти по левому пути", "Пойти по правому пути"]
    choice = make_choice(choices)
    
    if choice == 0:
        take_left_path()
    else:
        take_right_path()

def take_left_path():
    print("Вы выбираете левый путь и продолжаете свое путешествие.")
    print("Внезапно, вы слышите странный шум позади себя.")
    
    choices = ["Повернуться и исследовать", "Игнорировать шум и продолжать идти"]
    choice = make_choice(choices)
    
    if choice == 0:
        investigate_noise()
    else:
        keep_walking()

def take_right_path():
    print("Вы выбираете правый путь и продолжаете свое путешествие.")
    print("Пройдя некоторое время, вы натыкаетесь на скрытый сундук с сокровищами.")
    print("Что вы делаете?")
    
    choices = ["Открыть сундук", "Оставить сундук в покое"]
    choice = make_choice(choices)
    
    if choice == 0:
        open_treasure_chest()
    else:
        leave_treasure_chest()

def go_back_home():
    print("Вы решаете вернуться домой.")
    print("Прогуливаясь обратно, вы чувствуете облегчение.")
    print("Поздравляю! Вы завершили игру.")

def investigate_noise():
    print("Вы поворачиваетесь, чтобы исследовать шум.")
    print("К вашему удивлению, вы видите милого кролика.")
    print("Кажется, это была ложная тревога.")
    print("Что вы делаете?")
    
    choices = ["Погладить кролика", "Продолжить исследование леса"]
    choice = make_choice(choices)
    
    if choice == 0:
        pet_bunny_rabbit()
    else:
        continue_exploring()

def keep_walking():
    print("Вы решаете проигнорировать шум и продолжать идти.")
    print("Продвигаясь дальше, вы натыкаетесь на прекрасный водопад.")
    print("Вы садитесь у водопада и наслаждаетесь спокойной обстановкой.")
    print("Поздравляю! Вы завершили игру.")

def open_treasure_chest():
    print("Вы открываете сундук и находите внутри блестящий алмаз.")
    print("Вы чувствуете себя счастливым, что нашли такое ценное сокровище.")
    print("Поздравляю! Вы завершили игру.")

def leave_treasure_chest():
    print("Вы решаете оставить сундук в покое и продолжить свое путешествие.")
    print("Продвигаясь дальше, вы натыкаетесь на группу дружелюбных лесных существ.")
    print("Они приглашают вас присоединиться к их празднику.")
    print("Поздравляю! Вы завершили игру.")

def pet_bunny_rabbit():
    print("Вы приседаете и гладите кролика.")
    print("Он радостно убегает, и вы продолжаете свое исследование.")
    print("Вдруг вы замечаете странную фигуру вдалеке.")
    print("Что вы делаете?")
    
    choices = ["Подойти ближе и рассмотреть", "Продолжить исследование леса"]
    choice = make_choice(choices)
    
    if choice == 0:
        approach_figure()
    else:
        continue_exploring()

def approach_figure():
    print("Вы подходите ближе к фигуре и видите, что это старый мудрец.")
    print("Он предлагает вам магический артефакт, который может исполнить одно желание.")
    print("Что вы желаете?")
    
    choices = ["Богатство", "Любовь", "Мудрость"]
    choice = make_choice(choices)
    
    if choice == 0:
        print("Вы желаете богатства и получаете мешок золота.")
    elif choice == 1:
        print("Вы желаете любви и встречаете свою идеальную половинку.")
    else:
        print("Вы желаете мудрости и получаете знания, которые помогут вам преуспеть в жизни.")
    
    print("Поздравляю! Вы завершили игру.")

def continue_exploring():
    print("Вы решаете продолжить исследование леса.")
    print("Продвигаясь дальше, вы открываете скрытый водопад.")
    print("Вы садитесь у водопада и наслаждаетесь спокойной обстановкой.")
    print("Поздравляю! Вы завершили игру.")

def main():
    introduction()
    play_game()

if __name__ == "__main__":
    main()