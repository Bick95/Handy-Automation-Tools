import re
import requests
from bs4 import BeautifulSoup # as bs


############################### PART 1 ###############################

url = 'https://tunein.com/search/?query=radio%20hamburg' #ndr2
page = requests.get(url)

#print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')


# Split Results Container into Containers
containers = soup.findAll("div",{"id":re.compile(r"container-\d")})


# Iterate through Containers and find that containing Radio Stations
station_contents = None
for item in containers:
	category = item.find("div",{"class":"container-title__titleHeader___T_Nit"})
	#print('+++++ ', category, ' +++++')
	# TODO: extract content... by regex? >*</div>
	if 'Stations' in category:
		#print('----------------- Found!: ', category)
		station_contents = item
		break

#print(item)


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
			#urls.append('https://tunein.com/radio/' + href_text.split('/')[2]) # Extract constructor for station's private URL
			urls.append('https://tunein.com' + href_text)


for i in range(len(stations)):
	print('[' + str(i) + ']\t' + stations[i] + '\t' + urls[i])

selected = int(input('Which index to select? '))
#print(selected)


print('Selected:\t', stations[selected], '\t', urls[selected])



############################### PART 2 ###############################

selected_url = urls[selected]

import time
# Make sure WebDriver is available
from selenium import webdriver

# To automate download and finding of webdrivers needed to control browsers
from webdriver_manager.firefox import GeckoDriverManager  
from selenium.webdriver.common.by import By

# Check whether Firefox available

# Set options how to execute Firefox Browser

fireFoxOptions = webdriver.FirefoxOptions()  # For setting headless etc. 
#fireFoxOptions.set_headless()  # Deprecated
fireFoxOptions.headless = True

# Instentiate browser and load URL

# Create webbrowser/'driver' to control browser
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=fireFoxOptions)
browser.get(selected_url)  # Open/retrieve loaded page

# Click play button

play_button = browser.find_element(By.CLASS_NAME, 'tune-button__solid___Q8CzZ')  # Get access to play button
play_button.click()  # Click play button
print('Waiting for page to be loaded..')
time.sleep(20)  # driver.implicitly_wait(5)
print('Done waiting.')

# Retrieve streaming URL

element = None
identifier_ = 'jp_audio_'
nr = 0

while element is None:
	identifier = identifier_ + str(nr)
	try:
		link_element = browser.find_element(By.ID, identifier)
		print('1.', link_element)
		print('2.', link_element.get_attribute("src").split('?'))
		element = link_element.get_attribute("src").split('?')[0]
	except Exception():
		print('Doesn\'t exist: ', identifier)
	nr += 1

print('Finally: ', element)





#from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
# Step 1) Open Firefox 
#browser = webdriver.Firefox()
# Step 2) Navigate to Facebook
#browser.get("http://www.bild.de")
# Step 3) Search & Enter the Email or Phone field & Enter Password
#username = browser.find_element_by_id("email")
#password = browser.find_element_by_id("pass")
#submit   = browser.find_element_by_id("loginbutton")
#username.send_keys("YOUR EMAILID")
#password.send_keys("YOUR PASSWORD")
# Step 4) Click Login
#submit.click()
#wait = WebDriverWait( browser, 5 )
#page_title = browser.title
#assert page_title == "Facebook"