
from selenium import webdriver
import time
import csv
import requests
import re

def get_coordinates(url):
    wd = webdriver.Chrome('/usr/local/bin/chromedriver') 
    wd.get(url)
    wd.execute_script('''
    (function(open) {
        window.XMLHttpRequest.prototype.open = function() {
            this.addEventListener("readystatechange", function() {
                if(this.readyState == 4 && this.responseURL.indexOf('maps.php') > -1){
                    window.latlong = this.responseText
                }
            }, false);
            open.apply(this, arguments);
        };
    })(window.XMLHttpRequest.prototype.open);
    ''')

    wd.find_element_by_xpath('//a[@class="mapicn"]').click()
    try:
        latlong = str(wd.execute_async_script('var theData = arguments[0]; theData(latlong)'))
        temp = re.findall(r'\d+.\d+', latlong) 
        return list(map(float, temp)) 
    except:
        print('[ERROR]Location not specified')
        return [None, None]