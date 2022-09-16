# from tkinter import Text
# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet 
# import requests
# import random 
# from rasa_sdk.executor import CollectingDispatcher

# class ActionWeather(Action): 
#     def name(self) -> Text:
#         return "action_weather"

#     def run(self, dispatcher, tracker, domain):
#         city = tracker.get_slot('location') 

#         #print (city) 
#         #api_key = "a1254cd50259c0acb586726df05c6978" 

#         #skeleton="https://home.openweathermap.org/"
#         #complete_url = skeleton + "=" + city + "&APPID=" + api_key
#         complete_url="https://home.openweathermap.org/"+city+"&APPID=a1254cd50259c0acb586726df05c6978"

#         response = requests.get (complete_url)
    
#         data = response.json()

#         x=data['main'] 
#         temp = round(x['temp'] - 273.15, 2) 
#         place = data["name"]
#         x = data['weather'] 
#         desc = x[0]['main']

#         weather_data = "It's ()*C currently in (). The weather can be described as {}".format(temp, place, desc)
#         dispatcher.utter_message (weather_data)

#         return [SlotSet ("location", city)]





# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
