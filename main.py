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

# print('lyrics' in 'I am a Lyrics')
# print('Lyrics' in 'Tera Yaar Hoon Main Lyrics in Hindi, Sonu Ke Titu Ki Sweety Tera ...gaana.com › Hindi Songs › Tera Yaar Hoon Main')
# print('lyrics' in 'https://www.google.com/url?q=https://gaana.com/lyrics/tera-yaar-hoon-main&sa=U&ved=2ahUKEwj2pLaoo7DwAhUUA3IKHWMYBjEQFjABegQIAxAB&usg=AOvVaw3f0WP4qc3rGSY67ShH_AY-' and 'lyrics' in str('Tera Yaar Hoon Main Lyrics in Hindi, Sonu Ke Titu Ki Sweety Tera ...gaana.com › Hindi Songs › Tera Yaar Hoon Main').lower())