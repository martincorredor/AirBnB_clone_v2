#!/usr/bin/python3
"""Unittest for console"""
import cmd
import os
import pep8
import unittest
import models
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import json

run = os.system


class TestHBNBCommand(unittest.TestCase):
    """
    testing all commands
    """
    def test_docstring(self):
        """docstring"""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0)

    def test_aa_create(self):
        """ create tests """
        no_stdout = " > /dev/null 2>&1"
        run("rm file.json " + no_stdout)
        run("echo 'create State' | ./console.py" + no_stdout)
        run("echo 'all' | ./console.py" + no_stdout)
        with open("file.json", 'r') as f:
            temp = json.load(f)
        self.assertTrue(temp)

    def test_ab_create(self):
        """ create tests """
        no_stdout = " > /dev/null 2>&1"
        run("rm file.json " + no_stdout)
        run('echo create State name="California" | ./console.py' + no_stdout)
        run("echo 'all' | ./console.py" + no_stdout)
        with open("file.json", 'r') as f:
            temp = json.load(f)
        self.assertTrue(temp)

    def test_ac_create(self):
        """ create tests """
        no_stdout = " > /dev/null 2>&1"
        run("rm file.json " + no_stdout)
        command = 'echo create City state_id="1" name="San_Francisco" '
        command = command + '| ./console.py '
        run(command + no_stdout)
        run("echo 'all' | ./console.py" + no_stdout)
        with open("file.json", 'r') as f:
            temp = json.load(f)
        self.assertTrue(temp)
