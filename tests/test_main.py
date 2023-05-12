import os
import sys
import tempfile
from contextlib import redirect_stdin
from unittest import TestCase
from aider.main import main

class TestMain(TestCase):
    def test_main_with_dev_null(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            os.chdir(temp_dir)
    with open(os.devnull, 'r') as dev_null:
        with redirect_stdin(dev_null):
                    main()