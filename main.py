from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

# Sample data for Python code usage in templates
sample_mods = [
    {"name": "Create Mod", "author": "simibubi", "downloads": "50M+", "version": "1.20.1"},
    {"name": "JEI", "author": "mezz", "downloads": "100M+", "version": "1.20.1"},
    {"name": "Biomes O' Plenty", "author": "Forstride", "downloads": "75M+", "version": "1.20.1"},
    {"name": "Tinkers' Construct", "author": "mDiyo", "downloads": "80M+", "version": "1.20.1"}
]

featured_content = [
    {"title": "Epic Castle Build", "category": "builds", "rating": 4.8},
    {"title": "Faithful Texture Pack", "category": "textures", "rating": 4.9},
    {"title": "BSL Shaders", "category": "shaders", "rating": 4.7},
    {"title": "Skyblock World", "category": "worlds", "rating": 4.6}
]

def get_current_time():
    """Get current server time formatted for display"""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def get_random_featured():
    """Get random featured content for homepage"""
    return random.choice(featured_content)

@app.route('/')
def index():
    return render_template("index.html", 
                         current_time=get_current_time(),
                         featured_item=get_random_featured(),
                         total_mods=len(sample_mods))

@app.route('/mods')
def mods():
    return render_template("mods.html", 
                         current_time=get_current_time(),
                         mods_list=sample_mods,
                         total_count=len(sample_mods))

@app.route('/gallery')
def gallery():
    return render_template("gallery.html", 
                         current_time=get_current_time())

@app.route('/textures')
def textures():
    return render_template("textures.html", 
                         current_time=get_current_time())

@app.route('/worlds')
def worlds():
    return render_template("worlds.html", 
                         current_time=get_current_time())

@app.route('/shaders')
def shaders():
    return render_template("shaders.html", 
                         current_time=get_current_time())

@app.route('/modpacks')
def modpacks():
    return render_template("modpacks.html", 
                         current_time=get_current_time())

@app.route('/guides')
def guides():
    return render_template("guides.html", 
                         current_time=get_current_time())

@app.route('/upload')
def upload():
    return render_template("upload.html", 
                         current_time=get_current_time())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)