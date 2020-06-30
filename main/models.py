from django.db import models


class Document_type(models.Model):
    name = models.CharField(
        max_length=256, verbose_name='Наименование', blank=True)
    has_an_expiration_date = models.BooleanField(
        default=False, verbose_name='Имеет срок действия')
    has_a_series = models.BooleanField(
        default=False, verbose_name='Имеет серию')

    def __str__(self):
        return self.name


class Lost_documents(models.Model):
    identifier = models.CharField(
        max_length=256, verbose_name='Идентификатор', blank=False, unique=True)
    document_series = models.CharField(
        max_length=256, verbose_name='Серия документа', blank=True)
    document_number = models.CharField(
        max_length=256, verbose_name='Номер документа', blank=True)
    document_type = models.ForeignKey(Document_type, on_delete=models.CASCADE,
                                      related_name='department_type', verbose_name='Тип документа')
    status = models.CharField(
        max_length=256, verbose_name='Статус', blank=True)
    event_date = models.CharField(
        max_length=256, verbose_name='Дата события', blank=True)
    date_of_recording = models.CharField(
        max_length=256, verbose_name='Дата записи', blank=True)
    registration_authority = models.CharField(
        max_length=256, verbose_name='Орган регистрации события', blank=True)
