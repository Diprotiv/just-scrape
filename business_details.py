import requests
from bs4 import BeautifulSoup
import csv
from location import get_coordinates

class business:
    def __init__(self,data,city,query, writer):
        self.business_data = data
        self.city = city
        self.query = query.replace(' ','_')

        self.soup = BeautifulSoup(self.business_data.text, 'lxml')
        self.address = self.get_business_adrs()
        self.business_name = self.get_business_name()
        
        self.web_url = data.url
        self.table_name = city+'_'+self.query
        self.location = get_coordinates(self.web_url)
        write_to_csv(writer, self)

    def get_business_adrs(self):
        # soup = BeautifulSoup(self.business_data.text, 'lxml')
        detail = self.soup.findAll('span', class_='adrstxtr')
        for d in detail:
            data = str(d.text).replace('(Map)','').replace('\n',' ')
            # print(data)
            return data

    def get_business_name(self):
        detail = self.soup.findAll('span', class_='fn')
        for d in detail:
            data = str(d.text)

            return (data)


def write_to_csv(writer, self):
    row = {}
    row['Name'] = self.business_name
    row['Address'] = self.address
    row['URL'] = self.web_url
    row['Latitude'] = self.location[0] or 0.0
    row['Longitude'] = self.location[1] or 0.0
    print(row)
    writer.writerow(row)    