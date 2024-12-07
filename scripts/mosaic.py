import pandas as pd
from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from collections import Counter

inputFolder = './data'
outputFolder = './output'
data = pd.read_excel(f'{inputFolder}/data-full.xlsx')

data = data.dropna(subset=['Approach'])

props={}
props[('Parallel Transition','True')]={'facecolor':'#d6d6d6', 'edgecolor':'white'}
props[('Parallel Transition','False')]={'facecolor':'#bfbfbf', 'edgecolor':'white'}
props[('Informed Transition','True')]={'facecolor':'#a5bfcf', 'edgecolor':'white'}
props[('Informed Transition','False')]={'facecolor':'#879ba8', 'edgecolor':'white'}
props[('Twin Transition','True')]={'facecolor':'#85d4ff', 'edgecolor':'white'}
props[('Twin Transition','False')]={'facecolor':'#70b9e0', 'edgecolor':'white'}
# https://huemint.com/brand-3/#palette=70347d-d6d6d6-a5bfcf-85d4ff

labelizer=lambda k:{
    ('Parallel Transition','True'): len(data[(data['Approach']=='Parallel Transition') & (data['Mentions TT']==True)]),
    ('Parallel Transition','False'): len(data[(data['Approach']=='Parallel Transition') & (data['Mentions TT']==False)]),
    ('Informed Transition','True'): len(data[(data['Approach']=='Informed Transition') & (data['Mentions TT']==True)]),
    ('Informed Transition','False'): len(data[(data['Approach']=='Informed Transition') & (data['Mentions TT']==False)]),
    ('Twin Transition','True'): len(data[(data['Approach']=='Twin Transition') & (data['Mentions TT']==True)]),
    ('Twin Transition','False'): len(data[(data['Approach']=='Twin Transition') & (data['Mentions TT']==False)])
}[k]


plt.rcParams.update({'font.size': 22})

fig, ax = plt.subplots(figsize=(7, 3.1))
mosaic(data, ['Approach', 'Mentions TT'], properties=props, labelizer=labelizer, gap=0, ax=ax)

xlabels = ['Parallel Tr.', 'Informed Tr.', 'Twin Tr.']
ylabels = ['No TT label', 'TT-labeled']
ax.set_xticklabels(xlabels)
ax.set_yticklabels(ylabels)

ax2 = ax.twiny()
ax2.set_xticks(ax.get_xticks())
ax2.set_xticklabels([len(data[data['Approach']=='Parallel Transition']), len(data[data['Approach']=='Informed Transition']), len(data[data['Approach']=='Twin Transition'])])

ax.xaxis.set_tick_params(labelsize=16)
ax2.xaxis.set_tick_params(labelsize=18)
ax.yaxis.set_tick_params(labelsize=14)
plt.setp(ax.yaxis.get_majorticklabels(), rotation=90, ha='right', va='center')


plt.savefig('{}/rq1-mosaic.pdf'.format(outputFolder), bbox_inches='tight')