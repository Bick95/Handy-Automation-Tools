import re
import time
import requests
from bs4 import BeautifulSoup # as bs

from selenium import webdriver

# To automate download and finding of webdrivers needed to control browsers
from webdriver_manager.firefox import GeckoDriverManager  
from selenium.webdriver.common.by import By


############################### PART 1 ###############################
class WebScraper:

	def __init__(self, stream):
		self.stream = stream
		self.MAX_REPEATS = 5  # Max nr of times trying to retrieve streaming URL


	def find_query_results(self, query):
		query = query.replace(' ', '%')
		url = 'https://tunein.com/search/?query=' + query #e.g. radio%20hamburg or ndr2
		page = requests.get(url)

		soup = BeautifulSoup(page.content, 'html.parser')


		# Split Results Container into Containers
		containers = soup.findAll("div",{"id":re.compile(r"container-\d")})


		# Iterate through Containers and find that one containing Radio Stations
		station_contents = None
		for item in containers:
			category = item.find("div",{"class":"container-title__titleHeader___T_Nit"})

			if 'Stations' in category:
				station_contents = item
				break


		# Extract all radio stations and find their corresponding stream link
		station_items = soup.findAll("div",{"class":"row guide-item__guideItemContainer___1-ViC"})

		stations = []
		urls = []

		# Examine all list items, one per radio station...
		for station in station_items:
			ref_item = station.find("a",{"class":"guide-item__guideItemPlayButtonContainer___cVDuk guide-item__guideItemLink___3w_uL common__link___1BB3z"})
			if ref_item is not None:
				href_text = ref_item['href']
				if '/radio/' in href_text:
					stations.append(station['data-nexttitle'])
					urls.append('https://tunein.com' + href_text)

		return stations, urls


	def query_selection(self, stations, urls):

		for i in range(len(stations)):
			self.stream.show('[' + str(i) + ']\t' + stations[i] + '\t' + urls[i])

		try: selected = int(input('Which index to select? ')) 
		except Exception: return None, None

		self.stream.show('Selected:\t', stations[selected], '\t', urls[selected])
		return stations[selected], urls[selected]


	def get_browser(self, headless=True):
		# Check whether Firefox available
		# TODO

		# Set options how to execute Firefox Browser
		fireFoxOptions = webdriver.FirefoxOptions()  # For setting headless etc. 
		fireFoxOptions.headless = True

		# Instentiate browser and load URL

		# Create webbrowser/'driver' to control browser
		browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=fireFoxOptions)
		return browser


	def _stream_url(self, tunein_url):

		# Open/retrieve loaded page
		browser = self.get_browser()

		attempt = 0
		while attempt < self.MAX_REPEATS:
			self.stream.show('Attempt', attempt, 'of trying to retrieve straming URL.')
			try: 
				browser.get(tunein_url)  

				# Click play button
				play_button = browser.find_element(By.CLASS_NAME, 'tune-button__solid___Q8CzZ')  # Get access to play button
				play_button.click()  # Click play button
				self.stream.show('Waiting for page to be loaded..')
				time.sleep(20)  # driver.implicitly_wait(5)
				self.stream.show('Done waiting.')

				# Retrieve streaming URL
				element = None
				identifier_ = 'jp_audio_'
				nr = 0

				while element is None and nr < 10:
					identifier = identifier_ + str(nr)
					try:
						link_element = browser.find_element(By.ID, identifier)
						self.stream.show('1.', link_element)
						self.stream.show('2.', link_element.get_attribute("src").split('?'))
						element = link_element.get_attribute("src").split('?')[0]
					except Exception:
						self.stream.show('Doesn\'t exist: ', identifier)
					nr += 1

				if element is not None:
					self.stream.show('Finally: ', element)
					return element
				else: attempt += 1

			except Exception:
				attempt += 1

		return None


	def get_stream_url(self):

		query = input('Enter name of radio station: ')
		stations, urls = self.find_query_results(query)
		station, tunein_url = self.query_selection(stations, urls)
		if station is not None and tunein_url is not None:
			stream_url = self._stream_url(tunein_url)
			return station, stream_url
		else:
			return None, None

