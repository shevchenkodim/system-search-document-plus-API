from task_2.celery import app
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .models import Lost_documents
from django.db import IntegrityError
from .utils import timeit
import threading


@app.task
def load_data_structure_task():
    my_thread = threading.Thread(
        target=load_data_structure, name='load_data_structure', args=())
    my_thread.start()


@timeit
def load_data_structure():
    # Получаем html
    url = 'https://data.gov.ua/dataset/ab09ed00-4f51-4f6c-a2f7-1b2fb118be0f'
    html = requests.get(url)
    count = 0

    # Делаем поиск на файл структуры данных
    soup = BeautifulSoup(html.text)
    set_structure_link = soup.find_all(
        'td', {'class': 'dataset-details'})[-1].find('a').get('href')
    url_structures = 'https://data.gov.ua/' + set_structure_link

    # Получаем json структуры
    file_structures = requests.get(url_structures)
    json_structures = file_structures.json()

    resources_json = []
    for resource in json_structures.get('resources'):
        if 'Shema' in resource.get('name') or 'shema' in resource.get('name'):
            pass
        else:
            resources_json.append(resource.get('path'))

    for resource in resources_json:
        file_resorce = requests.get(resource)
        for data in file_resorce.json():
            try:
                Lost_documents.objects.create(identifier=data.get('ID'),
                                              document_series=data.get(
                                                  'D_SERIES'),
                                              document_number=data.get(
                                                  'D_NUMBER'),
                                              document_type_id=1,
                                              status=data.get('D_STATUS'),
                                              event_date=data.get(
                                                  'THEFT_DATA'),
                                              date_of_recording=data.get(
                                                  'INSERT_DATE'),
                                              registration_authority=data.get('OVD'))
            except IntegrityError as e:
                pass
