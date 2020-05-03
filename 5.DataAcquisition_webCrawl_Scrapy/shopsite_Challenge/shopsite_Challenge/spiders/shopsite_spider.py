import scrapy


class ShopsiteSpider(scrapy.Spider):
    name="bookstore"
    book_urls=[
        'http://books.toscrape.com/catalogue/'
    ]
    start_urls=[
        'http://books.toscrape.com/'
    ]
    def start_requests(self):
        
        urls=[
            'http://books.toscrape.com/catalogue/page-1.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
   
    def parse(self,response):
        page_id=response.url.split("/")[4][-6]
        filename='books-%s.html'%page_id
       
        for b in response.css("article.product_pod"):
            book_titles=''
            image_url=b.css("a img::attr(src)").get()
            book_title=b.css('h3 a::attr(title)').get()
            product_price=b.css('p.price_color::text').get()
            #book_url=self.book_urls[0]+b.css("div a::attr(href)").get()
            
            if "," in book_title:
                book_titles+='"'+book_title+'"'
            else:
                book_titles+=book_title

            yield{
                "image_url":image_url,                
                "book_title":book_titles,
                "product_price":product_price,
                #"book_url":book_url,
                
            }
        next_page=response.css('ul.pager li.next a::attr(href)').get()
        if next_page is not None:
            #this will join new link to next_page
            next_page=response.urljoin(next_page)
            # will make request will new url next_page and will call parse method until last page
            yield scrapy.Request(next_page,callback=self.parse)
        
        
        
