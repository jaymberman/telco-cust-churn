TEMPDIR = tempfile.mkdtemp()
PATH = os.path.join(TEMPDIR, 'delme.csv')

x = 4
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/single_result', methods=['POST'])
def stuff():
    usr_input = [str(x) for x in request.form.values()]
    return render_template('home.html', 
                            text=f'Result: {usr_input[0]}')

@app.route('/page1')
def page1():
	return "You're on page 1!"


def _do_data_science(df):
    df += 10
    return df

@app.route('/success', methods=['POST'])
def fileupload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "file not in request.files"
        file = request.files['file']
        df = pd.read_csv(file, header=None)
        df = _do_data_science(df)
        df.to_csv(PATH)
        return render_template('file.html')
    else:
        return "not a POST request"

@app.route('/download')
def download():
    @after_this_request
    def remove_file(response):
        os.remove(PATH)
        return response

    return send_file(PATH, as_attachment=True)