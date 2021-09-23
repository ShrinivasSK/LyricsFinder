import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.response import open_in_browser

'''
Websites I can  scrape:
1. Genius - sometimes empty
2. azlyrics - does not allow
3. Metrolyrics

4. Lyricsily - gives garbage too 
5. Jiosaavn - does not allow
6. Gaana- sometimes empty if non lyrics one

7. Lyricsmint - done
8. ilyricshub - done
9. lyrics.com

10. 

Does not give for songs like khali khali, Aise kyu
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
        data={}
        for id,link in enumerate(xlink.extract_links(response)):
            # print("Yo"+str(link),'lyrics' in link.url,'lyrics' in link.text)
            if 'lyrics' in link.url and 'lyrics' in str(link.text).lower():
                data[str(id)]={'link': str(link)}
        yield data


        link = [link for link in xlink.extract_links(
            response) if str(link.url).find('lyricsmint') != -1]
        if(len(link) != 0):
            # print(link[0].url)
            yield scrapy.Request(link[0].url, callback=self.parseLyricsMint)

        link = [link for link in xlink.extract_links(
            response) if str(link.url).find('gaana') != -1]
        if(len(link) != 0):
            # print(link[0].url)
            yield scrapy.Request(link[0].url, callback=self.parseGaana)

        link = [link for link in xlink.extract_links(
            response) if str(link.url).find('metrolyrics') != -1]
        if(len(link) != 0):
            # print(link[0].url)
            yield scrapy.Request(link[0].url, callback=self.parseMetrolyics)

        link = [link for link in xlink.extract_links(
            response) if str(link.url).find('genius') != -1]
        if(len(link) != 0):
            # print(link[0].url)
            yield scrapy.Request(link[0].url, callback=self.parseGenius)

        # link = [link for link in xlink.extract_links(
        #     response) if str(link.url).find('lyricsily') != -1]
        # if(len(link) != 0):
            # print(link[0].url)
        #     yield scrapy.Request(link[0].url, callback=self.parseLyricsily)

        link = [link for link in xlink.extract_links(
            response) if str(link.url).find('ilyricshub') != -1]
        if(len(link) != 0):
            # print(link[0].url)
            yield scrapy.Request(link[0].url, callback=self.parseILyricsHub)
        
        link = [link for link in xlink.extract_links(
            response) if str(link.url).find('karoke') != -1]
        if(len(link) != 0):
            # print(link[0].url)
            yield scrapy.Request(link[0].url, callback=self.parseAZLyrics)
        
        link = [link for link in xlink.extract_links(
            response) if str(link.url).find('karaoke-lyrics') != -1]
        if(len(link) != 0):
            # print(link[0].url)
            yield scrapy.Request(link[0].url, callback=self.parseKarokeLyrics)
        
        link = [link for link in xlink.extract_links(
            response) if str(link.url).find('crownlyric') != -1]
        if(len(link) != 0):
            # print(link[0].url)
            yield scrapy.Request(link[0].url, callback=self.parseCrownLyric)

        link = [link for link in xlink.extract_links(
            response) if str(link.url).find('songlyrics') != -1]
        if(len(link) != 0):
            # print(link[0].url)
            yield scrapy.Request(link[0].url, callback=self.parseSongLyrics)

        link = [link for link in xlink.extract_links(
            response) if str(link.url).find('smule') != -1]
        if(len(link) != 0):
            # print(link[0].url)
            yield scrapy.Request(link[0].url, callback=self.parseSmule)

    def parseGenius(self, response):
        # open_in_browser(response)
        lyrics = response.css('.lyrics p').css('::text').extract()
        yield {'lyrics': lyrics, 'source': 'Genius'}

    def parseLyricsily(self, response):
        lyrics = response.css('p::text').extract()
        yield {'lyrics': lyrics, 'source': 'Lyricsily'}

    def parseGaana(self, response):
        lyrics = response.css('.lyr_data p').css('::text').extract()
        yield {'lyrics': lyrics, 'source': 'Gaana'}

    def parseMetrolyics(self, response):
        lyrics = response.css('.verse::text').extract()
        yield {'lyrics': lyrics, 'source': 'Metrolyrics'}

    def parseILyricsHub(self, response):
        lyrics = response.css('.song_lyrics p').css('::text').extract()
        yield {'lyrics': lyrics, 'source': 'I Lyrics Hub'}

    def parseLyricsMint(self, response):
        lyrics = response.css('.pb-2 p').css('::text').extract()
        yield {'lyrics': lyrics, 'source': 'Lyrics Mint'}

    def parseAZLyrics(self,response):
        lyrics = response.css('h2+ p , p+ p').css('::text').extract()
        yield {'lyrics': lyrics, 'source': 'Karoke.in'}

    def parseKarokeLyrics(self,response):
        lyrics = response.css('.para_1lyrics_col1').css('::text').extract()
        yield {'lyrics': lyrics, 'source': 'Karoke Lyrics.in'}

    def parseCrownLyric(self,response):
        lyrics = response.css('.has-text-align-cente').css('::text').extract()
        yield {'lyrics': lyrics, 'source': 'Crown Lyrics'}

    def parseSongLyrics(self,response):
        lyrics = response.css('.pg_close-ad-btn-content , #songLyricsDiv').css('::text').extract()
        yield {'lyrics': lyrics, 'source': 'Song Lyrics'}

    def parseSmule(self,response):
        lyrics = response.css('.p').css('::text').extract()
        yield {'lyrics': lyrics, 'source': 'Smule'}