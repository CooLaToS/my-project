#!/usr/bin/env python3
'''
 Script Name: test_app.py
 Description: Tests for app.py.
 Author: Nektarios
 Date: {DD/MM/YY} (automatically fill this in)
 Version: 1.0

 This script tests the add_numbers function from app.py.
'''

from app import add_numbers

def test_add_numbers():
    assert add_numbers(3, 4) == 7
    assert add_numbers(-1, 1) == 0
    assert add_numbers(-2, -2) == -4

