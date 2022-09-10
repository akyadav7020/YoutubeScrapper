import get_video_link_from_home as vd
from pro import youtubescraper
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import database
import requests

app = Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def homepage():
    try:
        return render_template("index.html")
    except:
        return "Try Again"

@app.route('/review',methods=['POST'])
@cross_origin()
def main():
    try:
        if request.method == 'POST':
            ch_link = request.form['content']
            count = int(request.form['num'])
            video_id = vd.get_id_of_videos(ch_link,count)
            if (len(video_id)) == 0:
                return "Invalid Link Try again"
            details = []
            table_name = vd.title_of_channel(ch_link)
            database.create_unique_table(table_name)
            for i in range(len(video_id)):
                video_link,title, thumbnail_url = youtubescraper(video_id[i])
                views = vd.Total_Views(video_id[i])
                total_likes = vd.Total_Likes((video_id[i]))
                mydict = {"V_link":video_link,"Likes":total_likes,"Title":title,"thumbnail":thumbnail_url,"Views":views}
                details.append(mydict)
                database.insert_unique_data("video_link",table_name,mydict)
        return render_template('results.html',details=details[0:(len(details))],n =len(details))

    except Exception as e:
        return "Try Again"

if __name__ == "__main__":
    app.run(debug=True)






