from flask import Flask, request, render_template, current_app
import functions
from dotenv import load_dotenv
load_dotenv()

#MQ: 8336
#NS: 9533

def get_data(input_value):
    data = getattr(current_app, input_value, None)
    if data is None:
        data, faction = functions.get_faction(input_value)
        setattr(current_app, input_value, data)
    faction = 'test'
    return data, faction

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_value = request.form['input_value']
        input_value2 = request.form['input_value2']
        input_value3 = request.form['input_value3']
        input_value4 = request.form['input_value4']
        input_value5 = request.form['input_value5']
        print(input_value, input_value2, input_value3, input_value4, input_value5)


        #data, faction = get_data(input_value)
        data, faction = functions.get_faction(input_value)

        return render_template("index.html", data=data, faction=faction)
    return render_template("frontpage.html")

if "__name__" == "__main__":
    app.run(debug=True)

