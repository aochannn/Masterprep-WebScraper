import scrapy
from ..items import UnirankItem
import csv
class SchoolsSpider(scrapy.Spider):
    # urls = [
    #     'https://www.forbes.com/top-colleges/'
    # ]
    name = "schools"
    page_num = 2
    def start_requests(self):
        yield scrapy.Request(
            url = 'https://www.niche.com/colleges/search/best-colleges/?page=4',
            meta = {
                "playwright" : True,
            }
        )
   
    

    def parse(self, response):
        rows=[]
        items = UnirankItem()

        # schools = response.css('div.Table_tableRow__M82uU')
        # for school in schools:
        #     name = school.css('div.Table_organizationName__n0jEN::text').get()
        #     items['name'] = name
        names = response.css('.nss-rilmyj .nss-w5w7xf::text').getall()
        # second = response.css('.table a::text').getall()
        # for i in range(len(second)):
        #     names.append(second[i])
        # names = names[:100]
        # names=names[:100]

        with open('output.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        for i in range(len(names)):
            rows[i][0] = names[i]
        with open('cons.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)
        yield {
            'us':names,
        }
        # next_page = 'https://www.niche.com/colleges/search/best-colleges/?page='+str(SchoolsSpider.page_num)
        # if SchoolsSpider.page_num<=4:
        #     SchoolsSpider.page_num += 1
        #     yield response.follow(next_page, callback=self.parse)