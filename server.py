from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(f'NAME IS {__name__}')
path='C:\\Users\\Stephen\\Documents\\webserver\\'


@app.route('/')
def my_home():
	return render_template('index.html')


@app.route('/<string:endpoint>')
def route_to_page(endpoint):
	return render_template(endpoint)

def write_to_file(data):
	filename = path + 'database.txt'
	with open(filename, mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'{email},{subject},{message}\n')

def write_to_csv(data):
	filename = path + 'database.csv'
	with open(filename, newline='', mode='a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'did not save to database'
	else:
		return 'something went wrong. Try again!'