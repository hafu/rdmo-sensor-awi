import logging
import requests

from rdmo.options.providers import Provider


logger = logging.getLogger(__name__)


class SensorAWIProvider(Provider):

    search = True

    API_MAX_HITS = 10
    API_BASE_URL = f'https://sensor.awi.de/rest/search/sensor?hits={API_MAX_HITS}&q='

    def get_options(self, project, search=None):
        # Only run search if we have a term or at least 3 characters
        if not search or len(search) < 3:
            return []

        logger.debug(f'Search term: {search}')
        # TODO: Add proper error handling
        response = requests.get(f'{self.API_BASE_URL}{search}')

        json_data = response.json()
        results = []
        for data_set in json_data["records"]:
            results.append(
                {
                    'id': data_set['id'],
                    'text': data_set['title']
                }
            )

        logger.debug(f'Results: {results}')

        return results
