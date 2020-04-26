#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.gis.geoip2 import GeoIP2
class IPcheckMixins(object):
    def getipinfo(ipaddress):
        g = GeoIP2()
        result = g.city(ipaddress)
        return result