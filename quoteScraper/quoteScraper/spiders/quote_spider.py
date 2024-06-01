import scrapy

from quoteScraper.items import QuotescraperItem


class QuoteSpiderSpider(scrapy.Spider):
    name = "quote_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def get_quote_obj(self, quote):
        TEXT_SELECTOR = '.text::text'
        AUTHOR_SELECTOR = '.author::text'
        ABOUT_SELECTOR = '.author + a::attr("href")'
        TAGS_SELECTOR = '.tags > .tag::text'

        quote_obj = QuotescraperItem(
            quote.css(TEXT_SELECTOR).extract_first(),
            quote.css(AUTHOR_SELECTOR).extract_first(),
            'https://quotes.toscrape.com' +
            quote.css(ABOUT_SELECTOR).extract_first(),
            quote.css(TAGS_SELECTOR).extract(),
        )
        return quote_obj

    def parse(self, response):
        QUOTE_SELECTOR = '.quote'

        for quote in response.css(QUOTE_SELECTOR):
            article_item = self.get_quote_obj(quote)
            yield article_item
