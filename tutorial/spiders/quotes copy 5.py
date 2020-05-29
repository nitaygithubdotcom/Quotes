# -*- coding: utf-8 -*-
import scrapy

# Author and quotes
class QuotesSpider(scrapy.Spider):
    name = 'quotes5'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        quoteslen = '(//div[@class="quote"]/span[@class="text"])'
        quotesxp = '(//div[@class="quote"]/span[@class="text"])[{}]/text()'
        authorxp = '(//div[@class="quote"]/span[2])[{}]/small/text()'
        lngth = len(response.xpath(quoteslen))
        
        authorlist = set()
        data = {}
        for i in range(lngth):
            quotesxpath = quotesxp.format(i+1)
            authorxpath = authorxp.format(i+1)
            author = response.xpath(authorxpath).get()
            authorlist.add(author)
            for i in authorlist:
                if i == author:
                    quotes = response.xpath(quotesxpath).get()
                    for i in [{i:[quotes]}]:
                        for k,v in i.items():
                            if k in data:
                                data[k].append(v[0])
                            else:
                                data.update({k:v})

        yield data
        
            
        
        
