from os import system

from config import GAME_COMMANDS
from components import double_bar, game_title
from utils import draw_options

class Game():
    '''Create game file.'''
    def __init__(self) -> None:
        self.options = {
            1 : 'Iniciar Jogo',
            2 : 'Créditos',
            3 : 'Sair'
        }
        self.action = 0
        self.error = ''
    
    def draw_menu(self) -> None:
        '''Draw game menu.'''
        system('cls')
        screen = double_bar
        screen += game_title
        screen += '\n' + double_bar + '\n'
        screen += draw_options(self.options)
        screen += '\n' + double_bar + '\n'
        if self.error != '':
            screen += f'ERRO: {self.error}'
        print(screen)
    
    def player_action(self) -> None:
        '''Player action.'''
        self.action = input('DIGITE SUA RESPOSTA: ')
        if self.action.isdigit():
            self.action = int(self.action)
            if self.action in list(self.options) or self.action in list(GAME_COMMANDS):
                self.error = ''
            else:
                self.error = f'A opção "{self.action}" não existe, tente outra.'
        else:
            self.error = 'Você precisa digitar um número inteiro.'

    # RUN:
    def run(self) -> None:
        '''Run game.'''
        while self.action != 9:
            # MENU:
            while True:
                self.draw_menu()
                self.player_action()
                if self.error == '':
                    break
            
            # START GAME:
            if self.action == 1:
                while True:
                    if self.action == 9:
                        break
            
            # CREDITS:
            elif self.action == 2:
                pass

            # QUIT GAME:
            elif self.action == 3:
                self.action = 9

game = Game()
game.run()

# INTRO:

# CREDITS:
