import zipfile
path_to_zip_file = "../data/downloaded.csv.zip"
directory_to_extract_to = "../data"
zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()
