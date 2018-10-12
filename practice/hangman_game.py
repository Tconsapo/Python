'''
Игра "виселица"
'''
import random


class word(object):
    '''
    задает слово из набора
    '''
    def __init__(self):
        self.words =list('acres:adult:advice:arrangement:attempt:august:autumn:border:breeze:brick:calm:canal:casey:cast:chose:claws:coach:constantly:contrast:cookies:customs:damage:danny:deeply:depth:discussion:doll:donkey:egypt:ellen:essential:exchange:exist:explanation:facing:film:finest:fireplace:floating:folks:fort:garage:grabbed:grandmother:habit:happily:harry:heading:hunter:illinois:image:independent:instant:january:kids:label:Lee:lungs:manufacturing:martin:mathematics:melted:memory:mill:mission:monkey:mount:mysterious:neighborhood:norway:nuts:occasionally:official:ourselves:palace:pennsylvania:philadelphia:plates:poetry:policeman:positive:possibly:practical:pride:promised:recall:relationship:remarkable:require:rhyme:rocky:rubbed:rush:sale:satellites:satisfied:scared:selection:shake:shaking:shallow:shout:silly:simplest:slight:slip:slope:soap:solar:species:spin:stiff:swung:tales:thumb:tobacco:toy:trap:treated:tune:University:vapor:vessels:wealth:wolf:zoo'.split(':'))
        self.current_word = self.set_word()


    def set_word(self, index = -1):
        '''
        задает случайное слово из набора или по индексу
        :param index: индекс в списке
        :return: str слово или None, если указан неверный индекс
        '''
        if index == -1:
            return random.choice(self.words)
        if index < len(self.words):
            return self.words[index]
        else:
            return None


    def get_word(self):
        '''
        возвращает слово
        :return: str слово
        '''
        return self.current_word


class game(object):
    '''
    основной класс игры
    '''
    def __init__(self):
        self.word = word().get_word()
        self.lives_left = 10
        self.letters = list(self.word)
        self.user_letters = list('_' for i in self.letters)


    def set_lives_count(self, lives):
        """
        Устанавливает количество жизней
        :return: int количество жизней
        """
        self.lives_left = lives
        return self.lives_left


    def set_word(self, word):
        """
        устанавливает слово
        :return: str установленное слово
        """
        self.word = word
        self.letters = list(self.word)
        self.user_letters = list('_' for i in self.letters)
        return self.word


    def change_settings(self):
        """
        позволяет установить пользовательские настройки игры
        """
        while True:
            arg = input('Do you want to change settings [y/n]: ')
            if arg == 'y':
                lives = input('Enter lives count: ')
                if lives != '':
                    self.set_lives_count(int(lives))
                word = input('Enter the word: ')
                if word != '':
                    self.set_word(word)
                break
            elif arg == 'n':
                break


    def user_input(self):
        """
        обработка ввода
        :return: str символ в нижнем регистре
        """
        letter = ''
        while True:
            letter = input('Enter the letter: ')
            if len(letter) == 1:
                break
        return letter.lower()


    def print_game_status(self):
        """
        вывод текущего состояния игры
        """
        print('-'*80)
        print('your word is: ', self.user_letters)
        print('lives left: ', self.lives_left)
        print('-'*80)


    def game_status(self):
        """
        проверка состояния игры (закончена или нет)
        :return: bool продолжается ли игра
        """
        if self.lives_left <= 0:
            return False
        return not self.is_word_found()


    def is_word_found(self):
        """
        Проверка соответствия слова игрока и загаданного
        :return: True если слово угадано; False - если нет
        """
        for i in range(0,len(self.word)):
            if self.letters[i] != self.user_letters[i]:
                return False
        return True


    def letter_check(self, letter):
        """
        Проверка введенной буквы
        Если введенная буква есть в загаданном слове - обновляет
        пользовательское слово
        Иначе уменьшает количество жизней
        """
        if not self.word.find(letter) == -1:
            for i in range(0,len(self.word)):
                if self.letters[i] == letter:
                    self.user_letters[i] = self.letters[i]
        else:
            self.lives_left -= 1


    def print_game_result(self):
        """
        вывод результата игры
        """
        if self.lives_left <= 0:
            print('-'*80)
            print('You lose!')
            print('-'*80)
        else:
            print('-'*80)
            print('You win!')
            print('-'*80)


    def process(self):
        """
        Процесс игры
        """
        while self.game_status():
            self.letter_check(self.user_input())
            self.print_game_status()
        self.print_game_result()


    def start_game(self):
        """
        Запуск игры
        """
        self.change_settings()
        print('-'*80)
        self.process()


def main():
    game().start_game()

if __name__ == '__main__':
    main()
