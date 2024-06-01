import scrapy
from dataclasses import dataclass
import pymongo

@dataclass
class QuotescraperItem:
    text: str
    author: str
    about: str
    tags: str