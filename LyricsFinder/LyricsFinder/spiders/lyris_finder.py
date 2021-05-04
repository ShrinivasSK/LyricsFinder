import scrapy
from scrapy.linkextractors import LinkExtractor

class LyricsFinderSpider(scrapy.Spider):
    name = 'lyris_finder'

    def parse(self, response):
        xlink = LinkExtractor()
        for link in xlink.extract_links(response):
            if 'lyrics' in link.url and 'lyrics' in link.text:
                yield {'link': str(link)}

