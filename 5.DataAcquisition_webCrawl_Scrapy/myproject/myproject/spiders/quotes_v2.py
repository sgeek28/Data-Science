# if we want to crawl all the quotes from all the pages not only 
# 1st and last page, then we need to find class of next button on 1st page use following codeas shown below

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_v2"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.log('Saved file %s' % filename)

        for q in response.css("div.quote"):
            text=q.css('span.text::text').get()
            author=q.css('small.author::text').get()
            tags=q.css('a.tag::text').getall()
            yield {
                "text":text,
                "author":author,
                "tags":tags
            }
        
        
        #new code added
        #li.next a::attr(href) means give me anchor tag of li.next and we want to access
        #next page url which is present in href , attribute of a(anchor) tag
        # we can access next page url in other way also
        #response.css('li.next a').attrib["href"]
        next_page=response.css('li.next a::attr(href)').get()
        if next_page is not None:
            
            #this will join new link to next_page
            next_page=response.urljoin(next_page)
            
            # will make request will new url next_page and will call parse method until last page
            yield scrapy.Request(next_page,callback=self.parse)
        
            
            
            
            
            
            
