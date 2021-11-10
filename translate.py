WORDS = []


def load_data():
    print("Loading...")

    try:
        with open("words_bank.txt", 'r') as f:
            big_text = f.read()
            lines = big_text.split('\n')
            
            for i in range(0, len(lines), 2):
                WORDS.append({'English':lines[i], 'Persian':lines[i+1]})

        print("Loaded!")

    except FileNotFoundError:
        print("The file was NOT found!")
        exit()



def menu():
    print("\nWelcome to Mahtab Translate!")
    print("1. Translate English to Persian")
    print("2. Translate Persian to English")
    print("3. Add a new word")
    print("4. exit")

    

def get_input():
    user_text = input("\nPlease write your text: ").lower()
    return user_text



def translate_engToper(input_text):
    user_sentenses = input_text.split('.')
    output_text = ""

    for sentence in user_sentenses:
        user_words = sentence.split(' ')

        for user_word in user_words:
            for WORD in WORDS:
                if user_word == WORD['English']:
                    output_text += WORD['Persian'] + " "
                    break
            else:
                output_text += user_word + " "

        output_text += "."

    print("Output: " + output_text)



def translate_perToeng(input_text):
    user_sentenses = input_text.split('.')
    output_text = ""

    for sentence in user_sentenses:
        user_words = sentence.split(' ')

        for user_word in user_words:
            for WORD in WORDS:
                if user_word == WORD['Persian']:  
                    output_text += WORD['English'] + " "
                    break
            else:
                output_text += user_word + " "

        output_text += "."

    print("Output: " + output_text)



def add_new_word():
    temp_english = input("\nEnter the word in English: ")
    temp_persian = input("Enter the word in Persian: ")
    
    if not any(WORD['English'] == temp_english and WORD['Persian'] == temp_persian for WORD in WORDS):
        WORDS.append({'English':temp_english, 'Persian':temp_persian})
        print("\nThe word added successfully!\n")

        with open("words_bank.txt", 'a') as f:
            f.write("\n" + temp_english + "\n" + temp_persian)
         
    else:
        print("\nThis word is already available.\n")
        


load_data()

while True:
    menu()
    choice = int(input("Please enter your choice --> "))

    if choice == 1:
        translate_engToper(get_input())
    
    elif choice == 2:
        translate_perToeng(get_input())

    elif choice == 3:
        add_new_word()

    elif choice == 4:
        break
    
    else:
        print("\nTry again!\n")
