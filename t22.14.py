import os
import os.path as path
import pandas as pd

"""Скласти програму, яка обчислює статистику по файлах з різними
розширеннями у заданому каталозі. Для кожного розширення програма
повинна показати кількість та загальний розмір у байтах файлів з цим
розширенням. Також здійснити перенаправлення результатів роботи програми
у текстовий файл."""


def set_statistic(df, files, dir, ext):
    count = 0
    size = 0

    for file in files:
        file_path = path.join(dir, file)  # повний шлях до файлу
        # file.endswith(ext) - для розширення
        if path.isfile(file_path) and file.endswith(ext):
            count += 1
            size += os.path.getsize(file_path)
            # використовуємо метод пайтон at для оновлення статистики
            # dataframe.at[index,'column-name']='new value'
            df.at[ext, "Count"] = count
            df.at[ext, "Size"] = size


def file_statistics(dir):
    files = set(os.listdir(dir))
    file_extensions = set(file.split(".")[-1] for file in files)
    # створюємо dataframe
    df = pd.DataFrame([], columns=["Count", "Size"], index=list(file_extensions))

    for ext in file_extensions:
        set_statistic(df=df, files=files, dir=dir, ext=ext)
    # збереження таблиці у csv форматі за допомогою методу to_csv()
    df.to_csv("statistic.csv")


if __name__ == "__main__":
    file_statistics("dir3")
