# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os

class JsonWriterPipeline(object):

    result_file = 'results.json'

    def __init__(self):
        if os.path.exists(JsonWriterPipeline.result_file):
            os.remove(JsonWriterPipeline.result_file)

        self.file = open(JsonWriterPipeline.result_file, 'w')

    def __del__(self):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + ",\n"
        self.file.write(line)
        return item