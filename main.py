from flask import Flask, render_template, request
#from tables import db, VEHICLETBL

app = Flask(__name__)
#app.config.from_object('config.ProdConfig')
#db.init_app(app)


@app.route('/')
def index():
    return 'Hello Second World'


#@app.route('/vehicles')
#def vehicles():
#    vehicles = VEHICLETBL.query.all()
#    return render_template('vehicles.html', vehicles=vehicles)


@app.route('/shopping')
def shopping():
    shopping_list = ['Bread', 'Eggs', 'Flour', 'Milk']
    return render_template('shopping.html', shopping_list=shopping_list)


@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)


@app.route('/post/<int:post_id>')
def post(post_id):
    return "<h1>Post Id is %s<h1>" % post_id


if __name__ == '__main__':
  app.run()
