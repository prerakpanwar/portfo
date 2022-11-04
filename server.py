from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

# we can use the code from line 10 till 24 OR code from line 26 to 28

# @app.route('/index.html')
# def index():
#     return render_template('index.html')

# @app.route('/works.html')
# def work():
#     return render_template('works.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#function to write on txt file
def write_to_file(data):
    with open('database.txt','a')  as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

#function to write on csv file
def write_to_csv(data):
    with open('database.csv', newline='', mode='a')  as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        spamwriter = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([email,subject,message])
    


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect ('/thankyou.html')
        except:
            return 'Your input is not saved on the database. Please try after some time. \"If the problem persists drop a message on any of the given contact information\". Thank You.'
    else:
        return 'Something went wrong. Please try again!'

if __name__ == '__main__':
    app.run()
