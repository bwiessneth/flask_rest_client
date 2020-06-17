import json
import requests
from app import app
from flask import render_template, redirect, url_for, request, flash

api_url = 'https://bewi.uber.space/flask_rest_api/api/v0/'
api_user_endpoint = 'user'

# Index endpoint
@app.route("/")
def index():
	message = "Hello from flask_rest_client"
	return render_template('index.html', message=message)


@app.route("/user")
@app.route("/user/<user_id>")
def user(user_id=None):
	if user_id:
		r = requests.get(url=api_url + api_user_endpoint + '/' + user_id)
		if r.status_code == 200:
			d = json.loads(r.text)			
			return render_template('user_view.html', user=d)
	else:
		r = requests.get(url=api_url + api_user_endpoint)
		if r.status_code == 200:
			d = json.loads(r.text)
			return render_template('users.html', users=d)


@app.route("/user/create", methods=['GET', 'POST'])
def user_create():
	if request.method == 'POST':
		headers = {'Content-type': 'application/json'}
		j = json.dumps(request.form)
		r = requests.post(url=api_url + api_user_endpoint, data=j, headers=headers)
		return redirect(url_for('user'))
	else:
		r = requests.get(url=api_url + api_user_endpoint + '/' + '1')
		d = json.loads(r.text)
		print(d)
		return render_template('user_create.html', user=d)


@app.route("/user/update/<user_id>", methods=['GET', 'POST'])
def user_update(user_id):
	if request.method == 'POST':
		headers = {'Content-type': 'application/json'}
		j = json.dumps(request.form)
		r = requests.patch(url=api_url + api_user_endpoint + '/' + user_id, data=j, headers=headers)
		return redirect(url_for('user'))
	else:
		r = requests.get(url=api_url + api_user_endpoint + '/' + user_id)
		user = json.loads(r.text)
		return render_template('user_update.html', user=user)

@app.route("/user/delete/<user_id>")
def user_delete(user_id):
	r = requests.delete(url=api_url + api_user_endpoint + '/' + user_id)
	return redirect(url_for('user'))
