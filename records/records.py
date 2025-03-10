# skeleton of a class
import toyplot
import requests
import pandas as pd


class Records:
    def __init__(self, genusKey=None, year=None):

        # store input params
        self.genusKey = genusKey
        self.year = year
        self.base_url = "http://api.gbif.org/v1/occurrence/search"

        # will be used to store output results
        self.df = None
        self.json = None

    def get_single_batch(self, offset=0, limit=20):
        "returns JSON result for a small batch query"
        params = {
            "genusKey": self.genusKey,
            "year": self.year,
            "offset": offset,
            "limi": limit
        }
        response = requests.get(self.base_url, params = params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
            
        

    def get_all_records(self):
        "stores result for all records to self.json and self.df"
        all_results = []
        offset = 0
        limit = 300

        while True:
            batch = self.get_single_batch(offset = offset, limit = limit)
            records = batch.get("results", [])
            if not records:
                break
            all_results.extend(records)
            offset+=limit
        self.json = all_results
        self.df = pd.DataFrame(all_results)
