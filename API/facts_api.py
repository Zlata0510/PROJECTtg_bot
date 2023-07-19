from API.base import BaseApi


class FactsApi(BaseApi):
    async def get_facts(self):
        answer = await self.get(f'https://uselessfacts.jsph.pl/api/v2/facts/random')

        return answer['text']


facts_api = FactsApi()
