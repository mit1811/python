import csv
import urllib2

url = 'http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1'
response = urllib2.urlopen(url)
cr = csv.reader(response)

for row in cr:
    print row