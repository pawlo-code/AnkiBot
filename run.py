from anki.anki_main import AnkiBot

with AnkiBot() as bot:
    print("Program - AnkiBot")
    print("Co chciałbyś teraz zrobić? Do wyboru:")
    print("1 - Zapisać słówka z ank do pliku - file.csv")
    print("2 - Dodać słówka do bazy danych anki z pliku - learned_words.csv")
    print("3 - Włączyć program do nasłuchiwania i dodawanie słów do pliku na bieżąco za pomocą skopiowania słowa")
    answer = input("Podaj numer: ")
    match answer:
        case '1':
            bot.words_from_anki()
        case '2':
            bot.add_words_to_anki()
        case '3':
            print("Niedługo")
        case _:
            print("Nieprawidłowy wybór!")