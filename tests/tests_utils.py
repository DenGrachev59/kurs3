import pytest
from scr import utils

test_file = 'test_file.json'

rezult_load_json_file = [{'date': '2020-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'}, {'date': '2020-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}, {'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}, {'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}]
output_rezult1 =[{'date': '2019-08-26T10:50:58.294041',
           'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
           'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},]

output_rezult2 =[{'date': '2019-07-12T20:41:47.882230',
           'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},
           'description': 'Перевод организации', 'from': 'Счет 48894435694657014368', 'to': 'Счет 38976430693692818358'},]


output_rezult3 =[{'date': '2019-07-12T20:41:47.882230',
           'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},
           'description': 'Перевод организации', 'from': 'Счет 48894435694657014368', 'to': 'Maestro 1596837868705199'},]



# o_result = """26.08.2019 Перевод организации
# Maestro  1596 83** **** 5199 -> Счет  ****9589
# 31957.58 руб."""

o_result1 = ['26.08.2019 Перевод организации Maestro  1596 83** **** 5199 Счет  ****9589 31957.58 руб.']
o_result2 = ['12.07.2019 Перевод организации Счет  ****4368 Счет  ****8358 56883.54 USD']
o_result3 = ['12.07.2019 Перевод организации Счет  ****4368 Maestro  1596 83** **** 5199 56883.54 USD']

def test_load_json_file():
    assert utils.load_json_file(test_file)== rezult_load_json_file


def test_procesing_for_output():
    # rez_dict = []
    # rez = processing_for_output(output_rezult)
    # rez_dict.append(rez)

    assert utils.processing_for_output(output_rezult1) == o_result1
    assert utils.processing_for_output(output_rezult2) == o_result2
    assert utils.processing_for_output(output_rezult3) == o_result3

