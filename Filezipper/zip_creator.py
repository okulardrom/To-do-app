import zipfile
import pathlib




def make_archive(filepaths, dest_dir):

    with zipfile.ZipFile(pathlib.Path(dest_dir, "compressed.zip"), 'w') as archive:

        for filepath in filepaths:
            filepath = pathlib.Path(filepath)


            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    make_archive(['C:/Users/okula/PycharmProjects/pythonProject/Filezipper/anyfile.py'], "dest")