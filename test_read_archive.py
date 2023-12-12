import os
from zipfile import ZipFile
from pypdf import PdfReader
from openpyxl import load_workbook
import csv
from webdriver_manager.core import archive


def test_pdf_file(create_directory, archive):
    with ZipFile('resources/test_archive.zip') as archive:
        file = archive.read('example.pdf')
        file_stats = os.stat(file)
        print(file_stats)
        print(f'File size in bytes is {file_stats.st_size}.')
        reader = PdfReader('tmp/example.pdf')
        assert file_stats.st_size == archive.getinfo('example.pdf').file_size == 38329
        assert len(reader.pages) == 0
        assert "Пример PDF файла" in reader.pages[0]

def test_xlsx_file(create_directory, archive):
    with ZipFile('resources/test_archive.zip') as archive:
        file = archive.read('import_company.xlsx')
        workbook = load_workbook(file)
        sheet = workbook.active
        assert archive.getinfo('import_company.xlsx').file_size == 6809
        assert len(workbook.sheetnames) == 1
        assert sheet.max_row == 10
        assert sheet.max_column == 5
        assert sheet.cell(row=4, column=3).value == 'Отдел сервисного обслуживания'

def test_csv_file():
    with ZipFile('resourses/test_archive.zip') as zip_file:
        file = archive.read('gross-domestic-product-june-2023-quarter.csv')
        reader = csv.DictReader(file)
        print('Имена полей: ', reader.fieldnames)
        assert archive.getinfo('gross-domestic-product-june-2023-quarter.csv').file_size == 19034868




