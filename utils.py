#!/usr/bin/env python

import pandas as pd 
import os 
import numpy as np

import seaborn as sns
import matplotib.pyplot as plt 

import GEOparse as geo 

#basic methylation gse puller
#expects ID_REF and VALUE columns, but wont work on all GSEs
#requires more information to accurately split into control/case
def gse_df(gse):
    gse = geo.get_GEO(geo=gse,destdir=path)
    out = [x.table.set_index("ID_REF").VALUE for key,x in gse.gsms.items()]
    out = pd.DataFrame(out)
    out.index = list(gse.gsms.keys())
    return(out)

def gse_meta(gse):
    pass

def to_genes(gse):
    #load ensembl ids and probe mapping csvs
    #use those to collapse to mean across features
    pass
