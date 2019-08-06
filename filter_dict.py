import sys
import os

class filter_dict:

    dict2={ 1:1, 2:"True", 3:"False", 4:3, 5:'I', 6:"True"}

    filter_dict=dict(filter(lambda x : (("True" in x) or ("False" in x)),dict2.items()))
    print(filter_dict)

    for i in filter_dict.keys():
        print(i)



