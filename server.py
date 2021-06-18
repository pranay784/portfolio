from flask import Flask, render_template  , request , redirect
import csv

app = Flask(__name__)

@app.route('/')
def about():
	return render_template('index.html')



@app.route('/<string:page_name>')
def my_home(page_name):
	return render_template(page_name)

def write_csv(data):
	with open('database1.csv', mode ='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer= csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data= request.form.to_dict()
		write_csv(data)
		write_database(data)
		return redirect('/tankyou.html')
	else:
		return 'oops'

def write_database(data):
	with open('database.txt', mode ='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email},{subject},{message}')

