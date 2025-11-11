A simple interactive command-line Study Tracker built in Python.
This project was created to help track study progress across different subjects, understand confidence levels, and reflect on mood and motivation. It supports multiple users in a single session and summarizes each user’s study patterns.

Features included are:

Add Study Entry
	•	Add a subject
	•	Add a topic studied under that subject
	•	Record confidence level (1 = no confidence, 2 = somewhat, 3 = full confidence)
	•	Entries stored in memory during program runtime

Multi-User Support
	•	Each user has their own study history
	•	Switch users anytime within the same session

Summary View
	•	Display all subjects studied
	•	Topics covered under each subject
	•	Average confidence level per subject
	•	Weakest subject (lowest average confidence)
	•	Strongest subject (highest average confidence)

Mood Reflector
User chooses their current mood:
	•	Tired
	•	Stressed
	•	Unmotivated
	•	Focused
	•	Happy
The program gives a simple, friendly study tip or advice based on selected mood.


Why I Built This Project:
I wanted to create a useful tool that helps me study more effectively.

How to Run
	1.	Download the mini_study_tracker.py file.
	2.	Open a terminal.
	3.	Run: python mini_study_tracker.py

  Future Improvements
	•	Add persistent storage using JSON files
	•	Add time tracking (duration of study)
	•	Add a graphical interface
	•	Add charts/visualizations
	•	Export progress summary to a file
