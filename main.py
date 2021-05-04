from scrapy.crawler import CrawlerProcess
from LyricsFinder.LyricsFinder.spiders.lyris_finder import LyricsFinderSpider
import argparse

parser=argparse.ArgumentParser(description='Get the lyrics for your favourite songs')
parser.add_argument('-s','--song_name',required=True,help='Enter name of song')

args=vars(parser.parse_args())

file=open('items.json','r+')
file.truncate(0)
file.close()

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})
query=''
name_split= args['song_name'].split()
for name in name_split[:-1]:
    query+=name+'+'
query+=name_split[-1]+'+lyrics'
# print(query)
process.crawl(LyricsFinderSpider, start_urls=["https://www.google.com/search?q="+query])
process.start()