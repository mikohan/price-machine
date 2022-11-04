import shutil, os
from zipfile import ZipFile


def fix_truck_motors(file_path):
    """Fix brocken file truck motors"""
    # Создаем временную папку
    tmp_folder = "tmp_folder"
    # os.mkdir(tmp_folder)

    # Распаковываем excel как zip в нашу временную папку
    with ZipFile(file_path) as excel_container:
        excel_container.extractall(tmp_folder)

    try:
        # # Переименовываем файл с неверным названием
        wrong_file_path = os.path.join(tmp_folder, "xl", "SharedStrings.xml")
        correct_file_path = os.path.join(tmp_folder, "xl", "sharedStrings.xml")
        os.rename(wrong_file_path, correct_file_path)

        # # Запаковываем excel обратно в zip и переименовываем в исходный файл
        shutil.make_archive("yourfile", "zip", tmp_folder)
        os.rename("yourfile.zip", file_path)
    except Exception as e:
        print("Track motors error", e)

    shutil.rmtree(tmp_folder)
