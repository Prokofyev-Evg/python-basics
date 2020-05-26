# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

trans_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("Примеры_файлов/text_4_tr.txt", 'w', encoding='utf-8') as w_file:
    with open("Примеры_файлов/text_4.txt", 'r', encoding='utf-8') as r_file:
        lines = r_file.readlines()
        for line in lines:
            words = line.split()
            for i, word in enumerate(words):
                if trans_dict.get(word):
                    words[i] = trans_dict[word]
            print(' '.join(words), file=w_file)

#####################################
#    С помощью google translate     #
#####################################

from googletrans import Translator

translator = Translator()

with open("Примеры_файлов/text_4_googletr.txt", 'w', encoding='utf-8') as w_file:
    with open("Примеры_файлов/text_4.txt", 'r', encoding='utf-8') as r_file:
        translations = translator.translate(r_file.readlines(), dest='ru')
        for translation in translations:
            print(translation.text, file=w_file)
