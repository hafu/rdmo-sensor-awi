import logging
import requests

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

from rdmo.projects.models import Value
from rdmo.domain.models import Attribute

BASE_URL = 'https://sensor.awi.de/rest/search/sensor?q=uniqueId:{id_}&hits=1'

attribute_mapping = {
    'http://rdmo-dev.local/terms/domain/sensor/awi/type-name': 'typeName',
    'http://rdmo-dev.local/terms/domain/sensor/awi/name': 'shortName',
    'http://rdmo-dev.local/terms/domain/sensor/awi/serial': 'serial',
}


logger = logging.getLogger(__name__)

@receiver(post_save, sender=Value)
def post_save_project_values(sender, **kwargs):
    # logger.debug('Call of post_save_project_values')
    # print('Call of post_save_project_values')
    instance = kwargs.get("instance", None)
    if instance and instance.attribute.uri == 'http://rdmo-dev.local/terms/domain/sensor/awi/search':
        # print(f'Attribute of instance: {instance.attribute.uri}')
        # print(f'Attribute of type: {type(instance.attribute)}')
        # print(f'External ID: {instance.external_id}')
        # print(instance.attribute.uri == 'http://rdmo-dev.local/terms/domain/sensor/awi/search')
        if instance.external_id:
            request_url = BASE_URL.format(id_=instance.external_id)
            # print(f'Request URL {request_url}')
            # TODO: proper error handling
            response = requests.get(request_url)
            json_data = response.json()
            # go through attributes (hopefully predefined in questions)
            for attribute, source_attribute in attribute_mapping.items():
                # print(f'attribute {attribute}, source_attribute {source_attribute}')
                # check for key error
                attribute_value = json_data['records'][0]['metadata'][source_attribute]
                attribute_object = Attribute.objects.get(uri=attribute)
                obj, created = Value.objects.update_or_create(
                    project=instance.project,
                    attribute=attribute_object,
                    defaults={
                        'project': instance.project,
                        'attribute': attribute_object,
                        'text': attribute_value,
                    }
                )
                # print(f'created: {created}, object: {obj}')


