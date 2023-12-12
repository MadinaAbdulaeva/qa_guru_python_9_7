import os.path
import shutil
import pytest
@pytest.fixture    #создание папок resources и tmp
def create_directory():
    if not os.path.exists('resources'):
        os.mkdir('resources')
    if not os.path.exists('tmp'):
        os.mkdir('tmp')

@pytest.fixture  #cоздание архива в формате zip в папке resources
def archive():
    if not os.path.exists('resources/test_archive.zip'):
        shutil.make_archive('test_archive', 'zip', 'tmp')
        shutil.move('test_archive.zip', 'resources/test_archive.zip')