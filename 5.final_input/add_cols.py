
import numpy as np
from astropy.io import ascii
from astropy.table import MaskedColumn
import os

"""
Add colors and their uncertainties to 2MASS data.
"""

for f in os.listdir('.'):
    if f.endswith('_match.dat') and not f.endswith('no_match.dat'):
        print(f)
        inp_data = ascii.read(f)

        jhcol = inp_data['Jmag'] - inp_data['Hmag']
        eJH = np.sqrt(inp_data['e_Jmag']**2 + inp_data['e_Hmag']**2)
        jkcol = inp_data['Jmag'] - inp_data['Kmag']
        eJK = np.sqrt(inp_data['e_Jmag']**2 + inp_data['e_Kmag']**2)
        hkcol = inp_data['Hmag'] - inp_data['Kmag']
        eHK = np.sqrt(inp_data['e_Hmag']**2 + inp_data['e_Kmag']**2)

        inp_data.add_column(MaskedColumn(jhcol, name='JH'))
        inp_data.add_column(MaskedColumn(eJH, name='eJH'))
        inp_data.add_column(MaskedColumn(jkcol, name='JK'))
        inp_data.add_column(MaskedColumn(eJK, name='eJK'))
        inp_data.add_column(MaskedColumn(hkcol, name='HK'))
        inp_data.add_column(MaskedColumn(eHK, name='eHK'))

        ascii.write(inp_data, output=f[:-10] + '.dat', overwrite=True)
