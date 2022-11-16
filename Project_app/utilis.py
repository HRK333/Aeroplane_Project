import json
import pandas as pd
import numpy as np
import pickle
import config
import warnings
warnings.filterwarnings("ignore")

class AeroplaneTicket():
    def __init__(self,Airline,Source,Destination,Duration,Total_Stops):
        self.Airline = Airline
        self.Source = Source
        self.Destination = Destination
        self.Duration = Duration  
        self.Total_stops = Total_Stops
        
    def load_model(self):
        
        with open(config.JSON_PATH, "r") as f:
            self.data= json.load(f)
            
        with open(config.MODEL_PATH, "rb") as f:
            self.model = pickle.load(f) 
            

    def get_ticket_price(self):
        self.load_model()

        array= np.zeros(len(self.data["columns"]))

        array[0] = self.data["Airline"][self.Airline]
        array[1] = self.data["Source"][self.Source]
        array[2] = self.data["Destination"][self.Destination]
        array[3] = self.Duration
        array[4] = self.data["Total_Stops"][self.Total_stops]

        

        result= self.model.predict([array])[0]
        return result

if __name__ == "__main__":
    Airline= "IndiGo"
    Source= "Kolkata"
    Destination= "Banglore"
    Duration = 420
    Total_Stops = "2 stops"

    obj = AeroplaneTicket(Airline,Source,Destination,Duration,Total_Stops)
    result = obj.get_ticket_price()

    print("The aeroplane ticket will be Rs.:", result)                