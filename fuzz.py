import pandas as pd
from thefuzz import fuzz,process

df=pd.read_csv("/Users/debruppaul/Downloads/my_menu.csv")
menu=df["Food Item"]
m2=menu.to_list()
ops=["add","remove","modify","checkout","quit","try again"]

l={}

def sort_dict_by_value(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


def check(s):
    for item in m2:
        #l[f"{item}"]=
        #print(item)
        #print(s)
        #print(fuzz.ratio(s,item))
        l[f"{item}"]=max(fuzz.token_sort_ratio(s,item),fuzz.ratio(s,item))
    return list(sort_dict_by_value(l).keys())[0]

def checkops(s):
    for item in ops:
        # l[f"{item}"]=
        # print(item)
        # print(s)
        # print(fuzz.ratio(s,item))
        l[f"{item}"] = max(fuzz.token_sort_ratio(s, item), fuzz.ratio(s, item))
    return list(sort_dict_by_value(l).keys())[0]


