import pandas

data = pandas.read_csv("~/PycharmProjects/Python_Projects/Nato_Alphabet_Project/nato_phonetic_alphabet.csv")
data = {row.letter:row.code for (index, row) in data.iterrows()}

user_input = input("Type a word: ").upper()

output_list = [data[letter] for letter in user_input]
print(output_list)
