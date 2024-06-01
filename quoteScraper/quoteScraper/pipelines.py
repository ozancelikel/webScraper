from itemadapter import ItemAdapter
import pymongo
from scrapy.utils.project import get_project_settings
from dataclasses import asdict

from quoteScraper.items import QuotescraperItem

settings = get_project_settings()


class MongoDBPipeline:
    def __init__(self):
        conn = pymongo.MongoClient(
            settings.get('MONGO_HOST')
        )
        db = conn[settings.get('MONGO_DB_NAME')]
        self.collection = db[settings['MONGO_COLLECTION_NAME']]

    def process_item(self, item, spider):
        if isinstance(item, QuotescraperItem):  # article item
            self.collection.insert_one(asdict(item))
        return item
