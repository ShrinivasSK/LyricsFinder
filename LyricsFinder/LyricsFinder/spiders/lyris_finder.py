import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.response import open_in_browser

'''
Websites I can  scrape:
1. Genius
2. Lyrics.com
3. Metrolyrics

4. Lyricsily
5. Jiosaavn
6. Gaana

7. hinditracks
8. Lyricsmint
9. Jiosaavn
'''

class LyricsFinderSpider(scrapy.Spider):
    name = 'lyris_finder'

    # def parse(self, response):
    #     xlink = LinkExtractor()
    #     for link in xlink.extract_links(response):
    #         # print("Yo"+str(link),'lyrics' in link.url,'lyrics' in link.text)
    #         if 'lyrics' in link.url and 'lyrics' in str(link.text).lower():
    #             yield {'link': str(link)}

    def parse(self, response):
        xlink = LinkExtractor()
        link=[link for link in xlink.extract_links(response) if str(link.url).find('genius')!=-1]
        if(len(link)!=0):
            print(link[0].url)
            yield scrapy.Request(link[0].url,callback=self.parseGenius)
        # else:
        # for link in xlink.extract_links(response):
        # # print("Yo"+str(link),'lyrics' in link.url,'lyrics' in link.text)
        #     if 'lyrics' in link.url and 'lyrics' in str(link.text).lower():
        #         yield {'link': str(link)}
    
    def parseGenius(self,response):
        # open_in_browser(response)
        lyrics=response.css('.lyrics p').css('::text').extract()
        yield {'lyrics': lyrics}

