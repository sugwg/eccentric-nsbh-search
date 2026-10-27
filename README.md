# Search for Eccentric Neutron Star–Black Hole Binaries in Advanced LIGO's Fourth Observing Run using Effective-One-Body Waveforms
Aleyna Akyüz<sup>1</sup>, Keisi Kacanja<sup>1</sup>, Rahul Dhurkunde<sup>2</sup>, Alexander H. Nitz<sup>1</sup>

<sub>1. Department of Physics, Syracuse University, Syracuse, NY 13244, USA</sub>  
<sub>2. Institute of Cosmology and Gravitation, University of Portsmouth, Portsmouth, PO1 3FX, UK</sub>

## Introduction
We search the first two epochs of the fourth observing run (O4a and O4b) of Advanced LIGO for eccentric neutron star–black hole binaries using a bank of 88.6 million effective-one-body templates. Multibanding and high-frequency ratio-filtering reduce the computational cost by a factor of ~20. No new eccentric candidates are found, and we place 90% upper limits on the eccentric NSBH merger rate of 7.5–57 Gpc<sup>-3</sup> yr<sup>-1</sup>.

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
