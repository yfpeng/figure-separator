"""
Usage:
    main.py [options] --output=<dir> <inputs>...

Options:
    --thresh <float>    sub-figure detection threshold. [default: 0.5]
    --model <file>      model pb file. [default: ./data/figure-separation-model-submitted-544.pb]
    --split             split the image.
    --overwrite         Overwrite.
"""
import json
from pathlib import Path
from pprint import pprint

import docopt
import tensorflow as tf
import tqdm

from figure_separator import FigureSeparator, split_figure


def main():
    args = docopt.docopt(__doc__)
    pprint(args)
    dest_dir = Path(args['--output'])

    separator = FigureSeparator(args['--model'], thresh=float(args['--thresh']))
    with tf.Session(graph=separator.graph) as sess:
        for src in tqdm.tqdm(args['<inputs>']):
            src = Path(src)
            dst = dest_dir / f'{src.stem}.json'
            if not args['--overwrite'] and dst.exists():
                continue

            subfigures, _ = separator.extract_sess(sess, src)
            with open(dst, 'w') as fp:
                json.dump(subfigures, fp)

            if args['--split']:
                split_figure(src, subfigures, dest_dir)

if __name__ == '__main__':
    main()
