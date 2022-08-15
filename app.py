
from flask import Flask,render_template

app = Flask(__name__)

posts=[{
    'name': 'Ray Ash',
    'title1': 'Paradises on earth',
    'content': 'In today’s time everyone want to travel abroad , they want to go to Paris, Maldives,America, London, Japan etc., to chill and have a great vacation with their loved ones, but have you ever thought of travelling in India, have you ever thought that if you travel whole India you would travel the world.',
    'date':'12 January 2022',

},
{
    'name': 'Ray Ash',
    'title1': 'Paradises on earth',
    'content': 'In today’s time everyone want to travel abroad , they want to go to Paris, Maldives,America, London, Japan etc., to chill and have a great vacation with their loved ones, but have you ever thought of travelling in India, have you ever thought that if you travel whole India you would travel the world.',
    'date':'12 January 2022',

},
{
    'name': 'Ray Ash',
    'title1': 'Paradises on earth',
    'content': 'In today’s time everyone want to travel abroad , they want to go to Paris, Maldives,America, London, Japan etc., to chill and have a great vacation with their loved ones, but have you ever thought of travelling in India, have you ever thought that if you travel whole India you would travel the world.',
    'date':'12 January 2022',

}]

@app.route("/home",methods=['GET','POST'])
def hello():
    return render_template("static/home.html",posts=posts)

if __name__ =='__main__':
    app.run(debug=True)
