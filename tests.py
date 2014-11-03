# -*- coding: utf-8 -*-
import nbp
from datetime import date
from nose.tools import assert_equals



def test_downloads_exchange_rate_properly():
    expexted = {
        'search_date': '2010-07-11',
        'table_no': u'132/A/NBP/2010',
        'pub_date': u'2010-07-09',
        'url': 'http://rss.nbp.pl/kursy/xml2/2010/a/10a132.xml',
        'currency': {
            'name': u'euro',
            'rate': 4.0732999999999997,
            'code': u'EUR',
            },
        }
    currency_data = nbp.download_exchange_rate(nbp.date(2010, 7, 11), 'EUR')
    assert_equals(expexted, currency_data)

def test_downloads_exchange_rate_properly_even_with_broken_nbp_404_200():
    expexted = {
        'search_date': '2014-11-03',
        'table_no': u'213/A/NBP/2014',
        'pub_date': u'2014-11-03',
        'url': 'http://rss.nbp.pl/kursy/xml2/2014/a/14a213.xml',
        'currency': {
            'name': u'euro',
            'rate': 4.2209,
            'code': u'EUR',
            },
        }
    currency_data = nbp.download_exchange_rate(date.today(), 'EUR')
    assert_equals(date.today().strftime('%Y-%m-%d'), currency_data['pub_date'])
