# -*- coding: utf-8 -*-

from learn_confluence import api


def test():
    _ = api


if __name__ == "__main__":
    from learn_confluence.tests import run_cov_test

    run_cov_test(__file__, "learn_confluence.api", preview=False)
