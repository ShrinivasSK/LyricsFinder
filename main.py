from scrapy.crawler import CrawlerProcess
from LyricsFinder.LyricsFinder.spiders.lyris_finder import LyricsFinderSpider
import argparse
from scrapy import signals
from scrapy.signalmanager import dispatcher
import json
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings
import os


parser = argparse.ArgumentParser(
    description='Get the lyrics for your favourite songs')
parser.add_argument('-s', '--song_name', required=True,
                    help='Enter name of song')

args = vars(parser.parse_args())

file = open('items.json', 'r+')
file.truncate(0)
file.close()


def spider_results():
    results = []
    settings = Settings()

    os.environ['SCRAPY_SETTINGS_MODULE'] = 'LyricsFinder.LyricsFinder.settings'
    settings_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
    settings.setmodule(settings_module_path, priority='project')

    process = CrawlerProcess(settings)

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_passed)

    query = ''
    name_split = args['song_name'].split()
    for name in name_split[:-1]:
        query += name+'+'
    query += name_split[-1]+'+lyrics'
    # print(query)
    process.crawl(LyricsFinderSpider, start_urls=[
        "https://www.google.com/search?q="+query])
    process.start()
    return results


def cvtToJson(results):
    data = {}
    data['num'] = 0
    data['sources'] = []
    for res in results[1:]:
        # if(len(res['lyrics']) != 0):
        data['num'] += 1
        data['sources'].append(res['source'])
        data[res['source']] = res['lyrics']
    return data


def printResultsJson(res):
    print("{} results recieved".format(res['num']))
    for src in res['sources']:
        print("Received From: {}".format(src))
        print("Lyrics: {}\n".format(res[src]))


if __name__ == '__main__':
    results = spider_results()
    # print(results)
    y = cvtToJson(results)
    printResultsJson(y)

# print('lyrics' in 'I am a Lyrics')
# print('Lyrics' in 'Tera Yaar Hoon Main Lyrics in Hindi, Sonu Ke Titu Ki Sweety Tera ...gaana.com › Hindi Songs › Tera Yaar Hoon Main')
# print('lyrics' in 'https://www.google.com/url?q=https://gaana.com/lyrics/tera-yaar-hoon-main&sa=U&ved=2ahUKEwj2pLaoo7DwAhUUA3IKHWMYBjEQFjABegQIAxAB&usg=AOvVaw3f0WP4qc3rGSY67ShH_AY-' and 'lyrics' in str('Tera Yaar Hoon Main Lyrics in Hindi, Sonu Ke Titu Ki Sweety Tera ...gaana.com › Hindi Songs › Tera Yaar Hoon Main').lower())
