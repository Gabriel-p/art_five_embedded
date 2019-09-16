
## Folders content

* `1.original_RAV`: Original data files sent by Rubén.
* `2.UBV_move`: Processed original files to feed the `UBV-move` code, and
  the output.
* `3.Gaia_data`: Files retrieved via the `GaiaQuery` package.
* `4.2MASS_data`: Cross-match of the above files with the 2MASS survey.
* `5.final_input`: Gaia DR2 cross-matched files with 2MASS, with 2MASS colors
  and their uncertainties added via the `add_cols.py` script.
* `6.ASteCA`: Analysis by `ASteCA` of 2MASS and Gaia DR2 photometry, to obtain
  parallax and proper motions estimates.


## Analysis of five embedded clusters with ASteCA.

The clusters were originally presented in the article [Dutra et al. (2003)](https://ui.adsabs.harvard.edu/abs/2003A%26A...400..533D/abstract):

> "*We carried out a 2MASS J, H and Ks survey of infrared star clusters in the Milky Way sector 230deg< l < 350deg. This zone was the least studied in the literature, previously including only 12 infrared clusters or stellar groups with |b|< 10deg, according to the recent catalogue by Bica et al. (2003). We concentrated efforts on embedded clusters, which are those expected in the areas of known radio and optical nebulae. The present study provides 179 new infrared clusters and stellar groups, which are interesting targets for detailed future infrared studies. The sample of catalogued infrared clusters and stellar groups in the Galaxy is now increased by 63%.*"

The Vizier tables are [here](https://ui.adsabs.harvard.edu/abs/2003yCat..34000533D/abstract). The five analyzed clusters are:

```
Name             RA_2000      DEC_2000
[DBS2003]5       07:30:04.0   -18:32:06.0 (112.5167, -18.535)
[DBS2003]60      11:05:36.6   -62:28:54.5 (166.4025, -62.4818)
[DBS2003]98      15:59:38.0   -53:45:24.0 (239.9083, -53.7567)
[DBS2003]116     17:09:34.0   -41:36:0.00 (257.3917, -41.6)
[DBS2003]117     16:59:39.0   -40:11:24.0 (254.9125, -40.19)
```

Note that the coordinates for 116 are different from those originally given by Rubén (`17:09:32.2   -41:33:23.8)`.

### Aladin views

DSS colored view of each cluster (via [Aladin](https://aladin.u-strasbg.fr)):

**[DBS5](http://aladin.unistra.fr/AladinLite/?target=07%2030%204.000-18%2032%206.00&fov=0.42&survey=P%2FDSS2%2Fcolor)**

![](figs/dbs5.png)

**[DBS60](http://aladin.unistra.fr/AladinLite/?target=11%2005%2036.600-62%2028%2054.50&fov=0.42&survey=P%2FDSS2%2Fcolor)**

![](figs/dbs60.png)

**[DBS98](http://aladin.unistra.fr/AladinLite/?target=15%2059%2038.000-53%2045%2024.00&fov=0.42&survey=P%2FDSS2%2Fcolor)**

![](figs/dbs98.png)

**[DBS116](http://aladin.unistra.fr/AladinLite/?target=17%2009%2034.000-41%2036%200.00&fov=0.42&survey=P%2FDSS2%2Fcolor)**

![](figs/dbs116.png)

**[DBS117](http://aladin.unistra.fr/AladinLite/?target=16%2059%2039.000-40%2011%2024.00&fov=0.42&survey=P%2FDSS2%2Fcolor)**

![](figs/dbs117.png)


### 2MASS photometry

This analysis uses 2MASS data only. These files contain about half as many stars as the Gaia DR2 data files.

For DBS5, 60, 98, the structural overdensities are clearly distinguishable over the foreground/background (field) noise. For DBS177 a more weak but still noticeable overdensity is appreciated. No clear structural overdensity can be seen for DBS116. For these two clusters (116, 117) the radius is fixed to 1 arcmin, while the remaining values are estimated by `ASteCA`.

The maximum uncertainty cuts are done at `eJ_{max}=0.1` mag, `eHKs_{max}=0.2` mag. We use somewhat large maximum values to avoid losing too many stars.

The comparison with the surrounding field density shows that the number of members within each defined cluster region is:

```
Name    N_memb
--------------
DBS5    ~27
DBS60   ~12
DBS98   ~0
DBS116  ~0
DBS117  ~8
```


#### Parallax distances

The parallax analysis was performed after cleaning the cluster region from field stars. Due to the low number of probable members in all regions, the distance estimates obtained with the Bayesian method and the parallax data should be taken with care. An offset of +0.029 mas was added to the parallax values, as suggested by [Lindegren et al. (2018)](https://www.aanda.org/articles/aa/abs/2018/08/aa32727-18/aa32727-18.html).

The final distance estimates (and their 16th, 84th percentiles) are:

```
Name    d_Plx (16th, 84th)
--------------------------
DBS5    4020 (3573, 4476) [pc]
DBS60   5585 (5055, 6110) [pc]
DBS98   2666 (2443, 2888) [pc]
DBS116 10633 (9631, 11641) [pc]
DBS117  1848 (1522, 2182) [pc]
```

#### Proper motions

The estimated proper motion for the cluster regions, obtained through the maximum value of the 2D KDE are:

```
Name    pmRA     pmDEC
-----------------------
DBS5    -1.751    2.404 [mas/yr]
DBS60   -2.357    1.681 [mas/yr]
DBS98   -1.719   -3.666 [mas/yr]
DBS116  -1.493   -4.322 [mas/yr]
DBS117  -0.121   -0.829 [mas/yr]
```


### Gaia DR2 photometry

The maximum uncertainty cuts are done at `eG_{max}=0.01` mag,
`eBPRP_{max}=0.2` mag.

The comparison with the surrounding field density shows that the number of members within each defined cluster region is:

```
Name    N_memb
--------------
DBS5    ~75
DBS60   ~22
DBS98   ~21
DBS116  ~0
DBS117  ~9
```


#### Parallax distances

As above, the parallax analysis was performed **without cleaning the cluster region from field stars** and using the +0.029 mas offset. The resulting values are:

```
Name    d_Plx (16th, 84th)
--------------------------
DBS5    4091 (3724, 4466) [pc]
DBS60   5668 (5162, 6187) [pc]
DBS98   3090 (2823, 3361) [pc]
DBS116  9275 (8267, 10272) [pc]
DBS117  1639 (1393, 1874) [pc]
```

#### Proper motions

Same treatment as in the 2MASS analysis. Results are:


```
Name    pmRA     pmDEC
-----------------------
DBS5    -1.696    2.098 [mas/yr]
DBS60   -2.363    1.697 [mas/yr]
DBS98   -0.983   -2.921 [mas/yr]
DBS116  -1.562   -4.352 [mas/yr]
DBS117  -0.324   -1.096 [mas/yr]
```

