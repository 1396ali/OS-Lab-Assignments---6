#1

DICTIANORY = []

def menu():
    print()
    print('1. EN -> FA')
    print('2. FA -> EN')
    print('3. ADD')
    print('4. EXIT')

def load():
    print('Load...')

    try:
        with open ('words_bank.csv' , 'r') as file:
            file_text = file.read()
            words = file_text.split('\n')

            for i in range(0 , len(words) , 2):
                DICTIANORY.append({'ENG' : words[i] , 'FAR' : words[i+1]})
        print('loaded.')    
    except FileNotFoundError:
        print("NO file is here!")
        exit()


def translate_en_to_fa():
    inputed_text = input('Enter: ')
    user_sentence = inputed_text.split('.')
    outed_text = ""

    for user_sen in user_sentence:
        user_words = user_sen.split(' ')
        for user_word in user_words:
            for words in DICTIANORY:
                if user_word == words['ENG']:
                    outed_text += words['FAR'] + ' '
                    break

            else:
                outed_text += user_word + ' '
            
    return outed_text


def translate_fa_to_en():
    inputed_text = input('Enter: ')
    user_sentence = inputed_text.split('.')
    outed_text = ""

    for user_sen in user_sentence:
        user_words = user_sen.split(' ')
        for user_word in user_words:
            for words in DICTIANORY:
                if user_word == words['FAR']:
                    outed_text += words['ENG'] + ' '
                    break

            else:
                outed_text += user_word + ' '
            
    return outed_text


def add():
    print('add...')

    new_w = {'ENG': input('Enter EN: ')}
    new_w['FAR'] = input('Enter FA: ')

    DICTIANORY.append(new_w)

    file = open('words_bank.csv' , 'a')
    file.write('\n' + new_w['ENG'] + '\n' + new_w['FAR'])
    file.close
    
    print('added.')


load()


print('\nwelcome')

while True:
    menu()
    print()
    op = int(input('Input : '))

    if op == 1:        
        print('translated :' , translate_en_to_fa())

    elif op == 2:
        print('translated :' , translate_fa_to_en())
    
    elif op == 3:
        add()
        
    elif op == 4:
        print('bye')
        exit()
