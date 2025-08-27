import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# data_dict = data.to_dict()
new_data = {row.letter:row.code for (index,row) in data.iterrows()}
# print(data_dict)
print(new_data)

name = input("Enter a name: ").upper()
output = [new_data[letter] for letter in name]
print(output)