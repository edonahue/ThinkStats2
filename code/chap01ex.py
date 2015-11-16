import thinkstats2
import numpy as np
import pandas as pd

import nsfg

def ReadFemResp(dct_file='2002FemResp.dct',
		dat_file='2002FemResp.dat.gz'):
     dct = thinkstats2.ReadStataDct(dct_file)
     df = dct.ReadFixedWidth(dat_file, compression='gzip')
     return df

resp = ReadFemResp()
# print resp.shape

print resp.pregnum.value_counts().sort_index()
print 'Total: ' + str(sum(resp.pregnum))

preg = nsfg.ReadFemPreg()
preg_resps = {}
for c in preg.caseid:
    preg_resps[c] = preg_resps.get(c, 0) + 1
print 'Preg data pregnancies: '+ str(sum(preg_resps.values()))
