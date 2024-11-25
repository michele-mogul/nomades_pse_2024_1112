from functools import wraps
from flask import flash, redirect, session, url_for

def authenticated(func):
  @wraps(func)
  def inner_func(*args, **kwargs):
    if not session.get('loggedin', False):
      flash("Login first", "warning")
      return redirect(url_for('login'))

    return func(*args, **kwargs)
  return inner_func