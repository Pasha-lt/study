import os
import subprocess
import requests
import zipfile
import xml.etree.ElementTree as Tree


def get_download_link() -> str:
    url = 'https://repo.maven.apache.org/maven2/' \
          'io/qameta/allure/allure-commandline/'
    versions_list_url = url + 'maven-metadata.xml'
    response = requests.get(versions_list_url)
    root = Tree.fromstring(response.content)
    actual_version = root.find('.//versions').findall('version')[
        -1].text.strip()

    file_name = 'allure-commandline-' + actual_version + '.zip'
    link = url + actual_version + '/' + file_name
    return link


def get_filename() -> str:
    return get_download_link().split('/')[-1]


def get_latest_version() -> str:
    return get_filename().split('-')[-1].split('.zip')[0]


def get_installed_version() -> str:
    installed_version = None
    try:
        installed_version = subprocess.check_output(
            'allure --version', shell=True, text=True).strip()
    except subprocess.CalledProcessError:
        pass

    return installed_version


def print_versions_info():
    if not get_installed_version():
        print('Allure is not installed...')
    else:
        if get_latest_version() == get_installed_version():
            print('Latest version of Allure is installed')
        else:
            print('Allure is not latest version, updating...')


def is_file_already_downloaded(file_name: str, info: bool = True) -> bool:
    state = os.path.exists(file_name)
    if info:
        if state:
            print(f'File {file_name} already exists.')
        else:
            print(f'File {file_name} not exists.')
    return state


def get_unzipped_folder_name(zip_file_name: str) -> str:
    with zipfile.ZipFile(f'./{zip_file_name}', 'r') as zip_ref:
        file_names = zip_ref.namelist()
        folder_name = file_names[0]
    return folder_name


def is_folder_exists(folder_name: str, info: bool = True) -> bool:
    state = os.path.exists(folder_name)
    if info:
        if state:
            print(f"folder {folder_name} exists")
        else:
            print(f"folder {folder_name} doesn't exists")
    return state


def install(zip_file_name: str):
    binary = '/bin/allure'
    target = '/usr/share/'
    os.system(f'unzip {zip_file_name}')
    folder_name = get_unzipped_folder_name(zip_file_name)
    path = f'{target}{folder_name}'

    if not is_folder_exists(path, info=True):
        os.system(f'mv {folder_name} {target}{folder_name}')
        os.system(
            f'ln -s {target}{folder_name}{binary} /usr/local{binary}')


def uninstall():
    zip_file_name = get_filename()
    folder_name = get_unzipped_folder_name(zip_file_name)
    os.system(f'rm -rf /usr/local/bin/allure')
    os.system(f'rm -rf /usr/share{folder_name}')


if __name__ == '__main__':
    if not get_installed_version():
        if not is_file_already_downloaded(get_filename()):
            os.system(f'wget {get_download_link()}')
        install(zip_file_name=get_filename())