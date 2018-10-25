from flask import *
app = Flask(__name__)

@app.route('/')
def home_page():

    return render_template("home.html")

@app.route('/shop')
def shop():
	product=["cookies", "cake" ,"pizza"]
	return render_template("shop.html",
		products=product)

if __name__ == '__main__':
   app.run(debug = True)
