from wtforms.ext.sqlalchemy.orm import model_form
from wtforms.widgets import PasswordInput
from ..models.users import User

fieldargs = {'password': {
                'widget': PasswordInput()
                }}
UserForm = model_form(User, field_args=fieldargs)
