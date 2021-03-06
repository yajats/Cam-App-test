from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet

app = Flask(__name__, template_folder='template')

app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_IMAGES_DEST'] = 'C:/Users/yajat/Untitled Folder/pics'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

# #
class MyForm(FlaskForm):
    image = FileField('image')
#
#



# print(form.image)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()

    if form.validate_on_submit():
        print(form.image)
        #filename = images.save(form.image.data)
        #return f'Filename: {filename}'

    return render_template('index.html', form=form)





if __name__ == '__main__':
     app.run()