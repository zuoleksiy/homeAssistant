from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout

import time
from time import strftime
from time import gmtime



class Alarm(FloatLayout):

	def Inputs(self):
		time_input = self.time_input.text
		day_input = self.day_input.text
		print(time_input)

		time = False
		day = False

		while time == False or day == False:
			if time_input == strftime("%H:%M"):				
				time = True
				print("Time is true")
			
				

			if day_input == strftime('%d'):
				day = True
				print("Day is true")
			
				

		print('Yesss')


class AlarmApp(App):

	def build(self):
		return Alarm()

AlarmApp().run()