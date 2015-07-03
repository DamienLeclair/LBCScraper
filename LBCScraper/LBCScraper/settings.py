# -*- coding: utf-8 -*-

# Scrapy settings for LBCScraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'LBCScraper'

SPIDER_MODULES = ['LBCScraper.spiders']
NEWSPIDER_MODULE = 'LBCScraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'LBCScraper (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
    'LBCScraper.middlewares.ForceUTF8Response': 100,
}

ITEM_PIPELINES = {
    # 'LBCScraper.pipelines.JsonWriterPipeline': 100,
}
