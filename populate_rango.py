import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TwD.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    ### Python
    python_cat = add_cat('Python', 128, 64)

    add_page(cat=python_cat,
             title="Official Python Tutorial",
             uri="http://docs.python.org/2/tutorial/")
    add_page(cat=python_cat,
             title="How to Think like a Computer Scientist",
             uri="http://www.greenteapress.com/thinkpython/")
    add_page(cat=python_cat,
             title="Learn Python in 10 Minutes",
             uri="http://www.korokithakis.net/tutorials/python/")

    ### Django
    django_cat = add_cat('Django', 64, 32)

    add_page(cat=django_cat,
             title="Official Django Tutorial",
             uri="http://docs.djangoproject.com/en/1.5/intro/tutorial01/")
    add_page(cat=django_cat,
             title="Django Rocks",
             uri="http://www.djangorocks.com/")
    add_page(cat=django_cat,
             title="How to Tango with Django",
             uri="http://www.tangowithdjango.com/")

    ### Other Frameworks
    frame_cat = add_cat('Other Frameworks', 32, 16)

    add_page(cat=frame_cat,
             title="Bottle",
             uri="http://bottlepy.org/docs/dev/")
    add_page(cat=frame_cat,
             title="Flask",
             uri="http://flask.pocoo.org")

    ### Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))



def add_page(cat, title, uri, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.uri = uri
    p.views = views
    p.save()
    return p


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()