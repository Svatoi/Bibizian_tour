from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user

auth_bp = Blueprint("auth", __name__)