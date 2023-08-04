## [Python Django Tutorial for Beginners](https://www.youtube.com/watch?v=rHux0gMZ3Eg)

- **Front-end** (**Client**): is what is loaded inside a browser and what user sees.
- **Back-end** (**Server**): runs on a server and responsible for data processing, validation etc.
- **URL**: Uniform Resource Locator; a way to locate resource on the internet.

- When a user hits a websites, the browser sends a `Request` to the (web) `server`. The server processes the request and sends back a `Response` to the `Client`.

- The data exchange/communication between `Client` and `Server` is defined by **HTTP**.

- To create the back-end, one has to decide how one is going to response to the client. There are two ways:

1. Server generates the Response and return it to the Client. In this case, one generates an `HTML` file and return it to the client.
2. Only generate the data requested on the Server and return it. In this case, the Client will have to generate the HTML page. This is more scalable, meaning more users can be served at once using this approach.

- If one pushed the responsibility to generate the page on the Client, then Server becomes the Gateway for the data. In this scenario, one can provide different endpoint for user to talk to. These endpoints are called `API` (Application Programming Interface).

## [Django For Everybody - Full Python University Course](https://www.youtube.com/watch?v=o0XbHvKxw7Y) and [Django Documentation](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)

### Introduction to Dynamic Web Content

- The web browser waits for an event to happen, say clicking on the a link on the webpage. That click is intercepted by the browser application which opens a network socket across the network to the web server and sends a request. The web server does what it is supposed to do and then sends back a response on the same socket. This is `request-response cycle`.

### Network Sockets

- URL consists of three things: protocol (like http, https, ftp), host (google, data.pr4r.org etc) and the document name (page1.html).

- **HTTP** (HyperText Tranfer Protocol):

  - Invented for Web - to retrieve HTML, Images, DOcuments, etc
  - Entended to handle data in addition to documents - RSS, Web services, etc.
  - Basic Concept: Make a connection - Request a document, Retrieve the document - Close the connection.

- **Socket** is like a phone call where two computer software talk to each other. Internet is the medium through which the conversation takes place.

### Flow of a Web Request

- When the request arrives at a Django app the incoming request URL is compared to the list of paths in `url.py` in the variable `urlpatterns`.
- When there is a url match, it selects a `View` which is a bit of code that handles any database access and then produces and delivers the response to the browser.
- The `view` access the databse indirectly through an abstraction called a `model`.
- This is a general web pattern called **Model-View-Controller** or **MVC**.

### What goes in the background (in Django)

<img title="Workflow of the Web Application" src="workflow.png">

- User clicks on something in `DOM` (Document Object Model) i.e. in the browser. The browser intercept the click and creates a socket connection across the internet and does a `GET` request. This request goes into the (web) server.
- The three main modules are `routing` , `view`, and `models`. There is `setting.py` file that is like a config file that has information like, this is the view file, models file etc.
- When the request first comes in, it consults `url.py` (for each project or application) and pulls out the `view.py`.
- `view.py` has the destination for the incoming url. We can also use files like `forms.py` and `Templates`.
- In case some data needs to be stored, we use `models.py` to store the data in the database.
- Once that is done, we read the new data from the database and combine that with the template and send a response which the user ultimately sees.

#### To set up the basic infrastructure

```shell
mkdir django_projects
cd .\django_projects\
# this is to create a project
django-admin startproject mysite
```

- The following to allow all host.

```python
# make the following changes in the setting.py file in the mysite folder
ALLOWED_HOSTS = ["*"]
```

- The following to run the server.

```shell
python .\mysite\manage.py runserver
```

#### Create an application

- Note: make sure you’re in the same directory as `manage.py`

```shell
cd .\mysite\
python .\manage.py startapp polls
```

- Now, open `view.py` file in `polls` folder and add the following:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, you are the poll index.")
```

- To call the view, we need to map it to a URL - and for this we need a URLconf. To create a URLconf in the `polls` directory, create a file called `url.py`. In the `polls/urls.py` file include the following code:

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

- The next step is to point the root URLconf at the `polls.urls` module. Add the following in `mysite/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),
]
```

- The `include()` function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing. You should always use include() when you include other URL patterns. admin.site.urls is the only exception to this.

- You have now wired an index view into the URLconf. Verify it’s working with the following command:

```shell
# to check for errors
python .\manage.py check
python .\manage.py runserver
```

- This is display 404 on http://127.0.0.1:8000/. However, add `polls` at the end to see the changes we made so far. http://127.0.0.1:8000/polls

- The `path()` function is passed four arguments, two required: `route` and `view`, and two optional: `kwargs`, and `name`. At this point, it’s worth reviewing what these arguments are for.
  - `route` is a string that contains a URL pattern. When processing a request, Django starts at the first pattern in `urlpatterns` and makes its way down the list, comparing the requested URL against each pattern until it finds one that matches.
  - `view`: When Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first argument and any “captured” values from the route as keyword arguments.
  - `kwargs`: Arbitrary keyword arguments can be passed in a dictionary to the target view.
  - `name`: Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.

### Database setup

- By default, the configuration uses SQLite. If you wish to use another database, install the appropriate [database bindings](https://docs.djangoproject.com/en/4.0/topics/install/#database-installation`) and change the following keys in the `DATABASES 'default'` item to match your database connection settings:

  - `ENGINE` – `'django.db.backends.sqlite3'` etc.
  - `NAME` – The name of your database. If you’re using SQLite, the database will be a file on your computer; in that case, `NAME` should be the full absolute path, including filename, of that file. The default value, `BASE_DIR / 'db.sqlite3'`, will store the file in your project directory.

- If you’re using a database besides SQLite, make sure you’ve created a database. Also make sure that the database user provided in mysite/settings.py has “create database” privileges.

- `INSTALLED_APPS` holds the names of all Django applications that are activated in this Django instance. Apps can be used in multiple projects, and you can package and distribute them for use by others in their projects.

- `python manage.py migrate` is used to create tables in the database. The `migrate` command looks at the `INSTALLED_APPS` setting and creates any necessary database tables according to the database settings in your `mysite/settings.py` file and the database migrations shipped with the app. (Covered later)

- `Model`: is essentially your database layout, with additional metadata. A `model` is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Django follows the [DRY (Don't Repeat yourself)](https://docs.djangoproject.com/en/4.0/misc/design-philosophies/#dry) Principle. The goal is to define your data model in one place and automatically derive things from it.

- Use `model.py` to create the table:

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # 'date published is the human-readable name. in others, we haven't used human-readable names.
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

- Each field is represented by an instance of a Field class – e.g., `CharField` for character fields and `DateTimeField` for datetimes. This tells Django what type of data each field holds. The name of each Field instance (e.g. question_text or pub_date) is the field’s name. You’ll use this value in your Python code, and your database will use it as the column name. In the example above, we’ve only defined a human-readable name for `Question.pub_date`. For all other fields in this model, the field’s machine-readable name will suffice as its human-readable name.

- To include the app in our project, we need to add a reference to its configuration class in the `INSTALLED_APPS` setting. The `PollsConfig` class is in the `polls/apps.py` file, so its dotted path is `'polls.apps.PollsConfig'`. Edit the `mysite/settings.py` file and add that dotted path to the `INSTALLED_APPS` setting. It’ll look like this::

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- Then run the following commands:

```shell
python .\manage.py check
python .\manage.py makemigrations polls
python .\manage.py migrate
```

- By running `makemigrations`, you’re telling Django that you’ve made some changes to your models and that you’d like the changes to be stored as a _migration_. Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. You can read the migration for your new model if you like, they’re designed to be human-editable.

- The `sqlmigrate` command takes migration names and returns their SQL (doesn’t actually run the migration). It’s useful for checking what Django is going to do:

```python
python manage.py sqlmigrate polls 0001
```

- Note:

  - Table names are automatically generated by combining the name of the app (polls) and the lowercase name of the model – question and choice. (can override)
  - Primary keys (IDs) are added automatically. (can override)
  - By convention, Django appends "\_id" to the foreign key field name. (can override)

- The `migrate` command takes all the migrations that haven’t been applied (Django tracks which ones are applied using a special table in your database called `django_migrations`) and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.

#### Inserting data using python

- Run the command `python .\manage.py shell`
- Copy the following to insert data

```python
from polls.models import Choice, Question

# to print all questions in the system.
Question.objects.all()

from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save() # this will save the data in sqlite3
q.id() # prints the id
q.question_text
q.pub_date
q.question_text = "What's up?"
q.save()

# objects.all() displays all the questions in the database.
Question.objects.all()
# <QuerySet [<Question: Question object (1)>]>

Question.objects.filter(id=1)
Question.objects.filter(id=1).values() # this is like the where clause.
Question.objects.values() # to get all the values stored in the database.

current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)

# pk: primary key
Question.objects.get(pk=1) # identical to Question.objects.get(id=1)

# Display any choices from the related object set -- none so far.
q.choice_set.all()
# <QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
# <Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
# <Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
# <Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
# <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
# 3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# https://docs.djangoproject.com/en/4.0/topics/db/queries/#field-lookups-intro
Choice.objects.filter(question__pub_date__year=current_year)

Question.objects.filter(name='Dhiraj').delete()
Question.objects.filter(name='Dhiraj').update(email='dhiraj@some.com)
Question.objects.values().order_by('email')
```

- `<QuerySet [<Question: Question object (1)>]>` isn't helpful. To fix that add `__str__()` in the model definitions in `polls/models.py`:

```python
from django.db import models

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
```

### Introducing the Django Admin

- Run the following:

```shell
python manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: **********
Password (again): *********
Superuser created successfully.

python manage.py runserver
# http://127.0.0.1:8000/admin/
```

- As of now, polls app is not displayed on the admin index page. For that we need to tell the admin that `Question` objects have an admin interface. To do this, edit `polls/admin.py`:

```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

### Model-View-Controller

- In MVC, the `model` represents the information (the data) of the application and the business rules used to manipulate the data; the `view` corresponds to elements of the user interface such as text, checkbox items, and so forth; and the `controller` manages details involving the communication to the model of user actions.

  - `Controller`: the code that does the thinking and decision making.
  - `View`: the HTML, CSS etc. which makes up the look and feel of the application.
  - `Model`: the persistent data that we keep in the data store.

- What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

#### Tasks inside the server

- Process any user input data (ie.e from a form) - possibly storing it in a database or maknig some other change to the database such as a delete.
- Decide which screen to send back to the user.
- Retrieve any needed data.
- Produce the HTML response and send it back to the browser (e.e. a template).

### More on View

- A view is a “type” of web page in your Django application that generally serves a specific function and has a specific template. In Django, web pages and other content are delivered by views. Each view is represented by a Python function (or method, in the case of class-based views). Django will choose a view by examining the URL that’s requested (to be precise, the part of the URL after the domain name).

- To get from a URL to a view, Django uses what are known as ‘URLconfs’. A URLconf maps URL patterns to views.

- Added a few more views to `polls/views.py` (`detail`, `results`, `vote`).

- Wire these new views into the `polls.urls` module by adding the following `path()` calls:

```python
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

- When somebody requests a page from your website – say, `“/polls/34/”`, Django will load the `mysite.urls` Python module because it’s pointed to by the `ROOT_URLCONF` setting. It finds the variable named `urlpatterns` and traverses the patterns in order. After finding the match at `'polls/'`, it strips off the matching text `("polls/")` and sends the remaining text – `"34/"` – to the `‘polls.urls’` URLconf for further processing. There it matches `'<int:question_id>/'`, resulting in a call to the `detail()` view like so: `detail(request=<HttpRequest object>, question_id=34)`

- Each view is responsible for doing one of two things: returning an HttpResponse object containing the content for the requested page, or raising an exception such as Http404. The rest is up to you. Your view can read records from a database, or not. It can use a template system such as Django’s – or a third-party Python template system – or not. It can generate a PDF file, output XML, create a ZIP file on the fly, anything you want, using whatever Python libraries you want.

- We changed the `def index` in `polls/views.py`.

```python
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
```

- Up until now the the page's design is hard-coded in the view (meaning changes have to be made in the python script if one wants to change the page design). To move away from python use templates. First, create a directory called `templates` in your polls directory. Within the templates directory, create another directory called polls, and within that create a file called `index.html`. In other words, your template should be at `polls/templates/polls/index.html`. Because of how the `app_directories` template loader works as described above, you can refer to this template within Django as `polls/index.html`.

- We changed the `def index` in `polls/views.py`.

```python
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

- That code loads the template called `polls/index.html` and passes it a context. The `context` is a dictionary mapping template variable names to Python objects.

- Common idiom to load a template, fill a context and return an `HttpResponse` object with the result of the rendered template. Django provides a shortcut.

```python
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

- Note that once we’ve done this in all these views, we no longer need to import loader and HttpResponse (you’ll want to keep HttpResponse if you still have the stub methods for `detail`, `results`, and `vote`).

- The `render()` function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an `HttpResponse` object of the given template rendered with the given context.

- Common idiom to use get() and raise Http404 if the object doesn’t exist. Django provides a shortcut.

```python
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

#### Removing hardcoded URLs in templates

- Later

#### Namespacing URL names

- The tutorial project has just one app, polls. In real Django projects, there might be five, ten, twenty apps or more. How does Django differentiate the URL names between them? The answer is to add namespaces to your URLconf. In the polls/urls.py file, go ahead and add an app_name to set the application namespace:

```python
...
app_name = 'polls'
...
```

#### Cross-Set Scripting

- [XSS](https://en.wikipedia.org/wiki/Cross-site_scripting). To handle it do the following in the `view.py`:

```python
from django.utils.html import escape

def detail(request):
  response = """<html><body> <p>"""+escape(request.GET['guess'])+"""</p></body></html>"""
  return HttpResponse(response)
```

- Another way to handle it is along with `path` (which we did above):

```python
path("<int:question_id>/", views.detail, name="detail")
```

- Also, all POST forms that are targeted at internal URLs should use the {% csrf_token %} template tag (see the `details.html`).

#### Use generic views: Less code is better

- These views represent a common case of basic web development: getting data from the database according to a parameter passed in the URL, loading a template and returning the rendered template. Because this is so common, Django provides a shortcut, called the “generic views” system.
- Let’s convert our poll app to use the generic views system, so we can delete a bunch of our own code. We’ll have to take a few steps to make the conversion. We will:

  1. Convert the URLconf.
  2. Delete some of the old, unneeded views.
  3. Introduce new views based on Django’s generic views.

- Amend URLconf: First, open the polls/urls.py URLconf and change it like so:

```python
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

- Amend views: Next, we’re going to remove our old index, detail, and results views and use Django’s generic views instead. To do so, open the polls/views.py file and change it like so:

```python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
```
