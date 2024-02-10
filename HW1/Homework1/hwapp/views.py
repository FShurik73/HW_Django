from django.http import HttpResponse
import logging

# Create your views here.


logger = logging.getLogger(__name__)


html1 =""" <!doctype html>
           <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport"
                    content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                    <title>Главная страница!</title>
                </head>
                <body>
	                <h1>
		                Это главная страница сайта
	                </h1>
	                <p>lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus  molestiae repudiandae consequuntur velit fugit deserunt recusandae officiis voluptatibus mollitia. </p>	
                </body>
           </html>"""

html2 = """ <!doctype html>
           <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport"
                    content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                    <title>О нас</title>
                </head>
                <body>
	                <h1>
		                О себе
		            </h1>
                    <p>lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus  molestiae repudiandae consequuntur velit fugit deserunt recusandae officiis voluptatibus mollitia. Tenetur  repudiandae  molestiae  repudiandae consequuntur velit fugit deserunt recusandae officiis voluptatibus mollitia.     </p>		
                </body>
           </html>"""


def custom_log(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        logger.info(f'Была вызвана функция {func.__name__}')
        return res
    return wrapper


@custom_log
def index(request):
    return HttpResponse(html1)


@custom_log
def about(request):
    return HttpResponse(html2)


