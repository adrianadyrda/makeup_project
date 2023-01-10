import requests
import json                                       # to do general imports
from pprint import pprint
from read_input_file import read_input
from write_result import write_item_to_file       # to do from general import something separate
from parsing import scrap_item_from_makeup


all_urls_to_pars = read_input()                    # enter new variable: 'all_urls_to_pars' and keep function read_input

                                                   # in function 'read_input' I saved the list with 10 url


my_list = []                                       # create new  empty list
for url in all_urls_to_pars:                       # in the cycle, for every url from the variable 'all_urls_to_pars'
    my_product = scrap_item_from_makeup(url)       # I create new variable 'my_product', where I saved the main function and like argument 'url', cuz  i need to apply this func for every url
    my_list.append(my_product)                     # In  my empty list I append my product


write_item_to_file(my_list)                        # I have function which write the result, and i just cause this function and in argument my list that I filled out.
