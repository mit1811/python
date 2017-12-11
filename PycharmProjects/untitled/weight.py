import urllib2
import json
url='http://samples.openweathermap.org/data/2.5/weather?zip=91731,us&appid=b1b15e88fa797225412429c1c50c122a1'
data_jason=urllib2.urlopen(url)
data=json.load(data_jason)
print data
print data[u'weather']
for i in data[u'weather']:
    print dict.values(i)

