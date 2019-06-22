'''
Note.io App
'''
import os
#import getch
from textandfile_handler import text_to_file, file_to_text

PATH = '~/Notes'
def main():
    print_menu('main')
    while True: 
        '''
        Handle the main logic of the app
        '''
        choice = input().lower()
        if choice == ''
            print_menu('new')
            create_note()
        elif choice == 'v':
            print_menu('view')
            view_notes()
        elif choice == 'i':
            print_menu('import')
            import_note()
        elif choice == 'e':
            return
        else:
            print_menu('hint')
            return

def create_note():
    '''
    Collects a new note from user input and saves using the 'save_note()' function
    '''
    new_note = input()
    confirm_save = input("That note was most certainly interesting and/or useful!\n Do you want to keep it? y/n\n>>>')")
    if confirm_save == y:
        note_name = input('What is the name of this note? ')
        save_note(note_name, new_note)
    elif confirm_save == n:
        return


def save_note(note_name, note_contents):
    print('You wrote:')
    print(file_to_text('unnamed.txt'))
    
    text_to_file(input(), 'notes.json')


def add_line():
    print_menu('line')
    with open('notes/unnamed.txt', 'a') as appending_line:
        appending_line.write(input())

def manage_notes():
    pass

def append_line():
    pass

def get_decision(decision):
    choice = input()
    if decision == 'new line' and choice == 'regex': ## use regex to verify input
        return choice

# View your past notes
def view_notes():
    file_path = 'notes/'
    file_list = os.listdir(file_path)
    print(f'You have {str(len(file_list))}')
    for i in range(len(file_list)):
        print(f'{str(i + 1)}: {file_list[i]} ({os.path.getsize(file_list[i])} byte)')

def import_note():
    pass

def print_menu(menu):
    menus_dictionary = {
        'main': 'Welcome to "note.io"\n*******************\nNEW NOTE? Hit ENTER!\n*******************\n[v]: View notes\n[i]: Import a note\n[e]: Exit note.io\n*******************',
        'new': f"Get that idea down!\n{' NEW NOTE '.center(30, '-')}",
        'view': ' VIEW NOTES '.center(30, '-'),
        'import': ' IMPORT '.center(30, '-'),
        'hint': "Hint: ENTER => NEW NOTE, 'v' to view your notes, 'i' to import a note, 'e' to exit",
        'line': 'Would you like to add a new line?\nHit ENTER or [e] to save and exit to main menu\n'}
    print(menus_dictionary[menu])

main()