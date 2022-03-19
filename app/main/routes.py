from flask import Blueprint,render_template,request,redirect,send_file
from app.main.utils import downloadVideo
import io
import os

main = Blueprint('main', __name__)

@main.route("/",methods=["POST","GET"])
def index():
	if request.method == "POST":
		link = request.form["link"]
		print(link)
		downloadVideo(link)

		file_path = "video.mp4"
		return_data = io.BytesIO()
		with open(file_path, 'rb') as fo:
			return_data.write(fo.read())
			
		return_data.seek(0)

		os.remove(file_path)

		return send_file(return_data, mimetype='video/mp4',
						 attachment_filename='video.mp4',as_attachment=True)
	return render_template("index.html")

