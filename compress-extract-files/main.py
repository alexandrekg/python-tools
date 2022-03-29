import zipfile


def _extract_files(origin_file, final_file):
    with zipfile.ZipFile(f'./{origin_file}') as file_zip:
        file_zip.extract(final_file, './')

    print('[OK] File extracted')


def _compress_files(origin_file, final_file):
    with zipfile.ZipFile(f"./{final_file}", 'w') as file:
        file.write(f"./{origin_file}", compress_type=zipfile.ZIP_DEFLATED)

    print('[OK] File compressed')


if __name__ == "__main__":
    ORIGIN_FILE = 'file.zip'
    FINAL_FILE = 'file.json'

    _extract_files(ORIGIN_FILE, FINAL_FILE)
    # _compress_files(ORIGIN_FILE, FINAL_FILE)
