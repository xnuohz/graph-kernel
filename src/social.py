#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn import svm
from grakel import datasets
from grakel import GraphKernel


kernels = {
    "Shortest Path": [{"name": "shortest_path", "with_labels": False}],

    "Graphlet Sampling": [{"name": "graphlet_sampling",
                           "sampling": {"n_samples": 500}}],

    "Weisfeiler-Lehman/Subtree": [{"name": "weisfeiler_lehman", "niter": 5},
                                  {"name": "subtree_wl"}],

    "Pyramid match": [{"name": "pyramid_match", "d": 6, "L": 4, "with_labels": False}],

    "Core Shortest Path": [{"name": "core_framework"},
                           {"name": "shortest_path", "with_labels": False}],

    "Core Graphlet Sampling": [{"name": "core_framework"},
                               {"name": "graphlet_sampling", "sampling": {"n_samples": 500}}],

    "Core Weisfeiler-Lehman/Subtree": [{"name": "core_framework"},
                                       {"name": "weisfeiler_lehman", "niter": 5},
                                       {"name": "subtree_wl"}],

    "Core Pyramid match": [{"name": "core_framework"},
                           {"name": "pyramid_match", "d": 6, "L": 4, "with_labels": False}]
}

Datasets = ["IMDB-BINARY", "IMDB-MULTI", "REDDIT-BINARY", "REDDIT-MULTI-5K", "REDDIT-MULTI-12K"]
Methods = sorted(list(kernels.keys()))

for j, d in enumerate(Datasets):
    print(d)
    dataset_d = datasets.fetch_dataset(d, verbose=False, data_home="../dataset", produce_labels_nodes=True)
    G, y = np.asarray(dataset_d.data), np.asarray(dataset_d.target)

    stats = {m: {"acc": list(), "time": list()} for m in Methods}

    kfold = KFold(n_splits=10, random_state=50, shuffle=True)

    for train_idx, test_idx in kfold.split(G, y):
        train_g, train_y = G[train_idx], y[train_idx]
        test_g, test_y = G[test_idx], y[test_idx]

        for i, k in enumerate(Methods):
            gk = GraphKernel(kernel=kernels[k], normalize=True)

            start = time.time()
            k_train = gk.fit_transform(train_g)
            k_test = gk.transform(test_g)
            end = time.time()

            clf = svm.SVC(kernel='precomputed')
            clf.fit(k_train, train_y)

            pred_y = clf.predict(k_test)

            stats[k]["acc"].append(accuracy_score(test_y, pred_y))
            stats[k]["time"].append(end - start)

    for m in Methods:
        print("kernel: ", m,
              "time: ", np.round(np.mean(stats[m]["time"]), 2), "~", np.round(np.std(stats[m]["time"]), 2),
              "acc: ", np.round(np.mean(stats[m]["acc"]), 2), "~", np.round(np.std(stats[m]["acc"]), 2))
