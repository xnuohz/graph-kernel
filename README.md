# Graph Kernel

A Degeneracy Framework for Graph Similarity

## Envs

* python >= 3.5
* GraKel
* sklearn

## Usage

```bash
python bio.py
python social.py
```

## Dataset

### Bioinformatics and Chemoinformatics Dataset

| Dataset | MUTAG | ENZYMES | NCI1 | PTC-MR | DD |
| :-: | :-: | :-: | :-: | :-: | :-: |
| #Graphs | 188 | 600 | 4110 | 344 | 1178 |
| #Classes | 2 | 6 | 2 | 2 | 2 |
| Avg. #Nodes | 17.93 | 32.63 | 29.87 | 14.29 | 284.32 |
| Avg. #Edges | 19.79 | 62.14 | 32.30 | 14.69 | 715.66 |
| Node Labels | + | + | + | + | + |
| Edge Labels | + | - | - | + | - |
| Node Attr.(Dim.) | - | +(18) | - | - | - |
| Edge Attr.(Dim.) | - | - | - | - | - |

### Social Networks Dataset

| Dataset | IMDB-BINARY | IMDB-MULTI | REDDIT-BINARY | REDDIT-MULTI-5K | REDDIT-MULTI-12K |
| :-: | :-: | :-: | :-: | :-: | :-: |
| #Graphs | 1000 | 1500 | 2000 | 4999 | 11929 |
| #Classes | 2 | 3 | 2 | 5 | 11 |
| Avg. #Nodes | 19.77 | 13.00 | 429.63 | 508.52 | 391.41 |
| Avg. #Edges | 96.53 | 65.94 | 497.75 | 594.87 | 456.89 |
| Node Labels | - | - | - | - | - |
| Edge Labels | - | - | - | - | - |
| Node Attr.(Dim.) | - | - | - | - | - |
| Edge Attr.(Dim.) | - | - | - | - | - |

## Accuracy

### Bioinformatics and Chemoinformatics

* PTC-MR is currently unsupported.

| Method | MUTAG | ENZYMES | NCI1 | PTC-MR | DD |
| :-: | :-: | :-: | :-: | :-: | :-: |
| GR      | 83(0.12) | 20(0.06) | 62(0.02) | / |  |
| CORE GR | 79(0.11) | 20(0.04) | 62(0.03) | / |  |
| SP      | 81(0.11) | 37(0.05) | 67(0.02) | / |  |
| CORE SP | 81(0.11) | 37(0.06) | 67(0.03) | / |  |
| WL      | 78(0.12) | 32(0.04) | 81(0.02) | / |  |
| CORE WL | 81(0.10) | 33(0.04) | 81(0.02) | / |  |
| PM      | 85(0.10) | 34(0.05) | 70(0.03) | / |  |
| CORE PM | 86(0.11) | 36(0.06) | 73(0.02) | / |  |

### Social Networks

| Method | IMDB-BINARY | IMDB-MULTI | REDDIT-BINARY | REDDIT-MULTI-5K | REDDIT-MULTI-12K |
| :-: | :-: | :-: | :-: | :-: | :-: |
| GR      |  |  |  |  |  |
| CORE GR |  |  |  |  |  |
| SP      |  |  |  |  |  |
| CORE SP |  |  |  |  |  |
| WL      |  |  |  |  |  |
| CORE WL |  |  |  |  |  |
| PM      |  |  |  |  |  |
| CORE PM |  |  |  |  |  |

## Time

### Bioinformatics and Chemoinformatics

* PTC-MR is currently unsupported.

| Method | MUTAG | ENZYMES | NCI1 | PTC-MR | DD |
| :-: | :-: | :-: | :-: | :-: | :-: |
| GR      | 18.46(0.62) |  60.71(1.46) |  397.39(12.99) | / |  |
| CORE GR | 56.31(1.53) | 247.89(6.69) | 1225.32(33.67) | / |  |
| SP      |  0.40(0.01) |   4.94(0.06) |    24.97(0.12) | / |  |
| CORE SP |  1.29(0.06) |  21.57(0.33) |    74.30(0.71) | / |  |
| WL      |  0.09(0.02) |   0.83(0.17) |     9.48(0.17) | / |  |
| CORE WL |  0.33(0.07) |   3.76(0.78) |    25.06(0.74) | / |  |
| PM      |  0.96(0.05) |   8.03(0.44) |  379.52(33.21) | / |  |
| CORE PM |  2.85(0.15) |  32.03(2.20) | 1124.29(96.92) | / |  |

### Social Networks

| Method | IMDB-BINARY | IMDB-MULTI | REDDIT-BINARY | REDDIT-MULTI-5K | REDDIT-MULTI-12K |
| :-: | :-: | :-: | :-: | :-: | :-: |
| GR      |  |  |  |  |  |
| CORE GR |  |  |  |  |  |
| SP      |  |  |  |  |  |
| CORE SP |  |  |  |  |  |
| WL      |  |  |  |  |  |
| CORE WL |  |  |  |  |  |
| PM      |  |  |  |  |  |
| CORE PM |  |  |  |  |  |

## Reference

* [Paper](https://www.ijcai.org/proceedings/2018/0360.pdf)
* [Datasets](https://ls11-www.cs.tu-dortmund.de/staff/morris/graphkerneldatasets)
* [GraKel](https://ysig.github.io/GraKeL/dev/index.html)