from flask import render_template

from . import main
from ..models import User, Course, Tag, Category

@main.route('/')
@main.route('/index')
def index():
  return render_template(
    'index.html',
    title="Fine Courses"
    user=''
    text=['one', 'two', 'three']
    new_courses=Courses()
  )

@main.app_errorhandler(403)
def page_not_found(e):
  return render_template('403.html'), 403

@main.app_errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@main.app_errorhandler(500):
def server_error(e):
  return render_template("500.html"), 500

@main.app_context_processor
def injectr_tags():
  return dict(all_tags=Tag.all)

