# Compound Figure Separator

## Acknowledgement

This repository was forked from [https://github.com/apple2373/figure-separator](https://github.com/apple2373/figure-separator)
If you find this tool useful, please cite the original paper:

```
@inproceedings{tsutsui2017data,
  title={A data driven approach for compound figure separation using convolutional neural networks},
  author={Tsutsui, Satoshi and Crandall, David J},
  booktitle={2017 14th IAPR International Conference on Document Analysis and Recognition (ICDAR)},
  volume={1},
  pages={533--540},
  year={2017},
  organization={IEEE}
}
```

## Getting started

### Install requirements

```sh
$ pip install -r requirements.txt
```

### Download the pre-trained model

The model can be found at

- Google Drive: [https://drive.google.com/open?id=0B046sNk0DhCDems2am5YV3NLeDQ](https://drive.google.com/open?id=0B046sNk0DhCDems2am5YV3NLeDQ)  
- Dropbox: [https://www.dropbox.com/s/xug7uw1rrq7ljy0/figure-sepration-model-submitted-544.pb?dl=0](https://www.dropbox.com/s/xug7uw1rrq7ljy0/figure-sepration-model-submitted-544.pb?dl=0)
- GitHub: []()

### Separate compound figures
```sh
$ python split_figure.py --split --output ./results imgs/* 
```
See the `results` directory. Output json is something like:
```json
[
 {
 "x": (x coordinate of left top point of the sub-figure),
 "y": (y coordinate of left top point of the sub-figure),
 "w": (width of the sub-figure),
 "h": (height of the sub-figure),
 "conf": (confidence value of the extaction),
 } ,....
] 
```

Here is other options:
```
$ python split_figure.py --help                                       
Usage:
    main.py [options] --output=<dir> <inputs>...

Options:
    --thresh <float>    sub-figure detection threshold. [default: 0.5]
    --model <file>      model pb file. [default: ./data/figure-separation-model-submitted-544.pb]
    --split             split the image.
    --overwrite         Overwrite.
```

## Use the codes inside the project

```python
from figure_separator import FigureSeparator
fig_separator=FigureSeparator(MODEL)
sub_figures=fig_separator.extract(IMAGE)
print(sub_figures)
```

