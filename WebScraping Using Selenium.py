
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import getpass
from selenium.common import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome

path = '/Users/chromedriver'
driver = webdriver.Chrome(path)
driver.get("https://rma.realpage.com/explore/main")
sleep(10)

driver.find_element_by_xpath('//div[@class="sign-in"]/span').click()
username= driver.find_element_by_xpath('//input[@name="username"]')
username.send_keys('user')   
password= driver.find_element_by_xpath('//input[@id="inputPassword"]')
password.send_keys('password')
driver.implicitly_wait(100)
driver.find_element_by_xpath('//button[@type="submit"]').click()   
driver.implicitly_wait(100)

df= pd.DataFrame(columns=['Resia Property','Comps','Units','Type','Effective Rent','Effective RPSF',"Asking Rent"])
URL = [
"https://rma.realpage.com/explore/main/p/mila-i-ii/171531",
"https://rma.realpage.com/explore/main/p/the-olivia/175467",
"https://rma.realpage.com/explore/main/p/south-pointe/166934",
"https://rma.realpage.com/explore/main/p/the-heights-at-coral-town-park/157843",
"https://rma.realpage.com/explore/main/p/sophia-square/173088",
"https://rma.realpage.com/explore/main/p/parc-place/35767",
"https://rma.realpage.com/explore/main/p/park-towers/27384",
"https://rma.realpage.com/explore/main/p/cottonwood-west-palm-apartments/166938",
"https://rma.realpage.com/explore/main/p/alora-west-palm-beach/246582",
"https://rma.realpage.com/explore/main/p/avonlea-tributary/121730",
"https://rma.realpage.com/explore/main/p/riverside-parc/102435",
"https://rma.realpage.com/explore/main/p/the-park-at-riverview/27078",
"https://rma.realpage.com/explore/main/p/the-atlantic-river-west/40377",
"https://rma.realpage.com/explore/main/p/bexley-at-left-bank/190936",
"https://rma.realpage.com/explore/main/p/historic-electric-building/18599",
"https://rma.realpage.com/explore/main/p/the-depot/39623",
"https://rma.realpage.com/explore/main/p/the-braden-on-fifth/162070",
"https://rma.realpage.com/explore/main/p/madera-at-leftbank/152851",
"https://rma.realpage.com/explore/main/p/parkside-so-7-i/200818",
"https://rma.realpage.com/explore/main/p/the-abbey-at-northpoint-apartments/150639",
"https://rma.realpage.com/explore/main/p/the-mill/240688",
"https://rma.realpage.com/explore/main/p/the-pierpont/172333",
"https://rma.realpage.com/explore/main/p/the-abbey-at-northpoint-apartments/150639",
"https://rma.realpage.com/explore/main/p/the-mill/240688",
"https://rma.realpage.com/explore/main/p/the-pierpont/172333",
"https://rma.realpage.com/explore/main/p/crest-at-illinois/247627",
"https://rma.realpage.com/explore/main/p/mariposa-villas/36505",
"https://rma.realpage.com/explore/main/p/vistas-at-pinnacle-park/37064",
"https://rma.realpage.com/explore/main/p/cortland-inkwell-greenhouse/237364",
"https://rma.realpage.com/explore/main/p/greenhouse/158310",
"https://rma.realpage.com/explore/main/p/radius-west/239425",
"https://rma.realpage.com/explore/main/p/vollterra-at-westlake/125711",
"https://rma.realpage.com/explore/main/p/territory-at-greenhouse/239549",
"https://rma.realpage.com/explore/main/p/north-creek/250425",
"https://rma.realpage.com/explore/main/p/the-fairways-at-star-ranch/46824",
"https://rma.realpage.com/explore/main/p/alys-crossing/246601",
"https://rma.realpage.com/explore/main/p/cantera-at-towne-lake/102431",
"https://rma.realpage.com/explore/main/p/carrington-at-barker-cypress/44229",
"https://rma.realpage.com/explore/main/p/commons-at-hollyhock/195233",
"https://rma.realpage.com/explore/main/p/queenston-manor-apartments/123601",
"https://rma.realpage.com/explore/main/p/cue/185333",
"https://rma.realpage.com/explore/main/p/the-mill/240688",
"https://rma.realpage.com/explore/main/p/cue/185333",
"https://rma.realpage.com/explore/main/p/greenhouse-villas/46783",
"https://rma.realpage.com/explore/main/p/emory-west-cypress/262947",
"https://rma.realpage.com/explore/main/p/carrington-at-barker-cypress/44229",
"https://rma.realpage.com/explore/main/p/icon-avondale/9166",
"https://rma.realpage.com/explore/main/p/alora-west-palm-beach/246582",
"https://rma.realpage.com/explore/main/p/seasons-704/12021",
"https://rma.realpage.com/explore/main/p/tennis-towers/21323",
"https://rma.realpage.com/explore/main/p/centre-at-peachtree-corner/11181",
"https://rma.realpage.com/explore/main/p/cortland-peachtree-corners/173027",
"https://rma.realpage.com/explore/main/p/vue-on-medlock/21862",
"https://rma.realpage.com/explore/main/p/the-brunswick/237784",
"https://rma.realpage.com/explore/main/p/the-carson-at-peachtree-corners/20731",
"https://rma.realpage.com/explore/main/p/the-village-at-rayzor-ranch-i/191090",
"https://rma.realpage.com/explore/main/p/abbey-at-barker-cypress/39361",
"https://rma.realpage.com/explore/main/p/cortland-vizcaya/39360",
"https://rma.realpage.com/explore/main/p/the-place-at-barker-cypress-i/13486",
"https://rma.realpage.com/explore/main/p/the-place-at-barker-cypress/21456",
"https://rma.realpage.com/explore/main/p/cortland-inkwell-greenhouse/237364",
"https://rma.realpage.com/explore/main/p/greenhouse/158310",
"https://rma.realpage.com/explore/main/p/mirabella/111413",
"https://rma.realpage.com/explore/main/p/old-cutler-village/36167",
"https://rma.realpage.com/explore/main/p/the-braden-on-fifth/162070",
"https://rma.realpage.com/explore/main/p/madera-at-leftbank/152851",
"https://rma.realpage.com/explore/main/p/bexley-at-left-bank/190936",
"https://rma.realpage.com/explore/main/p/historic-electric-building/18599",
"https://rma.realpage.com/explore/main/p/parkside-so-7-i/200818",
"https://rma.realpage.com/explore/main/p/1300-north-post-oak/151935",
"https://rma.realpage.com/explore/main/p/north-post-oak-lofts/100162",
"https://rma.realpage.com/explore/main/p/viridian-design-district/153247",
"https://rma.realpage.com/explore/main/p/cortland-presidio-east/158111",
"https://rma.realpage.com/explore/main/p/monterra-village-i/42280",
"https://rma.realpage.com/explore/main/p/alleia-at-presidio/239342",
"https://rma.realpage.com/explore/main/p/longhorn-crossing/137142",
"https://rma.realpage.com/explore/main/p/ascent-lake-worth/18710",
"https://rma.realpage.com/explore/main/p/maa-mcdaniel-farm/20113",
"https://rma.realpage.com/explore/main/p/maa-pleasant-hill/14504",
"https://rma.realpage.com/explore/main/p/the-rey-on-reynolds/193734",
"https://rma.realpage.com/explore/main/p/sugarloaf-walk/187311",
"https://rma.realpage.com/explore/main/p/cordoba-doral-i/102584",
"https://rma.realpage.com/explore/main/p/green-park/157803",
"https://rma.realpage.com/explore/main/p/atlas-lavista-hills/102439",
"https://rma.realpage.com/explore/main/p/avana-city-north/40605",
"https://rma.realpage.com/explore/main/p/gold-creek/264745",
"https://rma.realpage.com/explore/main/p/westpoint-at-scenic-vista/46759",
"https://rma.realpage.com/explore/main/p/constellation-ranch/40065",
"https://rma.realpage.com/explore/main/p/aliro/11587",
"https://rma.realpage.com/explore/main/p/grand-island-square/32356",
"https://rma.realpage.com/explore/main/p/the-shoreline-sole-mia/192960",
"https://rma.realpage.com/explore/main/p/lazul/171254",
"https://rma.realpage.com/explore/main/p/aliro/11587",
"https://rma.realpage.com/explore/main/p/grand-island-square/32356",
"https://rma.realpage.com/explore/main/p/the-shoreline-sole-mia/192960",
"https://rma.realpage.com/explore/main/p/lazul/171254",
"https://rma.realpage.com/explore/main/p/aliro/11587",
"https://rma.realpage.com/explore/main/p/grand-island-square/32356",
"https://rma.realpage.com/explore/main/p/the-shoreline-sole-mia/192960",
"https://rma.realpage.com/explore/main/p/lazul/171254",
"https://rma.realpage.com/explore/main/p/cortland-south-kendall/236531",
"https://rma.realpage.com/explore/main/p/palmetto-station/187215",
"https://rma.realpage.com/explore/main/p/bay-village1/233706"
]
for url in URL:

    driver.get(url)
    driver.implicitly_wait(10)

    property_name = driver.find_element_by_xpath('//property-name-renderer[@class="ng-star-inserted"]/a').text
    onebr_units = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="104"]').text
    onebr_sqft = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="643"]').text
    onebr_occupancy = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="644"]').text
    onebr_effectiverent = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="645"]').text
    onebr_effectiverpfs = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="646"]').text
    onebr_askingrent = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="687"]').text
    
    twobr_units = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="114"]').text
    twobr_sqft = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="648"]').text
    twobr_occupancy = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="649"]').text
    twobr_effectiverent = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="650"]').text
    twobr_effectiverpfs = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="651"]').text
    twobr_askingrent = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="689"]').text

    threebr_units = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="124"]').text
    threebr_sqft = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="653"]').text
    threebr_occupancy = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="654"]').text
    threebr_effectiverent = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="655"]').text
    threebr_effectiverpfs = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="656"]').text
    threebr_askingrent = driver.find_element_by_xpath('//div[@role="gridcell"][@comp-id="691"]').text
    
    
    if property_name.find("Mila") != -1:
        resia_property = "Resia Oak Enclave (SFL)"
    elif property_name.find("Olivia") != -1 or property_name.find("South Point") != -1 or property_name.find("Sophia Square") != -1 or property_name.find("Coral Park") != -1 :
        resia_property = "AHS Biscayne Drive (SFL)"
    elif (property_name.find("Cottonwood West Palm") != -1 or property_name.find("Alora West Palm") != -1 ):
        resia_property = "AHS Pine Ridge (Southern & Jog) (SFL)"
    elif (property_name.find("Parc Place") != -1 or property_name.find("Park Towers") != -1):
        resia_property = "AHS Golden Glades (SFL)"    
    elif (property_name.find("Avonlea Tributary") != -1 or property_name.find("Panther Riverside Parc") != -1 or property_name.find("The Park at Riverview") != -1 or property_name.find("The Atlantic River West") != -1  ):
        resia_property = "AHS Tributary (ATL)"    
    elif (property_name.find("Bexley") != -1 or property_name.find("The Depot") != -1 or property_name.find("The Braden") != -1  or property_name.find("Madera at Leftbank") != -1):
        resia_property = "Calhoun St (DFW)"
    elif (property_name.find("The Abbey at North") != -1 or property_name.find("The Mill") != -1 or property_name.find("The Pierpont") != -1 ):
        resia_property = "Cathedral Lakes - North (HOU)"
    elif (property_name.find("Alta Cathedral Lakes") != -1 or property_name.find("The Abbey at Northpoint") != -1):
        resia_property = "Cathedral Lakes - South (HOU)"
    elif (property_name.find("Crest at Illinois") != -1 or property_name.find("Mariposa Villas") != -1 or property_name.find("Vista at Pinnacle Park") != -1):
        resia_property = "Dallas National - Resia Dallas West (DFW)"
    elif (property_name.find("Cortland Inkwell") != -1 or property_name.find("Greenhouse") != -1 or property_name.find("Radius West") != -1 or property_name.find("Volterra at Westlake") != -1 or property_name.find("Territory at Greenhouse") != -1   ):
        resia_property = "Forresta Village (HOU)"
    elif (property_name.find("North Creek") != -1 or property_name.find("The Fairways at Star Ranch") != -1):
        resia_property = "Hutto Square (AUS)"
    elif (property_name.find("Alys Crossing") != -1 or property_name.find("Cantera at Towne Lake") != -1 or property_name.find("Carrington at Barker Cypress") != -1 or property_name.find("Commons at Hollyhock") != -1 or property_name.find("Queenstone Manor Apartments") != -1  or property_name.find("Cue") != -1):
        resia_property = "Jazzy Cove Lane (HOU)"
    elif (property_name.find("Greenhouse Villas") != -1 or property_name.find("Emory West Cypress") != -1 or property_name.find("Carrington at Barker") != -1):
        resia_property = "Marvida (HOU)"
    elif (property_name.find("Icon Avondale") != -1):
        resia_property = "Memorial Drive - Kensington Station (ATL)"
    elif (property_name.find("Seasons 704") != -1 or property_name.find("Tennis Towers") != -1):
        resia_property = "Okeechobee-Town of Palm Beach (SFL)"    
    elif (property_name.find("Centre at Peachtree Corner") != -1 or property_name.find("Cortland Peachtree Corner") != -1 or property_name.find("Vue on Medlock") != -1 or property_name.find("The Brunswick") != -1  or property_name.find("The Carson at Peachtree") != -1 ):
        resia_property = "Peachtree Corners (ATL)"    
    elif (property_name.find("Village at Rayzor Ranch ") != -1):
        resia_property = "Rayzor Ranch (DFW)"    
    elif (property_name.find("Abbey at Barker Cypress") != -1 or property_name.find("Cortland Vizcaya") != -1 or property_name.find("The Place at Barker Cypress") != -1 or property_name.find("Cortland Inkwell Greenhouse") != -1  or property_name.find("Greenhouse") != -1):
        resia_property = "Ten Oaks (HOU)"
    elif (property_name.find("Mirabella") != -1 ):
        resia_property = "Village at Old Cutler (SFL)"
    elif (property_name.find("Braden on Fifth") != -1 or property_name.find("Madera at Leftbank") != -1 or property_name.find("Bexley at Left Bank") != -1 or property_name.find("Historic Electric Building") != -1 or property_name.find("Parkside So") != -1   ):
        resia_property = "Weatherford (DFW)"    
    elif (property_name.find("1300 North Post Oak") != -1 or property_name.find("North Post Oak Lofts") != -1 or property_name.find("Viridian Design District") != -1):
        resia_property = "West Loop (HOU)" 
    elif (property_name.find("Cortland Presidio") != -1 or property_name.find("Monterra Village") != -1 or property_name.find("Alleia at Presidio") != -1):
        resia_property = "North City Fort Worth (DFW)" 
    elif (property_name.find("Longhorn Crossing") != -1 or property_name.find("Ascent Lake Worth") != -1 ):
        resia_property = "Marine Creek (DFW)" 
    elif (property_name.find("MAA McDaniel Farm") != -1 or property_name.find("MAA Pleasant Hill") != -1 or property_name.find("The Rey on Reynolds") != -1 or property_name.find("Sugarloaf Walk") != -1  ):
        resia_property = "Orchid Grove - Phase 1 (ATL)" 
    elif (property_name.find("Green Park") != -1 or property_name.find("Atlas Lavista Hills") != -1 or property_name.find("Avana City North") != -1):
        resia_property = "Tucker Exchange (ATL)" 
    elif (property_name.find("Gold Creek") != -1 or property_name.find("Westpoint at Scenic Vista") != -1 or property_name.find("Constellation Ranch") != -1):
        resia_property = "Alemeda (DFW)"
    elif (property_name.find("Aliro") != -1 or property_name.find("Grand Island Square") != -1 or property_name.find("The Shoreline Sole Mia") != -1 or property_name.find("Lazul") != -1  ):
        resia_property = "New North Town Center (SFL)" 
    elif (property_name.find("Cortland South Kendal") != -1 or property_name.find("Palmetto Station") != -1 or property_name.find("Bay Billage One") != -1):
        resia_property = "Coral Reef (SFL)"
    elif (property_name.find("Siena Round Rock Apartments") != -1 or property_name.find("Park at Siena") != -1):
        resia_property = "Hutto Square (AUS)"
    elif (property_name.find("Cordoba") != -1):
        resia_property = "Palmetto Station (SFL)"
    elif (property_name.find("Siena Round Rock Apartments") != -1 or property_name.find("Park at Siena") != -1):
        resia_property = "Hutto Square (AUS)"            
    elif (property_name.find("Fieldhouse") != -1 or property_name.find("Century at the Ballpark") != -1 or property_name.find("The Heights at Exchange") != -1 or property_name.find("Overlook at Gwinnett Stadium") != -1 or property_name.find("Enzo at Ariston") != -1 or property_name.find("Ivy at Ariston") != -1):
        resia_property = "Tulip Grove (ATL)"
   
    df1 = pd.DataFrame({"Resia Property":[resia_property,resia_property,resia_property],"Comps":[property_name,property_name,property_name],"Units":[onebr_units,twobr_units,threebr_units],'Type':['1BR','2BR','3BR'],"Occupancy":[onebr_occupancy,twobr_occupancy,threebr_occupancy],"Area":[onebr_sqft,twobr_sqft,threebr_sqft],"Effective Rent":[onebr_effectiverent,twobr_effectiverent,threebr_effectiverent],"Effective RPSF":[onebr_effectiverpfs,twobr_effectiverpfs,threebr_effectiverpfs],"Asking Rent":[onebr_askingrent,twobr_askingrent,threebr_askingrent]},index=[0,1,2])
    df = df.append(df1,ignore_index=0)
    print (df)
    driver.quit()

df.to_csv("realpage_property.csv",index=0)
