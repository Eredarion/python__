long_string = 'Дорогие друзья, постоянное информационно-техническое обеспечение нашей деятельности позволяет оценить значение дальнейших направлений развитая системы массового участия? Повседневная практика показывает, что реализация намеченного плана развития позволяет оценить значение системы масштабного изменения ряда параметров? Задача организации, в особенности же сложившаяся структура организации играет важную роль в формировании дальнейших направлений развитая системы массового участия. Таким образом, постоянное информационно-техническое обеспечение нашей деятельности играет важную роль в формировании существующих финансовых и административных условий.'

def find_char_count(text):
      char_summ = 0
      for c in text:
            if c == "и":
                  char_summ += 1
      print(char_summ)

""" Write file """
with open("1_file_1.txt", "w") as file:
      file.write(long_string)

""" Read file """
with open("1_file_1.txt", "r") as file:
      file_text = file.read()

""" 'и' count """
find_char_count(file_text)
