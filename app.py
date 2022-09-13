import video_details as vd
import extract
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

@app.route('/extract',methods=['POST'])
@cross_origin()
def main():
    try:
        if request.method == 'POST':
            ch_link = request.form['content']
            count = int(request.form['num'])
            details = []
            ch_name="Abhay"
            video_id = vd.get_id_of_videos(ch_link,count)
            data1=[{"V_link":video_id,"Likes":100,"Title":"title1","thumbnail":"thumbnail_url1","Views":500}]
            """if (len(video_id)) == 0:
                return "Invalid Link Try again"
            data1 = []
            ch_name,ch_url = vd.title_of_channel(ch_link)
            table_name = vd.remove_special_char(ch_name)+"_{}".format(vd.remove_special_char(ch_url))
            database.create_unique_table(table_name)
            for i in range(count):
                video_link,title, thumbnail_url = extract.youtubescraper(video_id[i])
                views = vd.Total_Views(video_id[i])
                total_likes = vd.Total_Likes((video_id[i]))
                mydict = {"V_link":video_link,"Likes":total_likes,"Title":title,"thumbnail":thumbnail_url,"Views":views}
                data1.append(mydict)
                database.insert_unique_data("video_link",table_name,mydict)"""
            details.append(data1)
            data2 = database.Extract_data()
            details.append(data2)

        return render_template('results.html',details=details[0:len(details)],n =len(data1),count=len(data2),name=ch_name)

    except Exception as e:
        return e


if __name__ == "__main__":
    #app.run()
    app.run(port=8000, host='0.0.0.0')







