from scr.utils import load_json_file, processing_for_output

data = load_json_file('/home/den/project/kurs3/operations.json') # Вызываем функцию чтения файла и выдачи нужных полей в последних пяти операций
rezult = processing_for_output(data) # Вызываем функцию преобразования данных в нужный нам вид

