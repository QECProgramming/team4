from flask import Flask, request, redirect
from papaJohns import papaJohns
from skipthedishes import SkipTheDishes

import os
app = Flask(__name__, static_url_path='')

@app.route("/", methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        body = request.form.to_dict(flat=False)

        Johns = papaJohns("507 Princess St. Kingston Ontario", "K7L 1C6", body["pizzaSize"][0], body["pizzaToppings"][0], 1)

        return app.send({
            "Papa John's Pizza": Johns.findCost(),
            "Skip The Dishes Rec": SkipTheDishes.find(body["pizzaSize"][0], 1, body["pizzaToppings"][0])
        })
    else:
        return app.send_static_file('./webpage.html')

@app.route("/result")
def result():
    return app.send_static_file('./results.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
