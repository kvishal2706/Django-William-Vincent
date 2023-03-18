
*******          password change              *********
use {url 'password_change' } to change password by default functionality of django

**********      Customizing Password Change         *******

create password_change_form.html in templates/registrations
create password_change_done.html in templates/registrations

do with the same name and django will automatically do all the work by using these templates

**********     Password RESET     *******

add the above mentioned line in settings.py fro django console backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


CUSTOM

create password_reset_form.html
templates/registration/password_reset_done.html
templates/registration/password_reset_confirm.html
templates/registration/password_reset_complete.html
