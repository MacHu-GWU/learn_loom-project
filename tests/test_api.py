# -*- coding: utf-8 -*-

from learn_loom import api


def test():
    _ = api


if __name__ == "__main__":
    from learn_loom.tests import run_cov_test

    run_cov_test(__file__, "learn_loom.api", preview=False)
