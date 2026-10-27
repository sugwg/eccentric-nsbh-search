# Search for Eccentric Neutron Star–Black Hole Binaries in Advanced LIGO's Fourth Observing Run using Effective-One-Body Waveforms
Aleyna Akyüz<sup>1</sup>, Keisi Kacanja<sup>1</sup>, Rahul Dhurkunde<sup>2</sup>, Alexander H. Nitz<sup>1</sup>

<sub>1. Department of Physics, Syracuse University, Syracuse, NY 13244, USA</sub>  
<sub>2. Institute of Cosmology and Gravitation, University of Portsmouth, Portsmouth, PO1 3FX, UK</sub>

## Introduction
The observation of orbital eccentricity in compact binary coalescences would provide a direct signature of dynamical formation environments. Previous matched-filter searches for eccentric neutron star-black hole (NSBH) binaries have been severely limited by computational constraints, necessitating the use of simplified waveform models that capture secular dephasing but omit apsidal precession and inter-orbit harmonics. Including these physical features increases the sensitive search volume for systems with $0.2 \le e_{20} \le 0.28$ by $\sim 25\%$ to $30\%$. In this work, we present a rapid matched-filter search methodology that makes the direct use of time-domain effective-one-body waveforms computationally feasible across a wide parameter space. By multibanding and high-frequency ratio-filtering, our pipeline achieves a $\sim 20\times$ reduction in computational cost on high-throughput clusters. This allows a bank of 88.6 million effective-one-body templates, fifteen times larger than prior eccentric analyses, to search the first two observing epochs of the fourth observing run (O4a and O4b) of Advanced LIGO. We report the results of this search across both coincident and non-coincident observing time, totaling 401 days (comprising 238 days of coincident H1L1 data and 163 days of single-detector data). We recover the known low-mass mergers GW230518_125908 and GW230529_181500 (the latter identified during single-detector observing time) with parameters consistent with zero eccentricity. Finding no new gravitational-wave events with orbital eccentricity ($e_{20} \ge 0.05$), we place $90\%$ credible upper limits on the local merger rate density of eccentric NSBH systems across the search space of $\mathcal{R}_{90\%} \le 7.5\text{–}57\ \mathrm{Gpc}^{-3}\ \mathrm{yr}^{-1}$, up to a factor of $\sim 4$ improvement over previous observational bounds. At the parameters of GW200105_162426, this non-detection establishes an upper limit of $\mathcal{R}_{90\%} \le 12.1\ \mathrm{Gpc}^{-3}\ \mathrm{yr}^{-1}$. Alternatively, if GW200105_162426 is treated as an eccentric detection, the lack of subsequent detections in O4 updates the inferred local merger rate density of this population to $\mathcal{R} = 6.6^{+6.3}_{-3.8}\ \mathrm{Gpc}^{-3}\ \mathrm{yr}^{-1}$ ($90\%$ credible upper bound of $15.3\ \mathrm{Gpc}^{-3}\ \mathrm{yr}^{-1}$).

## Contents

| File | Description |
| --- | --- |
| `data/o4_vt.csv` | O4a and O4b sensitive volume-time [Mpc<sup>3</sup> yr] for each injection set, split by coincident (HL) and single-detector time |
| `data/ecc_dropoff.csv` | Sensitive volume-time beyond the template bank edge relative to inside it |
| `data/o3_reach.csv` | Distance reach of the previous O3 search [Mpc] |
| `data/bank_comparison.csv` | Sensitive volume-time of each template bank for one week of O4a data |
| `data/throughput.csv` | Filtering throughput of the multiband search and `pycbc_inspiral` |
| `scripts/` | Scripts to reproduce Figures 2, 3, 4 and 16 |

To make the figures (requires `numpy` and `matplotlib`):
```
cd scripts
for s in plot_*.py; do python $s; done
```

## Code
The hierarchical multiband ratio-filtering implementation is available in the `multiband` branch of [ahnitz/pycbc](https://github.com/ahnitz/pycbc).

## License and Citation

![Creative Commons License](https://i.creativecommons.org/l/by-sa/3.0/us/88x31.png "Creative Commons License")

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 United States License](http://creativecommons.org/licenses/by-sa/3.0/us/).

We encourage use of these data in derivative works. If you use the material provided here, please cite the paper.
