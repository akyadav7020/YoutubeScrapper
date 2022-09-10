from get_video_link_from_home import get_id_of_videos
from pro import youtubescraper
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import database
import requests

app = Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")

@app.route('/review',methods=['POST'])
@cross_origin()
def main():
    if request.method == 'POST':
        ch_link = request.form['content'] #"https://www.youtube.com/user/zeemusiccompany/videos"
        video_id = get_id_of_videos(ch_link)
        details = []#[{"num":1,"V_link":'a',"Title":'b',"thumbnail":'c'},{"num":2,"V_link":'d',"Title":'e',"thumbnail":'f'}]
        #database.table()
        for i in range(5):
            video_link,title, thumbnail_url = youtubescraper(video_id[i])
            mydict = {"num":i+1,"V_link":video_link,"Title":title,"thumbnail":thumbnail_url}
            details.append(mydict)
            database.save_data(mydict)

    return render_template('results.html',details=details[0:(len(details))],n =len(details))

if __name__ == "__main__":
    app.run(debug=True)






