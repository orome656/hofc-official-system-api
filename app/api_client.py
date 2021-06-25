import aiohttp

class ApiClient():
    def __init__(self):
        self.base_url = 'http://www.hofc.fr/wp-json'

    def _map_actus(self, wp_actus):
        return [{
            "id": wp_actu['id']
        } for wp_actu in wp_actus]

    async def get_actus(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.base_url}/wp/v2/posts') as response:

                print("Status:", response.status)
                print("Content-type:", response.headers['content-type'])

                return self._map_actus(await response.json())