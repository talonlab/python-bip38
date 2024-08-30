#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

import pytest

from bip38.exceptions import Error


def test_exception():
    class TestError(Error):
        pass

    with pytest.raises(TestError, match="Error"):
        raise TestError(message="Error")

    with pytest.raises(TestError, match="more_detail"):
        raise TestError(message="Error", detail="more_detail")

    with pytest.raises(TestError, match="value_expect"):
        raise TestError(message="Error", expected="value_expect")

    with pytest.raises(TestError, match="value_got"):
        raise TestError(message="Error", expected="value_expect", got="value_got")