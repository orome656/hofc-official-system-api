import aiohttp
import base64
import pydash
import json
import os

class ApiClient():
    def __init__(self):
        self.base_url = 'http://www.hofc.fr/wp-json'

    async def _map_actus(self, wp_actus):
        async with aiohttp.ClientSession() as session:
            return [{
                "id": wp_actu['id'],
                "titre": wp_actu['title']['rendered'],
                "contenu": wp_actu['content']['rendered'],
                "date_creation": wp_actu['date_gmt']+"Z",
                "image_url": pydash.get(wp_actu, '_embedded.wp:featuredmedia.0.source_url', None),
                "image_base64": base64.b64encode(await (await session.get(pydash.get(wp_actu, '_embedded.wp:featuredmedia.0.source_url', None))).read()) if pydash.get(wp_actu, '_embedded.wp:featuredmedia.0.source_url', None) is not None else None
            } for wp_actu in wp_actus]

    async def get_actus(self, limit=100, offset=0):
        page_size = 10 if limit > 10 else limit

        if os.environ.get('ENV', 'PROD') == 'DEV':
            with os.open('../mocks/mock.json') as content:
                return json.loads(content)
        else:
            async with aiohttp.ClientSession() as session:

                    async with session.get(f'{self.base_url}/wp/v2/posts?_embed&per_page={page_size}&offset={offset}') as response:

                        print("Status:", response.status)
                        print("Content-type:", response.headers['content-type'])
                        if response.status == 200:
                            return await self._map_actus(await response.json())
                        else:
                            return []