from django.conf import settings
from datetime import datetime
from django.utils import dateformat

# Форматирование даты
formatted_date = dateformat.format(datetime.now(), settings.DATE_FORMAT)

