import zipfile
import os

files_to_zip = [
    "/Users/stanislavdudnik/Desktop/Git/qa7/resources/sample1.pdf",
    "/Users/stanislavdudnik/Desktop/Git/qa_7/resources/sample2.xlsx",
    "/Users/stanislavdudnik/Desktop/Git/qa7/resources/sample3.csv",
]

archive_path = "/Users/stanislavdudnik/Desktop/Git/qa7/resources/archive.zip"

with zipfile.ZipFile(archive_path, 'w') as zipf:
    # Добавляем каждый файл в архив
    for file_path in files_to_zip:
        # arcname - имя файла внутри архива (может быть изменено)
        sample = os.path.basename(file_path)
        zipf.write(file_path, sample)

print(f"Архив создан по пути: {archive_path}")
