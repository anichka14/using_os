import os
import os.path as path
import sys
import humanize

"""Скласти програму порівняння файлів з однаковим ім’ям у двох
каталогах. Для таких пар файлів треба показати різницю у розмірі файлів.
Якщо файли мають однаковий розмір, то нічого показувати не потрібно.
Результат роботи програми слід спрямувати у текстовий файл."""


def compare_size(dir1, dir2):  # порівнюємо каталоги
    files_1 = set(os.listdir(dir1))  # отримуємо вміст заданого каталогу
    files_2 = set(os.listdir(dir2))

    for file in files_1 & files_2:
        file_path1 = path.join(dir1, file)  # повний шлях до файлу
        file_path2 = path.join(dir2, file)
        if path.isfile(file_path1) and path.isfile(file_path2):
            size_1 = os.path.getsize(file_path1)
            size_2 = os.path.getsize(file_path2)

            if size_1 < size_2:
                print(
                    f"Файл {file} з директорії {dir1} має "
                    f"менші розміри, ніж файл з директорії {dir2}."
                    f"\nРізниця у розмірі файлів {file}:",
                    humanize.naturalsize(size_1 - size_2)
                )
            elif size_1 > size_2:
                print(
                    f"Файл {file} з директорії {dir1} має "
                    f"більші розміри, ніж файл з директорії {dir2}."
                    f"\nРізниця у розмірі файлів {file}:",
                    humanize.naturalsize(size_1 - size_2)
                )


if __name__ == "__main__":
    old_out = sys.stdout  # стандартний вивід (вивід у консоль)
    new_out = open("output_22.3.txt", "w", encoding="utf-8")
    sys.stdout = new_out
    compare_size("dir1", "dir2")
    sys.stdout = old_out
    new_out.close()
    # size_1 = os.path.getsize(r"C:\Users\DELL E5490\PycharmProjects\ООП_Прикладне програмування\2 курс\5\dir1\output")
    # size_2 = os.path.getsize(r"C:\Users\DELL E5490\PycharmProjects\ООП_Прикладне програмування\2 курс\5\dir2\output")
    # print(size_1)
    # print(size_2)
