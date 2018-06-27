#!/usr/bin/env python3
# NeoPixel library strandtest example
# Authors: Riccardo Ancona  (riccardo.ancona@gmail.com)

from unittest import TestCase
from unittest.mock import patch
 
 class MyTest(TestCase):
    @patch("neopixel")
    def test_my_code(self, mock_post):
        # ... do my thing here...

