import json
import pandas as pd

"""
Чтение из файла json и вывод параметров необходимых в дальнейшем для обработки последних 5 операций
"""
def load_json_file(filename):
    operations_executed = []
    with open(filename, 'r', encoding='utf-8') as f:
        dict_operations = json.load(f)    # Читаем данные зи json

    df = pd.DataFrame(dict_operations)  # Модуль pandas создал data frame

    sort_df = df.sort_values('date', ascending=False).to_dict('records') # сортируем по дате в обратном порядке, чтобы более свежие операции были вверху

    for operation in sort_df:   #цикл обработки и сортировки
        operation.items()
        dict_filter = {}
        for k, v in operation.items():
            if k in ('state') and v == 'EXECUTED':   # берем только EXTENDED
                operations_executed.append(dict(
                    filter(lambda item: item[0] in ('date', 'description', 'from', 'to', 'operationAmount'),
                           operation.items())))   # берем только нужные нам поля и записываем в список

    return operations_executed[0:5]  # Отдает последние пять операций


"""
Конвертация полученных данных в нужный нам формат
перебираем все данные преобразуем их в нужный нам вид.
Выводим на экран
"""
def processing_for_output(dict_operations):
    for_test = []
    for operation in dict_operations:
        for k, v in operation.items():
            if k == 'date':
                date = v[0:10]
                date = str(date).split('-')
                date = list(reversed(date))
                date = '.'.join(date)
            if k == 'description':
                description = v
            if k == 'from':
                from_ = str(v)
                if from_ != None:
                    list_from = from_.split()
                    from_beginning = ' '.join(list_from[:-1])  # Карта или счет (написание)
                    from_end = list_from[-1]
                    if len(from_end) == 16:
                        firts_from_end = from_end[0:4]
                        second_from_end = from_end[4:6]
                        end_from_end = from_end[12:]
                        from_end = f"{from_beginning}  {firts_from_end} {second_from_end}** **** {end_from_end}"
                    if len(from_end) == 20:
                        end_from_end = from_end[16:]
                        from_end = f"{from_beginning}  ****{end_from_end}"
            if k == 'to':
                to_ = v
                if to_ != None:
                    list_to = to_.split()
                    to_beginning = ' '.join(list_to[:-1])  # Карта или счет (написание)
                    to_end = list_to[-1]
                    if len(to_end) == 16:
                        firts_to_end = to_end[0:4]
                        second_to_end = to_end[4:6]
                        end_to_end = to_end[12:]
                        to_end = f"{to_beginning}  {firts_to_end} {second_to_end}** **** {end_to_end}"
                    if len(to_end) == 20:
                        end_to_end = to_end[16:]
                        to_end = f"{to_beginning}  ****{end_to_end}"
            if k == 'operationAmount':
                sum_operation = v
                for k, v in sum_operation.items():
                    if k == 'amount':
                        sum_op = v
                    if k == 'currency':
                        currency = v
                        for k,v in currency.items():
                            if k == 'name':
                                currency = v
        print()
        print(f"{date} {description}")
        print(f"{from_end} -> {to_end}")
        print(f"{sum_op} {currency}")

        for_test.append(f"{date} {description} {from_end} {to_end} {sum_op} {currency}") # Записываем в список для использования в тестировании
    return for_test  # Вывод списка