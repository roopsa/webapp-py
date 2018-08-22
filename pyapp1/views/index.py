from flask import Blueprint, render_template
#from jinja2 import TemplateNotFound

bp = Blueprint(__name__, __name__, template_folder='templates')

@bp.route('/')
def home():
#	return("Hello World")
	return render_template('index.html')  #inherit a template
	
#@simple_page.route('/<page>')
#def show(page):
#    try:
 #       return render_template('pages/%s.html' % page)
