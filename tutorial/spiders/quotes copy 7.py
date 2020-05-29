# -*- coding: utf-8 -*-
import scrapy

# Author and tags
class QuotesSpider(scrapy.Spider):
    name = 'quotes7'
    # allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        quoteslen = '(//div[@class="quote"]/span[@class="text"])'
        tagxp = '(//div[@class="tags"])[{}]/a/text()'
        authorxp = '(//div[@class="quote"]/span[2])[{}]/small/text()'
        lngth = len(response.xpath(quoteslen))
        
        authorlist = set()
        data = {}
        for i in range(lngth):
            tagxpath = tagxp.format(i+1)
            authorxpath = authorxp.format(i+1)
            author = response.xpath(authorxpath).get()
            authorlist.add(author)
            for i in authorlist:
                if i == author:
                    tags = response.xpath(tagxpath).getall()
                    for i in [{i:tags}]:
                        for k,v in i.items():
                            if k in data:
                                data[k].extend(v)
                            else:
                                data.update({k:v})

        nextpage = response.xpath('//li/a/@href').get()
        if nextpage is not None:
            yield response.follow(nextpage, callback=self.parse)

        yield data    
        
        
            
        
        
