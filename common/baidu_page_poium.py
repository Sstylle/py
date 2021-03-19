# coding:utf-8

from poium import Page, Element


class BaiduPage(Page):
    search_input = Element(id_='kw')
    search_button = Element(id_='su')
