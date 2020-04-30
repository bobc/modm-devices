#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, Niklas Hauser
# All rights reserved.

from ..cache import cached_property

class DriverExti:
    def __init__(self, device):
        self._device = device
        self._core = self._device.get_driver("core")

    @cached_property
    def vector_map(self):
        """
        :return: a map from int(pin number) to str(name) EXTI{name} interrupt.
        """
        extimap = {}
        for vector in [v["name"][4:] for v in self._core["vector"] if "EXTI" in v["name"]]:
            vrange = sorted(int(d) for d in vector.split("_") if d.isdigit())
            if len(vrange) == 2:
                vrange = list(range(vrange[0], vrange[1]+1))
            for num in vrange:
                if num in extimap:
                    raise ValueError("Pin '{}' already in EXTI map!".format(str(num)))
                extimap[num] = vector
        return extimap

