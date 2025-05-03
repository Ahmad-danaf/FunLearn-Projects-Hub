import pandas
df = pandas.read_csv('nato_phonetic_alphabet.csv')

alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}

user_input = input("Enter your words: ").upper()
res = [alphabet_dict[letter] for letter in user_input if letter in alphabet_dict.keys()]

print(res)
