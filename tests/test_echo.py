#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo

# Your test case class goes here
class TestEcho(unittest.TestCase):
    def test_upper_short(self):
       args = ['-u', 'hello']
       output = echo.main(args)
       self.assertEqual(output,'HELLO')


    def test_lower_short(self):
        args = ['-l', 'Hello']
        output = echo.main(args)
        self.assertEqual(output, 'hello')
    

    def test_title_short(self):
        args = ['-t', 'hello']
        output = echo.main(args)
        self.assertEqual(output, 'Hello')


    def test_options(self):
        result = echo.main(['-tul', 'heLLo'])
        self.assertEquals('Hello', result)

    
    def test_text(self):
        result = echo.main(['hello'])
        self.assertEquals('hello', result)

if __name__ == '__main__':
    unittest.main()
