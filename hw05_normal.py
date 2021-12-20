import random
import re
# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

regex_upprcase = re.compile(r'[^A-Z]+')
matched_text = regex_upprcase.findall(line)
print(matched_text)

def find_uppercase(input_sting):
       list = []
       counter = ''
       for i in range(len(input_sting)):
              if not input_sting[i].isupper():
                     counter += input_sting[i]
                     if i == len(input_sting)-1:
                            list.append (counter)
              else:
                     if not counter:
                            pass
                     else:
                            list.append(counter)
                            counter = ''
       return list
print(find_uppercase(line))

print(find_uppercase("mtMmEZUOmcq"))
print(regex_upprcase.findall("mtMmEZUOmcq"))

print(len(regex_upprcase.findall("mtMmEZUOmcq")))
print(len(find_uppercase("mtMmEZUOmcq")))


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

regex_upper_task_2 = re.compile(r'([a-z]{2})([A-Z]+)([A-Z]{2})')
founded_groups = regex_upper_task_2.findall(line_2)
result_list = [x[1] for x in founded_groups]
print(result_list)
print(len(result_list))

def find_uppercase_advanced(input_sting):
    list = []
    counter_is_lower = 0
    # counter_is_upper = 0
    upper_to_print = ''
    for i in input_sting:
        # print(i)
        if counter_is_lower >= 2:
            if i.isupper():
                # print(i)
                upper_to_print+=i
            else:
                if len(upper_to_print) > 2:
                    list.append(upper_to_print[:-2])
                    # print(upper_to_print)
                    upper_to_print = ''
                    # counter_is_upper = 0
                    counter_is_lower = 1
                else:
                    if len(upper_to_print):
                        upper_to_print = ''
                        counter_is_lower = 1
                    else:
                        pass
        elif i.islower():
            # print(i)
            counter_is_lower += 1
        else:
            counter_is_lower = 0
    return list
print(find_uppercase_advanced(line_2))
print(len((find_uppercase_advanced(line_2))))
print(find_uppercase_advanced("GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"))
founded_groups_test = regex_upper_task_2.findall("GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec")
result_list_test = [x[1] for x in founded_groups_test]
print(result_list_test)
# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
str_random_list = ''.join([str(x) for x in random_list])
print(str_random_list)
print(len(str_random_list))
with open('random_string.txt', 'w') as r:
    r.write(str_random_list)
counter = ''
sorted_and_grouped = []
for i in range(len(str_random_list)-1):
       if str_random_list[i] == str_random_list[i + 1]:
              counter += str(str_random_list[i])
       else:
              counter += str(str_random_list[i])
              sorted_and_grouped.append(counter)
              counter = ''
list_lengthes = (list(map(len, sorted_and_grouped)))
print(f'len of list_lenthes= {len(list_lengthes)} == len of sorted_and_grouped= {len(sorted_and_grouped)}')
max_number_of_repeats = max(list_lengthes)
print(f'max number repeats= {max_number_of_repeats}')
index_of_max_repeats = list_lengthes.index(max_number_of_repeats)
biggest_number = sorted_and_grouped[index_of_max_repeats]
print(f'The biggest number= {biggest_number}')
