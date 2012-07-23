#!/bin/sh

nosetests -s -v --with-xunit --xunit-file=nosetests.xml test_get_user_info.py
