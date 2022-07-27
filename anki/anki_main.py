from calendar import c
from selenium import webdriver
from anki.anki_data_sender import DataSender
import anki.constants as const
import os
import time

class AnkiBot(webdriver.Chrome):

    def __init__(self, driver_path=r'C:\Selenium'):
        self.driver_path = driver_path
        os.environ['PATH'] += driver_path
        super(AnkiBot, self).__init__()
        self.implicitly_wait(5)
        self.maximize_window()
        self.cookies_login()

    def cookies_login(self):
        self.get(const.BASE_URL)
        self.add_cookie(const.COOKIES)
        self.refresh()

    def words_from_anki(self):
        button = self.find_element_by_link_text('Search')
        button.click()

        second_button = self.find_element_by_name('submit')
        second_button.click()

        words = self.find_elements_by_tag_name('td')
        
        strings_from_anki = []

        for word in words:
            if "Edit" not in word.get_attribute('innerHTML'):
                strings_from_anki.append(word.get_attribute('innerHTML'))

        
        DataSender(strings_from_anki, '/', 'list_to_file')

    def add_words_to_anki(self):
        button = self.find_element_by_link_text('Add')
        button.click()

        models = self.find_element_by_id('models')
        models.click()

        models.find_element_by_xpath('//*[text()="Basic (and reversed card)"]').click()

        deck = self.find_element_by_id('deck')
        deck.click()
                
        deck.find_element_by_xpath('//*[text()="IT"]').click()

        ds = DataSender('text_files/learned_words.csv', '-', 'file_to_list')

        print('Dodawanie słów do bazy słówek anki...')
        print('Ilość słów:', len(ds.list_of_file_lw))

        
        for element in ds.list_of_file_lw:
            
            time.sleep(0.3)

            while True:

                first_word = self.find_element_by_id('f0')

                if first_word.get_attribute("innerText") == "":

                    first_word.send_keys(element['Word1'].strip())

                    second_word = self.find_element_by_id('f1')
                    second_word.send_keys(element['Word2'].strip())

                    try:
                        btn = self.find_element_by_css_selector('button[class="btn btn-primary"]')
                        btn.click()
                    except:
                        print('ERROR: Nie udało się dodać słowa - ', element )

                    break

        print('Dodawanie zakończone!')

