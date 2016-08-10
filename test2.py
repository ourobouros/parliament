
ids=[4,68,111,122,211,216,235,237,239,252,261,269,273,280,303,305,309,312,340,345,346,354,356,366,377,386,392,401,410,415,422,1296,
4778,5255,5261,5268,5270,5272,5273,5274,5279,5282,5290,5292,5296,5297,5300,5301,5307,5310,5311,5313,5317,5321,5322,5342,5376,
5379,5383,5384,5402,5406,5415,5433,5437,5444,5445,5447,5453,5456,5459,5460,5461,5462,5472,5473,5475,5476,5477,5485,5486,5487,
5490,5495,5501,5505,5506,5507,5512,5513,5516,5520,5552,5558,5766,5768,5819,5859,5866,5890,5891,5892,5893,5894,5895,5896,5897,
5898,5899,5900,5901,5902,5903,5904,5905,5906,5907,5908,5909,5910,5911,5912,5913,5914,5915,5916,5917,5918,5919,5920,5921,5922,
5923,5924,5925,5926,5927,5928,5929,5930,5931,5932,5933,5934,5935,5936,5937,5938,5939,5940,5941,5942,5943,5944,5945,5946,5947,
5948,5949,5950,5951,5952,5953,5954,5955,5956,5957,5958,5959,5960,5961,5962,5963,5964,5965,5966,5967,5968,5969,5970,5971,5972,
5973,5974,5975,5976,5977,5978,5979,5980,5981,5982,5983,5984,5985,5986,5987,5989,5990,5991,5992,5993,5999,6003,6008]

#ids=[4,68]

import os,sys,re,urllib, cPickle
from parse2 import parsePos

def downData(id):
    url = "http://www.psp.cz/sqw/detail.sqw?id=%s&t=11,1&o=6" % id
    print url
#        urllib.urlretrieve(url % i, filename="posls/%s.html" % i)
    return urllib.urlopen(url).read().decode("cp1250")
    
poss=[]
for id in ids:
    data = downData(id)
    p = parsePos(data)
    p.k=id
    poss.append(p)
    print p,p.klub, p.jmeno 

cPickle.dump(poss, open("poss.dump","w"))
