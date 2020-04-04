# -*- coding: utf-8 -*-
# !/usr/bin/env python

'''
author:satoshi tsutsui
a simple version with one file.
'''

# from box import BoundBox, box_iou, prob_compare
# from box import prob_compare2, box_intersection
import argparse
import math

import cv2
# sys.path.insert(0, './')
import numpy as np
import tensorflow as tf



# here is my simple implementation
if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--img", type=str, help=u"input image", required=True)
    parser.add_argument("--out", default="predicted.png", type=str, help=u"output image file path")
    parser.add_argument("--model", default="./data/figure-separation-model-submitted-544.pb", type=str,
                        help=u"model pb file")
    parser.add_argument("--thresh", default=0.5, type=float, help=u"detection threshold")
    args = parser.parse_args()
    graph = load_graph(args.model)

    # for op in graph.get_operations():
    #     print(op.name)

    imgcv, imgcv_resized, img_input = preprocess(args.img)

    with tf.Session(graph=graph) as sess:
        detections = sess.run('output:0', feed_dict={'input:0': img_input})

    meta = {'object_scale': 5, 'classes': 1, 'out_size': [17, 17, 30], 'colors': [(0, 0, 254)], 'thresh': args.thresh,
            'anchors': [1.08, 1.19, 3.42, 4.41, 6.63, 11.38, 9.42, 5.11, 16.62, 10.52], 'num': 5, 'labels': ['figure']}

    outboxes, detected = postprocess(meta, detections, imgcv)
    cv2.imwrite(args.out, detected)

    print("Detected %d figures" % len(outboxes))
    print("Saved to %s" % args.out)
