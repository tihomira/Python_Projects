import pandas

data = pandas.read_csv("~/PycharmProjects/Python_Projects/Nato_Alphabet_Project/nato_phonetic_alphabet.csv")
data = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    user_input = input("Type a word: ").upper()
    try:
        output_list = [data[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet, please!")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
