import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

kivy.require('1.11.1')  # Replace with your Kivy version

class CricketScoreTrackerApp(App):
    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation='horizontal', padding=10, spacing=10)

        # Input frame
        input_frame = GridLayout(cols=2, size_hint_x=0.3, padding=10, spacing=10)
        input_frame.add_widget(Label(text="Batting Team:"))
        self.batting_team_input = TextInput(text="Team 1")
        input_frame.add_widget(self.batting_team_input)

        input_frame.add_widget(Label(text="Bowling Team:"))
        self.bowling_team_input = TextInput(text="Team 2")
        input_frame.add_widget(self.bowling_team_input)

        input_frame.add_widget(Label(text="Overs:"))
        self.overs_input = TextInput(text="0")
        input_frame.add_widget(self.overs_input)

        main_layout.add_widget(input_frame)

        # Scorecard frames
        scorecard_frame = BoxLayout(orientation='vertical', size_hint_x=0.7, spacing=10)

        # Team 1 Score frame
        team1_score_frame = GridLayout(cols=2, size_hint_y=None, height=200)
        team1_score_frame.add_widget(Label(text="Team 1 Score:", font_size=20))
        self.team1_runs_label = Label(text="0", font_size=24)
        team1_score_frame.add_widget(self.team1_runs_label)

        team1_score_frame.add_widget(Label(text="Wickets:", font_size=18))
        self.team1_wickets_label = Label(text="0", font_size=18)
        team1_score_frame.add_widget(self.team1_wickets_label)

        team1_score_frame.add_widget(Label(text="Overs:", font_size=14))
        self.team1_overs_label = Label(text="0", font_size=14)
        team1_score_frame.add_widget(self.team1_overs_label)

        team1_score_frame.add_widget(Label(text="Balls:", font_size=14))
        self.team1_balls_label = Label(text="0", font_size=14)
        team1_score_frame.add_widget(self.team1_balls_label)

        scorecard_frame.add_widget(team1_score_frame)

        # Team 2 Score frame
        team2_score_frame = GridLayout(cols=2, size_hint_y=None, height=200)
        team2_score_frame.add_widget(Label(text="Team 2 Score:", font_size=20))
        self.team2_runs_label = Label(text="0", font_size=24)
        team2_score_frame.add_widget(self.team2_runs_label)

        team2_score_frame.add_widget(Label(text="Wickets:", font_size=18))
        self.team2_wickets_label = Label(text="0", font_size=18)
        team2_score_frame.add_widget(self.team2_wickets_label)

        team2_score_frame.add_widget(Label(text="Overs:", font_size=14))
        self.team2_overs_label = Label(text="0", font_size=14)
        team2_score_frame.add_widget(self.team2_overs_label)

        team2_score_frame.add_widget(Label(text="Balls:", font_size=14))
        self.team2_balls_label = Label(text="0", font_size=14)
        team2_score_frame.add_widget(self.team2_balls_label)

        scorecard_frame.add_widget(team2_score_frame)

        main_layout.add_widget(scorecard_frame)

        # Buttons frame
        buttons_frame = GridLayout(cols=3, size_hint_y=None, height=250, spacing=5)
        buttons_frame.add_widget(Button(text="Dot Ball", on_press=self.add_dot_ball))
        buttons_frame.add_widget(Button(text="Add Run", on_press=self.add_run))
        buttons_frame.add_widget(Button(text="Add Wicket", on_press=self.add_wicket))

        buttons_frame.add_widget(Button(text="Wide", on_press=lambda instance: self.add_extras(1)))
        buttons_frame.add_widget(Button(text="No Ball", on_press=lambda instance: self.add_extras(1)))
        buttons_frame.add_widget(Button(text="Bye", on_press=lambda instance: self.add_extras(1)))
        buttons_frame.add_widget(Button(text="Leg Bye", on_press=lambda instance: self.add_extras(1)))
        buttons_frame.add_widget(Button(text="Four", on_press=lambda instance: self.add_boundary(4)))
        buttons_frame.add_widget(Button(text="Six", on_press=lambda instance: self.add_boundary(6)))

        main_layout.add_widget(buttons_frame)

        return main_layout

    def add_run(self, instance):
        self.update_score(1, 0)
        self.update_balls()

    def add_wicket(self, instance):
        self.update_score(0, 1)
        self.update_balls()

    def add_extras(self, runs):
        self.update_score(runs, 0)

    def add_boundary(self, runs):
        self.update_score(runs, 0)
        self.update_balls()

    def add_dot_ball(self, instance):
        self.update_balls()

    def update_balls(self):
        balls = int(self.team1_balls_label.text) + 1
        if balls == 6:
            balls = 0
            overs = int(self.team1_overs_label.text) + 1
            self.team1_overs_label.text = str(overs)
        self.team1_balls_label.text = str(balls)

    def update_score(self, runs, wickets):
        # Update Team 1 score
        self.team1_runs_label.text = str(int(self.team1_runs_label.text) + runs)
        self.team1_wickets_label.text = str(int(self.team1_wickets_label.text) + wickets)

        # You'll need to add logic here to switch between batting teams
        # and update Team 2 score accordingly. This could involve a button
        # to change innings or automatically switch after a certain number of overs.

if __name__ == '__main__':
    CricketScoreTrackerApp().run()