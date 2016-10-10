import scrapy

import requests
from bs4 import BeautifulSoup

from collections import OrderedDict

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

class Counter:
	count = 1
	#pageCount = 2

class responseObj:
	r = requests.session()
	r.post('http://store.steampowered.com/agecheck/app/307780/', data = {'ageDay':'1', 'ageMonth': 'January','ageYear': '1992', })

class QuotesSpider(scrapy.Spider):
	name = "games"
	start_urls = [
		'http://store.steampowered.com/search/?tags=-1&category1=998',
	]
	def parse(self, response):

		for quote in response.xpath('//div[@id="search_result_container"]//a[contains(@href, "app")]'):
			# yield{
			# 	'Num' : Counter.count,
			# 	'Title': quote.css('span.title::text').extract_first(),
			# 	'Link': quote.xpath('@href').extract_first(),
			# }
			yield self.getData(quote.xpath('@href').extract_first())
			Counter.count += 1

		nplist = response.xpath('//div[@class="search_pagination_right"]//a[@class="pagebtn"]/@href').extract()
		next_page = nplist[-1]


		if Counter.count <= 4000:
			print(next_page)
			next_page = response.urljoin(next_page)
			print(next_page)
			yield scrapy.Request(next_page, callback=self.parse)

	def getData(self, url):
		r = responseObj.r.get(url, headers = headers)

		with open('./html/steam' + str(Counter.count) + '.html', 'wb') as fd:
			for chunk in r.iter_content(1024):
				fd.write(chunk)

		soup = BeautifulSoup(r.text, 'html.parser')

		gameName = soup.find("div",class_= "apphub_AppName")
		if gameName is None:
		    gameName = ""
		else:
		    gameName = gameName.text
		#print gameName


		release = soup.find("span",{"class" : "date"})
		if release is None:
		    release = ""
		else:
		    release = release.text
		#print release

		all = soup.find("div", class_="block_content_inner")
		if all is None:
			return

		alldiv = all.find("div")

		genreOri = ""
		genreNew = ""
		genre = ""

		genreRow = alldiv.find('b', string = 'Genre:')
		if genreRow is not None:
			nextSibs = genreRow.find_next_siblings('a')
			for nextSib in nextSibs:
			    genreNew = nextSib.text
			    genre = genreOri + "/" + genreNew
			    genreOri = genre
			print genre

		developerOri = ""
		developerNew = ""
		developer = ""

		developerRow = alldiv.find('b', string = "Developer:")
		if developerRow is not None:
			nextSibs = developerRow.find_next_siblings('a')
			for nextSib in nextSibs:
			    developerNew = nextSib.text
			    developer = developerOri + "/" + developerNew
			    developerOri = developer
			print developer

		publisherOri = ""
		publisherNew = ""
		publisher = ""

		publisherRow = alldiv.find('b', string = "Publisher:")
		if publisherRow is not None:
			nextSibs = publisherRow.find_next_siblings('a')
			for nextSib in nextSibs:
			    publisherNew = nextSib.text
			    publisher = publisherOri + "/" + publisherNew
			    publisherOri = publisher
			print publisher



		# all = soup.find("div", class_="block_content_inner")
		# if all is None:
		# 	return None


		# alldiv = all.find("div")
		# allA = alldiv.find_all("a")

		# genreori = ""
		# genrenew = ""
		# genre = ""
		# i=0
		# while i<(len(allA)-2):
		# 	genrenew = allA[i].text
		# 	genre = str(genrenew) + "/" +str(genreori)
		# 	genreori = genre
		# 	i += 1
		# #print genre

		# publish = allA[-1]
		# if publish is None:
		#     publisher = ""
		# else:
		#     publisher = publish.text
		#     # while "," in publisher:
		#     #     publisher = publisher.replace(",","/")
		#     publisher = publisher.strip()
		# #print publisher

		# developer = allA[-2]
		# if developer is None:
		#     developer = ""
		# else:
		#     developer = developer.text
		#     # while "," in developer:
		#     #     developer = developer.replace(",","/")
		#     developer = developer.strip()
		# 	#print developer

		review = soup.find("span",{"itemprop" : "description"})
		review_detail = soup.find("span",{"class" : "nonresponsive_hidden responsive_reviewdesc"})
		if review is None:
		    review = ""
		    review_detail = ""
		else:
		    review = review.text
		    review_detail = review_detail.text
		    review_detail = review_detail.strip()
		#print review
		#print review_detail

		result = OrderedDict()
		result['id'] = Counter.count
		result['title'] = gameName
		result['releaseDate'] = release
		result['publisher'] = publisher
		result['developer'] = developer
		result['genre'] = genre
		result['review'] = review
		result['review_detail'] = review_detail
		

		# result = {
		# 	'id': Counter.count,
		# 	'title': gameName,
		# 	'releaseDate': release,
		# 	'publisher': publisher,
		# 	'developer': developer,
		# 	'genre': genre,
		# 	'review': review,
		# 	'review_detail': review_detail,
		# }
	
		return result

