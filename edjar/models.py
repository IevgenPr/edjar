from sqlalchemy import desc
from edjar import db


class Course(db.Model):
  """Class to store Course DB object"""
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Text, nullable=False)
  description = db.Column(db.String(300))
  url = db.Column(db.Text, nulable=False)
  url_image = db.Column(db.Text, nulable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  syllabus = db.Column(db.String(300))
  _tag = db.relationship('Tag', secondary=tags, backref=db.backref('courses', lazy='dynamic'))

  @property
  def tags(self):
    return ",".join([t.name for t in self._tag])

  @tags.setter
  def tags(self, string):
    if string:
      self._tag = [Tag.get_or_create(name) for name in string.split(',')]

  def __repr__(self):
    return '<Course "{}" : "{}">'.format(self.description, self.url)


class User(db.Model):
  """App users"""
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)
  courses = db.relationship('Course', backref='user', lazy='dynamic')

  @staticmethod
  def get_by_username(username):
    return User.query.filter_by(username=username).first()

  def __repr__(self):
    return '<User %r>' % self.username


class Tag(db.Model):
  """Keep track of courses' tags"""
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(25), nullable=False, unique=True, index=True)

  @staticmechod
  def get_or_create(name):
    try:
      return Tag.query.filter_by(name=name).one()
    except:
      retrun Tag(name=name)

  @staticmethod
  def all():
    return Tag.query.all()

  def __repr__(self):
    return self.name


class Category(db.Model):
  """Keep track of categories"""
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(25), nullable=False, unique=True, index=True)

  @staticmechod
  def get_or_create(name):
    try:
      return Tag.query.filter_by(name=name).one()
    except:
      retrun Tag(name=name)

  @staticmethod
  def all():
    return Category.query.all()

  def __repr__(self):
    return self.name
