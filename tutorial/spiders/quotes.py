# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        quoteslen = '(//div[@class="quote"]/span[@class="text"])'
        quotesxp = '(//div[@class="quote"]/span[@class="text"])[{}]/text()'
        lngth = len(response.xpath(quoteslen))
        for i in range(lngth):
            quotesxpath = quotesxp.format(i+1)
            quotes = response.xpath(quotesxpath).get()

        
        authorlen = '(//div[@class="quote"]/span[2])'
        authorxp = '(//div[@class="quote"]/span[2])[{}]/small/text()'
        lngth = len(response.xpath(authorlen))
        for  i in range(lngth):
            authorxpath = authorxp.format(i+1)
            author = response.xpath(authorxpath).get()

        taglen = '(//div[@class="tags"])'
        tagxp = '(//div[@class="tags"])[{}]/a/text()'
        lngth = len(response.xpath(taglen))
        for i in range(lngth):
            tagxpath = tagxp.format(i+1)
            tags = response.xpath(tagxpath).getall()
        
        yield {"Quotes":quotes,"Author":author,"Tags":tags}
