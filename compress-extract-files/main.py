import zipfile

# with zipfile.ZipFile('./file.zip', 'w') as file_zip:
#     file_zip.write('./file.json', compress_type=zipfile.ZIP_DEFLATED)

with zipfile.ZipFile('./file.zip') as file_zip:
    file_zip.extract('file.json', './')