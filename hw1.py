# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# Входные данные:
# file_path = "C:/Users/User/Documents/example.txt"
#
# Выходные данные:
# ('C:/Users/User/Documents/', 'example', '.txt')
def get_two_str_by_split(text: str, sep: str, without_sep=False) -> tuple[str, str]:
    text_b = text.split(sep)[-1]
    text_a = text[:-len(text_b) - without_sep]
    return text_a, text_b


def get_file_info(file_path: str) -> tuple[str, str, str]:
    path, file_name_and_extension = get_two_str_by_split(file_path, '/')
    if '.' in file_name_and_extension:
        file_name, extension = get_two_str_by_split(file_name_and_extension, '.', True)
        extension = '.' + extension
    else:
        file_name = ''
        extension = '.' + file_name_and_extension
    return path, file_name, extension
    # file_name = file_path.split("/")[-1]
    # file_extension = file_name.split(".")[-1]
    # path = file_path[:-len(file_name)]
    # return path, file_name[:-len(file_extension) - 1], "." + file_extension


def main():
    file_path = "C:/Users/User/Documents/example.txt"
    print(get_file_info(file_path))


if __name__ == "__main__":
    main()
