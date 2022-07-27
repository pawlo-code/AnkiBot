import csv

class DataSender():

    list_of_file_lw= []
    check_list = []

    def __init__(self, data=None, char=None, do=None):
        self.data = data
        self.char = char
        self.do = do
        self.add_to_checklist()
        match do:
            case 'file_to_list': self.file_to_list(data)
            case 'list_to_file': self.convert_data(data, char)

    def add_to_checklist(self):
        with open('text_files/file.csv', 'r',encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='-', fieldnames=['Word1', 'Word2'])
            for row in reader:
                print(row)
                self.check_list.append(row)
            print("----------------------------------------------------------------")

    def convert_data(self, data, char):
        splited_words = []
        dict_words_list = []

        for not_splited_word in data:
            splited = not_splited_word.split(char)
            splited_words.append(splited)

        for splited_word in splited_words:
            try:
                dict_words_list.append({"Word1":splited_word[0], "Word2":splited_word[1]})
            except:
                pass
        
        self.save_in_file(dict_words_list, 'text_files/file.csv')

    def file_to_list(self, file_name):
        with open(file_name, 'r' ,encoding='utf-8', newline="") as f:
            dreader = csv.DictReader(f, delimiter='-', fieldnames=['Word1', 'Word2'])

            for row in dreader:
                print(row)
                if row not in self.check_list:
                    self.list_of_file_lw.append(row)

    def save_in_file(self, dict_list, file_name):
        with open(file_name, 'a+', newline="", encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter='-', fieldnames=['Word1', 'Word2'])

            words_counter = 0

            for row in dict_list:
                if row not in self.check_list:
                    writer.writerow(row)
                    words_counter += 1

            if words_counter == 0:
                print('Żadne nowe słowa w pliku, nie dodano słów!')
            else:
                print(f'Dodano {words_counter} słów!')
                    
                