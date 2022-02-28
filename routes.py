from flask import Flask,render_template, request, redirect, jsonify
from extensions import db
from models import Link
from random import choices
import string
dict_urls = {}
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
app.config['SECRET_KEY'] = "itissecretkey"
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template("index.html")

def shorturlgenerate(original_url):        
    if(original_url not in dict_urls):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=6))        
        dict_urls[original_url] = short_url        
    else:
        return short_url
    return short_url      

@app.route('/encode', methods=['GET','POST'])
def create_link():
    if(request.method=="POST"):
        if(request.form['url'] ):
            original_url = request.form['url']  
            if(original_url not in dict_urls) :  
                short_url = shorturlgenerate(original_url)                
                link = Link(original_url=original_url, short_url=short_url)
                json=({original_url:dict_urls[original_url]})
                db.session.add(link)
                db.session.commit()
            else:
                json=({original_url:dict_urls[original_url]})
            return jsonify(json)          
    return render_template("home.html")  

@app.route('/decode', methods=['GET','POST'])
def decode():    
    if(request.method=="POST"):       
        if(request.form['url'] ):
            short_url = request.form['url']            
            for item,value in dict_urls.items():
                if(value==short_url):                    
                    original_url=item
                    json = {short_url:original_url} 
                    break  
            else:
                json = ({"message":"Please first encode URL to short url"})               
        return jsonify(json)                       
    return render_template("home.html")                

@app.route('/<short_url>')
def redirect_to_url(short_url):
    if(short_url):
        link = Link.query.filter_by(short_url=short_url).first_or_404()        
        db.session.commit()
    return redirect(link.original_url)     

@app.errorhandler(404)
def page_not_found(e):
    return ('<h1> Page Not Found 404 </h1>', 404)

if __name__=="__main__" :   
    app.run()

