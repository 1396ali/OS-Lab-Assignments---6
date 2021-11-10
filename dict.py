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
        with open ('words_bank.csv' , 'r') as f:
            text = f.read()
            words = text.split('\n')

            for i in range(0 , len(words) , 2):
                DICTIANORY.append({'EN' : words[i] , 'FA' : words[i+1]})
        print('loaded.')    
    except:
        print("NO file is here!")
        exit()


def translate_en_to_fa(input_text):
    user_words = input_text.split(' ')
    out_text = ""

    for user_word in user_words:
        for word in DICTIANORY:
            if user_word == word['EN']:
                out_text += word['FA'] + ' '
                break

        else:
            out_text += user_word + ' '
            
    return out_text

def translate_fa_to_en(input_text):
    user_words = input_text.split(' ')
    out_text = ""

    for user_word in user_words:
        for word in DICTIANORY:
            if user_word == word['FA']:
                out_text += word['EN'] + ' '
                break

        else:
            out_text += user_word + ' '
            
    return out_text


load()


print('\nwelcome')

while True:
    menu()
    print()
    op = int(input('Input : '))

    if op == 1:
        user_text = input('Enter: ')
        out_text = translate_en_to_fa(user_text)
        print('translated :' , out_text)
        

    elif op == 2:
        user_text = input('Enter: ')
        out_text = translate_fa_to_en(user_text)
        print('translated :' , out_text)
    
    elif op == 3:
        #add()
        pass
        
    elif op == 4:
        print('bye')
        exit()
