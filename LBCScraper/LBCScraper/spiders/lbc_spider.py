import scrapy
from LBCScraper.items import LbcAnnouncement

class LbcSpider(scrapy.Spider):
    name = 'lbc'
    allowed_domains = ['leboncoin.fr']
    start_urls = [
        'http://www.leboncoin.fr/ventes_immobilieres/offres/ile_de_france/?f=a&th=1&pe=14&sqs=7&ros=3&ret=1&location=Br%E9tigny-sur-Orge%2091220'
    ]

    announcements_query = '//div[@class=\'list-lbc\']/a'

    def parse(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response)

        for sel in response.xpath(LbcSpider.announcements_query):
            announcement = LbcAnnouncement()
            announcement['title'] = sel.xpath('@title').extract()[0]

            print announcement
            # yield announcement
