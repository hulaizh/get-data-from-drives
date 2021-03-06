import dropbox
import os
import zipfile


def main():
    # connect to dropbox with token
    token_file = 'token.txt'
    token = {}
    with open(token_file) as f:
        for line in f:
            (key, val) = line.split(':')
            token[key] = val
    dbx_token = token['dropbox'].strip()
    dbx = dropbox.Dropbox(dbx_token)

    # download dbx folder and files
    dbx_path = '/sharing'
    local_path = '/Users/hulai/Desktop'
    # all files to be downloaded
    file_names = ['Bryan  Everett.xlsx', 'Bryan  Everett.dta']

    # folder
    zip_name = dbx_path.split('/')[-1] + '.zip'
    zip_file = os.path.join(local_path, zip_name)
    print('Downloading to {}: '.format(local_path) + dbx_path)
    dbx.files_download_zip_to_file(zip_file, dbx_path)
    # unzip the zipped folder
    print('Unzipping: ' + zip_name)
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(local_path)
    os.remove(zip_file)

    # file
    for f in file_names:
        local_file = os.path.join(local_path, f)
        dbx_file = os.path.join(dbx_path, f)
        print('Downloading to {}: '.format(local_path) + f)
        dbx.files_download_to_file(local_file, dbx_file)


if __name__ == '__main__':
    main()
