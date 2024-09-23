## Week 1

### Application Development Lifecycle

Regardless of the application type, every application will go through different phases, called the **application development lifecycle**. You can divide the application development lifecycle into seven phases: _Requirement gathering_, _analysis_, _design_, _code and test_, _user and system test_, _production_, and _maintenance_.

- **Requirement gathering** is the first phase in the application development process. In the requirement gathering phase, you will capture the requirements across all aspects of the application, including user requirements, business requirements, and technical requirements. You must also identify any constraints of design and viability of the business model.
- After gathering the requirements and constraints, you must analyze each to create a possible solution for the application’s design. During **analysis and design**, there might be multiple rounds of verification and revision to create a model solution that meets all the specified requirements. Across the analysis and design phases of application development, you must maintain proper documentation with records of all updates in the design. This documentation should be clear and concise as used during the code and test phase. The final proposed design and the specified requirements are passed on to the code and test phase.
- During the **code and test** phase, the team uses the programming requirements specified in the design documentation to code, test, revise, and test the application programs until the code meets all documented requirements. The tests you conduct for the unit code is called unit testing. Conduct the unit testing at the programming level to ensure you meet all required specifications. After the unit testing, you can generate an acceptable application version. The new version of the application is then run through a series of user and system level tests.
- The **user tests** verify the functionality from a user’s point of view. In addition, you will need to execute several **system-level tests**, including integration and performance testing. _Integration tests_ verify that all involved programs continue functioning as expected after integration. Integration testing also verifies that the application functions within a larger framework. _Performance testing_ helps evaluate the speed, scalability, and stability of the application based on varying workloads. After testing, you can generate a new application version and send it to production.
- Once in production, end users can access and use it. You must ensure that the application functions accurately and is available to users. When the application is in the production phase, it must remain in a steady state. In a steady state, you should not make any changes to the application. However, this is not always possible.
- The last phase in the application development lifecycle is **maintenance**. The application might need an upgrade, or you might need to add new features. In this case, the new features must go through all previous phases before being integrated into the application version deployed in production.

Every app usually has multiple functionalities, and the requirements for each functionality might vary. The best practice is to code each functionality in separate file. You can then create a central program, which runs the application and calls the individual files to perform specific functions. This approach to organizing code makes code maintenance efficient and easy. Having multiple files also helps when you need to add new functionality to an existing application. When you write the code for new functionality in a separate file, only the file will go through the entire design and verification process before being integrated into the running application.

### Introduction to Web Applications and APIs

A **web app** is a program stored on a remote server and delivered over the internet. A user interacts with the app using a browser.

A web app requires three components to process a client request: a web server to manage raised requests, an app server to execute the requested task, and a database to store the information needed to complete the task.

An **Application Programming Interface**, or API, is a software component that enables two unconnected apps to communicate

API is a more generic term given to all forms of apps that create a link between any two parts of a system. Web apps are a form of API that communicate between the front end and the back end.

### Python Style Guide and Coding Practices

**Static code analysis** is a method to evaluate code against a predefined style and standard without executing the code. Static analysis helps find issues, such as: Programming errors, Coding standard violations, Undefined values, Syntax violations, and Security vulnerabilities.

- Use Pylint

### Unit Testing

Unit testing is a method to validate if units of code are operating as designed. A unit is a smaller, testable part of an application.

During code development, you will test each unit. The test is performed in two phases. In the first phase, you will test the unit on your local system. If the test fails, you will determine the reason for the failure and fix the issue. Then, you will again test the unit. After the unit test passes, you will need to test the unit in a server environment, such as the continuous integration continuous delivery (or CI/CD) test server. If the unit fails the server test, you will receive the failure details. You will need to determine and fix the issue. Once the unit passes the server test, the unit is integrated into the final code base.

### Packaging

A Python **module** is a .py file containing Python definitions, statements, functions, and classes.
A **package** is a collection of python modules into a dictionary with a **init**.py file, which distinguishes it from just a dictionary of python scripts.

How to create a package?

```python
# package name: myproject

# Say the package has two modules, module1.py and module2.py

# to create a package, you will also need __init__.py file
# __init__.py will just import the packages.

# module1.py
def square(num):
    return num ** 2

# module1.py
def sum(num):
    return sum(num)

# __init__.py
from . import module1
from . import module2

# test in python
>>> import myproject
>>> myproject.module1.square(2)
# 4
```

- Note that the distinction between module and package is only at the file system level.

A **library** is a collection of packages or it can be a single package. Note that the terms package and library are often used interchangeably.

## WEEK 2

### Python Libraries and Frameworks for Application Development

**Frameworks** are predefined structures for application development. In addition, Frameworks provide a set of guidelines for application development. Frameworks facilitate good coding practices by offering a well-defined structure for writing and organizing code and enabling the reuse of code libraries for added features.

The framework contains the basic flow and the architecture of an application, which enables you to build the complete application. A Python library is a set of packages that perform only specific functionality.

### Introduction to Flask

Flask is a micro framework that can create web applications. It is not opinionated like some other larger frameworks and does not bind the user to a specific set of tools.

The main features of Flask include the following.

- Flask has a web server that runs applications in development mode.
- Flask also comes with a debugger to help debug applications. The debugger shows interactive traceback and stack trace in the browser.
- Flask uses standard Python logging for application logs, and you can use the same logger to log custom messages about your application.
- Flask provides a way to test different parts of your application. The testing feature enables developers to follow a test-driven approach. You can use frameworks like Pytest to ensure your code works as desired.
- Flask developers can access the request and response objects to pull arguments and customize responses.

Additional features of Flask are the following.

- The framework supports static assets like CSS files, JavaScript files, and images. Flask provides tags to load static files in the templates.
- You can also develop dynamic pages using Jinja templating framework and these dynamic pages can display information that may change for each request or may check if the user is logged in.
- Flask provides routing and supports dynamic URLs that are extremely useful for RESTful services. You can create routes for different HTTP methods and provide redirection in your application.
- You can write global error handlers in Flask that work on the application level.
- Flask supports user session management.

popular extensions

- Flask-SQLAlchemy
- Flask-Mail
- Flask-Admin
- Flask-Uploads: allow you to add customized file uploading to your application.

Other extensions

- Flask-CORS allows your application to handle Cross-Origin Resource Sharing, making cross-origin JavaScript requests possible.
- Flask-Migrate adds database migrations to SQLAlchemy ORM.
- Flask-User adds user authentication, authorization, and other user management activities.
- Marshmallow adds extensive object serialization and deserialization support to your code.
- Celery is a powerful task queue that can be used for simple background tasks and complex multi-storage programs and schedules.

### Request and Response Objects – Using GET and POST Modes

You define the path using the route decorator. The `@app.route` decorator defaults to the GET method.

All HTTP calls to Flask contain the request object created from the Flask. Request class. When a client requests a resource from the Flask server, it is handled by the @app.route decorator.

The following information is available in the request object:

- The address of the server in the form of a tuple, host, port.
- The headers sent with the request.
- The URL that is the resource asked by request.
- access_route that lists all the IP addresses for requests that are forwarded multiple times.
- full_path that represents the complete path of the request, including any query string.
- is_secure is true if a client makes a request using HTTPS or WSS protocol.
- is_JSON is true if the request contains JSON data.
- The Cookies dictionary contains any cookies sent with the request.

In addition, you can access the following data from the header:

- Cache-Control: holds information on how to cache in browsers.
- Accept: informs the browser what kind of content type is understood by the client .
- Accept-Encoding: indicates the code content.
- User-Agent: identifies the client, application, operating system, or version.
- Accept-Language: requests for a specific language and locale.
- Host: specifies the host and port number of the requested server.

There are multiple ways to get information from the Request Object.

- Use the `get_data` to access data from the POST request as bytes. You are then responsible for parsing this data. Y
- ou can also use the `get_JSON()` method to get data parsed as JSON from the post request.

Flask also provides more focused methods to get exact information from the request, so you don't have to parse the data into a specific type.

- `args` will give you query parameters as a dictionary.
- `JSON` will parse the data into a dictionary.
- `files` will provide you user uploaded files.
- `form` contains all values posted in a form submission.
- `values` combine the args data with the form data.

Some common response attributes include the following:

- `status_code` indicates the success or failure of the request.
- `headers` give more information about the response.
- `content_type` shows the media type of the requested resource.
- `content_length` is the size of the response message body.
- `content_encoding` indicates any encoding applied to the response, so the client knows how to decode the data.
- `mime-type` sets the media type of the response.
- `expires` contains the date or time after which the response is considered expired.

And here are some standard methods on response objects.

- `set_cookie` sets a browser cookie on the client.
- `delete_cookie` deletes a cookie on the client.

How Flask works with the response object using the different methods:

- A Response object with a status_code of 200 and a mime-type of HTML is automatically created for you when you return data from the @route method.
- JSONify also creates a Response object automatically.
- You can use make_response to create a custom response.
- Flask provides a special redirect method to return a 302 status-code and redirect the client to another URL.
- Flask provides an abort method to return a response with an error condition.

### Dynamic Routes

When developing RESTful APIs, you can send some resource-id as part of the request URL. For example, you want to create an endpoint that returns book information by International Standard Book Number (ISBN), but instead of hard coding the ISBN, you want the client to send it as part of the URL Flask provides **dynamic routing** for this purpose Let's look at a concrete example:

```python
@app.route("/book/<isbn>")
# @app.route("/book/<int:isbn>")
def get_author(isbn):
    res = requests.get("https://.../{escape(isbn)}.JSON")

    if res.status_code == 200:
        return {"message": res.JSON()}
    elif res.status_code == 404:
        return {"message": "something went wrong."}, 404
```

### Error Handling

Flask server automatically returns a 200 OK status when you return from the @app.route method. 200 is also returned by default when you use the `jsonify()` method to respond to a request.

You can also use the `make_response()` method to explicitly set the status code.

### Deploying Web Apps using Flask

The difference between Post and Put is that Post creates the object or data on every request, while Put creates the object or data only on the first request and continues to update the object or data in consecutive requests.

By default, the Flask application looks for the templates in a directory called `templates` under the root directory and `static` directory for static content.

### Reading: Decorators in Flask

**Decorators** help in annotating the methods and tell what a particular method is meant for. These are different from comments. This is used by the interpreter while running the code.

```python
def jsonify_decorator(function):
    def modifyOutput():
        return {"output":function()}
    return modifyOutput

@jsonify_decorator
def hello():
    return 'hello world'

@jsonify_decorator
def add():
    num1 = input("Enter a number - ")
    num2 = input("Enter another number - ")
    return int(num1)+int(num2)
print(hello())
print(add())
```

### Reading: Additional Features in Flask

You can use `flask.request.form` to access form data that a user has submitted via a POST request. For instance

```py
from flask import request
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # process login here
```

Flask provides a function called flask.redirect to guide users to a different webpages (or endpoints).

```py
from flask import redirect
@app.route('/admin')
def admin():
    return redirect('/login')
```

The flask.url_for function dynamically generates URLs for a given endpoint.

```py
from flask import url_for
@app.route('/admin')
def admin():
    return redirect(url_for('login'))
@app.route('/login')
def login():
    return "<Login Page>"
```
