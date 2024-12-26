import unittest
from cricket_tracker import CricketScoreTrackerApp

class TestCricketScoreTrackerApp(unittest.TestCase):

    def setUp(self):
        self.app = CricketScoreTrackerApp()
        self.app.team1_runs_label = MockLabel("0")
        self.app.team1_wickets_label = MockLabel("0")
        self.app.team1_overs_label = MockLabel("0")
        self.app.team1_balls_label = MockLabel("0")
        self.app.team2_runs_label = MockLabel("0")
        self.app.team2_wickets_label = MockLabel("0")
        self.app.team2_overs_label = MockLabel("0")
        self.app.team2_balls_label = MockLabel("0")

    def test_initial_values(self):
        self.assertEqual(self.app.team1_runs_label.text, "0")
        self.assertEqual(self.app.team1_wickets_label.text, "0")
        self.assertEqual(self.app.team1_overs_label.text, "0")
        self.assertEqual(self.app.team1_balls_label.text, "0")
        self.assertEqual(self.app.team2_runs_label.text, "0")
        self.assertEqual(self.app.team2_wickets_label.text, "0")
        self.assertEqual(self.app.team2_overs_label.text, "0")
        self.assertEqual(self.app.team2_balls_label.text, "0")

    def test_add_run(self):
        self.app.add_run(None)
        self.assertEqual(self.app.team1_runs_label.text, "1")
        self.assertEqual(self.app.team1_balls_label.text, "1")

    def test_add_wicket(self):
        self.app.add_wicket(None)
        self.assertEqual(self.app.team1_wickets_label.text, "1")        

    def test_add_extras(self):
        self.app.add_extras(1)
        self.assertEqual(self.app.team1_runs_label.text, "1")
        

class MockLabel:
    def __init__(self, text):
        self.text = text

if __name__ == '__main__':
    unittest.main()