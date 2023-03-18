
*******             bootstrap           *********
Go to https://getbootstrap.com/docs/4.5/getting-started/introduction/ to add bootstrap 
add css and Separate cols 

add <meta name="viewport" content="width=device-width,initial-scale=1, shrink-to-fit=no"> #new to html

add seperate parts in body beside main

now use bootstrap in base.html and anywhere else



*******             Restyling Signup Texts           *********
use crispy forms to restyle signup texts
$ pipenv install django-crispy-forms==1.9.2 /   python -m pip install django-crispy-forms            

add 'crispy_forms', # new in settings installed app section

add CRISPY_TEMPLATE_PACK = 'bootstrap4' in settings below

add {% load crispy_forms_tags %} in signup first then
use {{ form|crispy }} in place of {{ form.as_p}}

