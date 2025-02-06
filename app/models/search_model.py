import asyncio
from concurrent.futures import ThreadPoolExecutor
from scrapers.amazon.amazon_spyder import AmazonSpyder
from scrapers.olx.olx_spyder import OLX_Spyder
from scrapers.badr.badr_spyder import BadrSpyder
from scrapers.sigma.sigma_spyder import SigmaSpyder
from scrapers.alfrensia.alfrensia_spyder import ALFrensia_Spyder
from scrapers.baraka.baraka_spyder import BarakaSpyder

class SearchModel:
    def run_spyder(self, spyder, method, *args):
        return asyncio.run(method(*args))
    
    async def async_search_products(self, search_term, source_filters):
        results = {
            'amazon': [],
            'olx': [],
            'badr': [],
            'sigma': [],
            'alfrensia': [],
            'baraka': [],
        }

        with ThreadPoolExecutor() as executor:
            loop = asyncio.get_event_loop()
            tasks = []

            if source_filters.get('amazon'):
                amazon_spyder = AmazonSpyder()
                tasks.append(loop.run_in_executor(executor, self.run_spyder, amazon_spyder, amazon_spyder.scrap, search_term))

            if source_filters.get('olx'):
                olx_spyder = OLX_Spyder(search_term)
                tasks.append(loop.run_in_executor(executor, self.run_spyder, olx_spyder, olx_spyder.scrape))

            if source_filters.get('badr'):
                badr_spyder = BadrSpyder()
                tasks.append(loop.run_in_executor(executor, self.run_spyder, badr_spyder, badr_spyder.scrap, search_term))

            if source_filters.get('sigma'):
                sigma_spyder = SigmaSpyder(search_term)
                tasks.append(loop.run_in_executor(executor, self.run_spyder, sigma_spyder, sigma_spyder.scrap))

            if source_filters.get('alfrensia'):
                alfrensia_spyder = ALFrensia_Spyder()
                tasks.append(loop.run_in_executor(executor, self.run_spyder, alfrensia_spyder, alfrensia_spyder.scrap, search_term))

            if source_filters.get('baraka'):
                baraka_spyder = BarakaSpyder()
                tasks.append(loop.run_in_executor(executor, self.run_spyder, baraka_spyder, baraka_spyder.scrap, search_term))

            results_list = await asyncio.gather(*tasks, return_exceptions=True)

        if source_filters.get('amazon'):
            if len(results_list) > 0 and isinstance(results_list[0], Exception):
                results['amazon'] = [f"Error scraping Amazon: {str(results_list[0])}"]
            elif len(results_list) > 0:
                results['amazon'] = results_list[0] or []

        if source_filters.get('olx'):
            if len(results_list) > 1 and isinstance(results_list[1], Exception):
                results['olx'] = [f"Error scraping OLX: {str(results_list[1])}"]
            elif len(results_list) > 1:
                results['olx'] = results_list[1] or []

        if source_filters.get('badr'):
            if len(results_list) > 2 and isinstance(results_list[2], Exception):
                results['badr'] = [f"Error scraping Badr: {str(results_list[2])}"]
            elif len(results_list) > 2:
                results['badr'] = results_list[2] or []

        if source_filters.get('sigma'):
            if len(results_list) > 3 and isinstance(results_list[3], Exception):
                results['sigma'] = [f"Error scraping Sigma: {str(results_list[3])}"]
            elif len(results_list) > 3:
                results['sigma'] = results_list[3] or []

        if source_filters.get('alfrensia'):
            if len(results_list) > 4 and isinstance(results_list[4], Exception):
                results['alfrensia'] = [f"Error scraping ALFrensia: {str(results_list[4])}"]
            elif len(results_list) > 4:
                results['alfrensia'] = results_list[4] or []

        if source_filters.get('baraka'):
            if len(results_list) > 5 and isinstance(results_list[5], Exception):
                results['baraka'] = [f"Error scraping Baraka: {str(results_list[5])}"]
            elif len(results_list) > 5:
                results['baraka'] = results_list[5] or []

        return results