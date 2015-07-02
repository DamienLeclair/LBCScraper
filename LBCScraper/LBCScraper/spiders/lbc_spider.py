import scrapy
import urllib2
from LBCScraper.items import LbcAnnouncement


class LbcSpider(scrapy.Spider):

    name = 'lbc'
    allowed_domains = ['leboncoin.fr']
    start_urls = [
        'http://www.leboncoin.fr/ventes_immobilieres/offres/ile_de_france/?f=a&th=1&pe=14&sqs=7&ros=3&ret=1&location=Br%E9tigny-sur-Orge%2091220'
    ]

    # Main container
    container_main = '//div[@id=\'ContainerMain\']'
    # List
    list_lbc = container_main + '/div/div/div[@class=\'list-lbc\']/a'
    # Item
    lbc_container = container_main + '/div/div/div[@class=\'lbcContainer\']'

    def __init__(self):
        self.index = 0

    def run_debug_shell(self, response):
        from scrapy.shell import inspect_response

        inspect_response(response)

    def parse(self, response):
        # self.run_debug_shell(response)

        for sel in response.xpath(LbcSpider.list_lbc):
            # announcement = LbcAnnouncement()
            # announcement['title'] = sel.xpath('@title').extract()[0]
            #
            # print announcement
            # # yield announcement
            url = sel.xpath('@href').extract()[0]
            yield scrapy.Request(url, callback=self.parse_announcement)

    def parse_announcement(self, response):
        # self.run_debug_shell(response)

        title = response.xpath(LbcSpider.lbc_container + '/div[@class=\'header_adview\']/h1/text()').extract()[0]

        # print title
        # print type(title)
        print str.format('[{}] ', self.index) + title
        self.index += 1

        announcement = LbcAnnouncement()
        announcement['title'] = title
        # yield announcement
