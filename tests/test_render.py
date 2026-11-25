import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from render import render

class ReportTest(unittest.TestCase):
    def test_unobserved_sections_are_explicit(self):
        result = render(Path(__file__).resolve().parents[1] / 'examples' / 'issue.json')
        self.assertIn('Editorial draft', result)
        self.assertIn('Awaiting observation', result)
