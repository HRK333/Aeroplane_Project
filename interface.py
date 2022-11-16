from flask import Flask, render_template, request
from Project_app.utilis import AeroplaneTicket

app =Flask(__name__)

@app.route("/")
def hello_flask():
    print("We are in Home API")
    return render_template("index.html")

@app.route("/predict_price", methods=["POST"])
def get_price():
    Airline = request.form.get("Airline")
    Source= request.form.get("Source")
    Destination= request.form.get("Destination")
    Duration = request.form.get("Duration")
    Total_Stops = request.form.get("Total_Stops")
    
    obj = AeroplaneTicket(Airline,Source,Destination,Duration,Total_Stops)
    result = obj.get_ticket_price()
    return render_template("index.html", prediction = result)

@app.route("/contact_us", methods = ["POST"])
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=5002, debug = True)