@app.route('/')
def nothing():
    return redirect(url_for('index'))


@app.route('/blog')
def blog():
    return render_template('blog.html', title="Blog")


@app.route('/index', methods=['GET', 'POST'])
def index():
    form = WelcomeScreenForm()
    if form.validate_on_submit():
        return redirect(url_for('create'))

    return render_template('index.html', title='Start', form=form)