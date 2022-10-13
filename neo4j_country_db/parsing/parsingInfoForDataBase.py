import requests
from lxml import html


def convertToNumber(string):
    string = string[:-2]
    ind = len(string) + 1
    for element in string:
        if element == ',':
            ind = string.index(element)
    return float(string[:ind] + string[ind + 1:])


def costOfLivingForCity(cityName):
    dictionary = {}
    params = {'displayCurrency': 'USD'}
    url = 'https://www.numbeo.com/cost-of-living/in/{}'.format(cityName)
    r = requests.get(url, params=params)
    tree = html.fromstring(r.text)
    table = '//table[@class = "data_wide_table new_bar_table"]'
    descrs = tree.xpath('{}/tr/td/text()'.format(table))
    prices = tree.xpath('{}/tr/td/span/text()'.format(table))
    for descr in descrs:
        if descr != ' ' and descr != '\n':
            dictionary[descr] = convertToNumber(prices[descrs.index(descr)])
    return dictionary
