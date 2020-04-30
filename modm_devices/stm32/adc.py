#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, Niklas Hauser
# All rights reserved.

class DriverAdc:
    def __init__(self, device):
        self._device = device
        self._adc = self._device.get_driver("adc")

    def instances(self, default=None):
        """
        :return: a map from int(pin number) to str(name) EXTI{name} interrupt.
        """
        if "instance" in self._adc:
            return list(map(int, self._adc["instance"]))
        return default

