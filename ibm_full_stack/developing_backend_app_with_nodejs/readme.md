## Week 1

### Course Introduction

- Node.js is a runtime environment that can run server-side JavaScript applications, while Express is a server-side JavaScript web framework that runs on top of Node.js in which to write your applications.

### What is Back End Development?

- The frontend runs on the client machine, and the backend runs on a server. The client machine runs the web browser and the web browser’s engine. The browser’s engine is what communicates with the backend.
- Servers consist of hardware, software, or both that communicate with and provide functionality to a client.
- Types of Servers:
  - The database server is the machine and the application that houses, retrieves, and delivers data. The terms “database server” and “database” are often used interchangeably.
  - Web servers ensure client requests are responded to, often using hypertext transfer protocol or HTTP for short. An HTTP server is part of the software running on a web server. The software part of a web server is what controls how a user accesses files hosted on the server.
  - Application servers host and deliver a business application through HTTP. They sit between a database server and a web server. Application servers transform data into dynamic content and run the business logic, which is the data storage and transfer rules.
- APIs, which stands for “application programming interface,” allow two pieces of software to communicate with each other. A web service is a type of web API.
- A web service is a type of web API. A web service communicates using HTTP requests. In other words, the web service is the programming interface that sends and receives requests using HTTP among web servers and the client.
- A runtime behaves similarly to a mini operating system that provides the resources necessary for an application to run. The runtime is the infrastructure that supports the execution of a codebase. It is the hardware and software environment in which an application gets executed. Node.js is an example of a backend runtime environment. The reason Node.js has become so popular as a backend technology is because it runs on Google Chrome’s open-source V8 engine.
- Another issue backend developers need to be concerned with is scalability. Scalability is essential for enterprise software success and is the responsibility of the backend which is affected by the load on an application. Load refers to the number of concurrent users, the number of transactions, and the amount of data transferred back and forth between the clients and servers. Web applications should be scalable. Scalability is the application’s ability to dynamically handle the load as it grows or shrinks without it affecting the application’s performance.
- Lastly, other backend responsibilities include security, authentication, and prevention of malware attacks.
- The backend is also mainly responsible for performance because it retrieves and transfers data between machines, delivers content to the front end, and supplies the business logic of the application.
- Node.js is single-threaded, which means it can only do one process at one time. That might make it sound like it is not appropriate for server-side coding but Node.js is asynchronous and non-blocking. This means, while a process is being executed, the program doesn’t have to wait until the process fininshes.
- Node.js is event-driven. When Node.js performs an input/output (I/O) operation, like reading from the network, accessing a database or the file system, an event is triggered. Instead of blocking the thread and wasting the processor time waiting, Node.js will resume the operations when the response comes back or, in other words, the reseponse event occurs. During that time, the server is not blocked and can do other things, which makes it look like it is multi-threaded.

### Introduction to NodeJS

- With server-side JavaScript, Node applications process, and route web service requests from the client.

  - In step 1, the user selects an option in the user interface, written in HTML and CSS.
  - In step 2, this action by the user triggers JavaScript code that implements the business logic on the client-side, for example, input validation.
  - In step 3, the JavaScript application makes a web service call over HTTP with a JSON data payload. The REST web service, which is part of a node.js application running on the node server, receives the HTTP request.
  - In step 4, the REST web service processes the request and returns the result to the client as a JSON payload over HTTP.

- ExpressJS abstracts lower-level APIs in Node.js by using  HTTP utility methods and middleware.

- The following features enable you to develop your application quickly:
  - Public: public assets like image, CSS, and javascript.
  - Templates/views: server-rendered HTML that is sent back to the client in response to requests.
  - Routes: defines endpoints that accept and process client requests.
  - Server.js: a file which contains the main application code.
  - Package.json: contains metadata information about the project including dependencies, scripts, and so on.

### Import and Require

- In Node.js, modules are files containing related, encapsulated JavaScript code that serve a specific purpose. Modules can be a single file or a collection of multiple files and folders. Developers rely heavily on modules because of their reusability as well as their ability to break down complex code into manageable chunks. When the external application calls a module, the module is called using an `import()` or a `require()` statement. Which statement is needed depends on the specification.
- A directory with one or more modules bundled together is called a `package`. Module specifications are the conventions and standards used to create packages in JavaScript code for Node.js applications. The most commonly used module specifications for Node.js applications are `CommonJS` and `ES modules`.
- By default, Node.js treats JavaScript code as a CommonJS module. Library authors can easily enable ES modules in a Node.js package by simply changing the package file extension from `.js` to `.mjs`. CommonJS modules use the `require()` statement to import modules whereas ES modules use the `import()` function.
- When a module is needed outside of its own file it must be exported first. The `module.exports` statement should be used with CommonJS. Modules can be exported to an ES specification using the `export` keyword.
- Differences in calling require and import within the application code. The require statement can be called anywhere in the file whereas the import statement must be called at the beginning of the file. This means that require can be called within conditional statements and functions, but import cannot. This may sound like an advantage of require but note that the require statement is bound dynamically whereas import is bound statically. This means errors that occur when linking the function definition to the function call will not be identified until run-time. For Import, binding errors are identified at Compile time.
- Require modules are synchronous in nature and modules imported with import are asynchronous. Synchronous means the modules will be loaded and processed in a linear fashion, one at a time. Asynchronous means the modules can be processed simultaneously. Import runs faster compared to require functions in large-scale applications which involve loading hundreds of modules.

```js
// export from a file named message.js
module.exports = "hello world";
// import from the message.js file
let msg = require('./message.js')
///////////////////////////////////////////////
///////////////////////////////////////////////
// exprt from file named module.mjs
const a = 1;
export {a as "myvalue"};
// import from module.mjs
import { myvalue } from module.mjs
```

### Introduction to Server

- In step 1, the user selects an option in the user interface, which is written in HTML and CSS. In step 2, the option triggers a JavaScript application that implements the business logic on the client-side. In step 3, the JavaScript application makes a web service call over HTTP with a data payload written in JSON. In step 4, a REST web service intercepts the HTTP request and in the final step, instead of invoking an Enterprise Java application, the Node.js server hosts an application written in the JavaScript language. This code written in JavaScript runs on the server, and not in the client's web browser.

### Creating a Web Server with Nodejs

- JS is built with a heavy emphasis on concurrent programming with a lightweight language. Node.js is a single-threaded application environment that handles input/output (I/O) operations through events. Instead of blocking on asynchronous I/O operations, you write callback functions to handle results when they complete. Node.js is suited for developers who want to build scalable and concurrent server applications by using features like callback functions and the Node.JS runtime event loop.
- Every JavaScript file is a module in Node.js. A module corresponds to a script file. A package can contain one or more nodes. The Node.js runtime is packaged with many utility modules that you can use to create and extend your applications. With the HTTP Node.js module, you can develop an application that listens to HTTP requests and returns HTTP response messages.

```js
let server = http.createServer(function (request, response) {
  let body = "hello world";
  response.writeHead(200, {
    "Content-Length": body.length,
    "Content-Type": "text/plain",
  });
  resposne.end(body);
});
server.listen(8080);
```

### Working with Nodejs Modules

- A package consists of one or more modules. The package.json file describes details about a Node.js module. If a module does not have a package.json file, Node.js assumes that the main class is named `index.js`. To specify a different main script for your module, specify a relative path to the Node.js script from the module directory.
- The require statement assumes that scripts have a file extension of .js. The require function creates an object that represents the imported Node.js module. When you call require with the name of a subdirectory, Node.js looks for a script file with the same name as the subdirectory. If the script file does not exist, the function assumes that the name is the name of a directory and looks for a script named index.js within that directory.
- To make a function or a value available to Node.js applications that import your module, add a property to exports.
- Libraries are the same thing as modules in regard to Node.js. Libraries contain code that has been developed that can be reused throughout an application. There are three types of modules:
  - Core Node.js modules form a minimal library. They contain the minimal functionality needed to develop Node.js applications.
  - Local modules are the modules written by you and the development team as part of creating your Node.js application.
  - Third-party modules are available online and have been created by the back-end Node.js community.
- The most important of the core modules are http, path, fs, os, util, url, and querystring.

```js
let http = require("http");
http
  .createServer(function (req, res) {
    res.write("hello from server"); //write a response to the client
    res.end(); //end of response from server
  })
  .listen(6000); //the server instance listens for http requests on port 6000
```

```js
// sample code to read a file synchronously using the fs.readFile() method
const fs = require("fs");
const data = fs.readFile("sample.txt", "utf8");
// print contents of the file "sample.txt" to console
console.log(data);
```

```js
const fs = require(‘fs’);
const data = fs.readFileSync(‘/content.md’); // blocks here until file is read
console.log(data);//writes data in the content.md file to the console
```

```js
let os = require("os");
console.log("Computer OS Platform Info : " + os.platform());
console.log("Computer OS Architecture Info: " + os.arch());
```

```js
const path = require("path");
let result = path.basename("/content/index/home.html");
console.log(result); //outputs home.html to the console
```

```js
let util = require("util");
let str = "The loop has executed %d time(s).";
for (let i = 1; i <= 10; i++) {
  console.log(util.format(str, i)); //outputs 'The loop has executed i time(s)'
}
```

```js
const url = require("url");
let webAddress =
  "http://localhost:2000/index.html?lastName=Kent&firstName=Clark";
let qry = url.parse(webAddress, true);
let qrydata = qry.query; //returns an object: {lastName: 'Kent', firstName: 'Clark'}
console.log(qrydata.firstName); //outputs Clark
```

```js
let qry = require("querystring");
let qryParams = qry.parse("lastName=Kent&firstName=Clark");
console.log(qryParams.firstName); //returns Clark
```

### Overview of Node Package Manager

- A package manager is a set of tools used to deal with modules and packages containing dependencies.
- Dependencies are code, usually in the form of libraries and packages, that are called and reused in a program.
- A library of code usually contains many dependencies, but the library is self-contained and isn’t dependent on code outside of the library itself. Packages work the same.
- A package manager automates the process of finding, installing, upgrading, configuring, maintaining, and removing packages for a computer program. Package managers usually are connected to and maintain a database of dependencies and versioning information for the packages in a repository. The package manager ensures that a piece of software has the dependencies to run correctly and eliminates the need to do this work manually.
- Node Package Manager, usually abbreviated as NPM, is the default package manager for the Node.js runtime engine. NPM has two functions. First, it provides a command line interface that allows users to publish and download packages. Second, it behaves as an online repository of binary JavaScript packages. The repository is a database of packages that tracks versions of packages referenced in applications.
- All NPM packages require a file named “package.json” that should be located in the project’s root directory. NPM uses the metadata in the package.json file to determine all of the dependencies in a package. This file contains the project’s identifying metadata in the form of key-value pairs that, at a minimum, identify the name of the project and the project’s version number.
- There are two ways in which NPM can install packages:
  - locally: to install a package you want to use within your application. Run the local install command from the directory you want the package installed in. The local install is npm’s default behavior. To install the node_modules package locally, use the NPM command line interface to enter: `npm install <package_name>`. This command creates a directory named node_modules with the package and its dependencies in your current working directory.
  - Globally: means that all applications on the machine in which the package is installed can use that code. Global installs should be used judiciously because all projects on that computer will make use of that package and its dependencies. If you have different versions of a project on your machine, they will all use the globally installed package, which might break compatibility with other dependencies. To install node_modules so the package can be accessed by any application on the machine, which means they are installed globally, use the command `npm install -g package_name` in the command line interface.

## Week 2

### Asynchronous I/O with Callback Programming

- Network operations run in an asynchronous manner. For example, the response from a web service call might not return immediately.
- When an application blocks (or waits) for a network operation to complete, that application wastes processing time on the server. Node.js makes all network operations in a non-blocking manner. Every network operation returns immediately. To handle the result from a network call, write a callback function that Node.js calls when the network operation completes.
- Interaction between the application, the Node.js framework, the web service call to the remote server, and the call back to the callback function:
  - In the first step, the application makes a call to HTTP.request. This function makes a call to the remote web server and requests the web service.
  - Before the Node.js framework receives the HTTP response message from the remote web server, it immediately returns a result for the HTTP.request function call. This result simply indicates that the request message was sent successfully. It does not say anything about the response message.
  - When the Node.js framework receives an HTTP response message from the remote server, it calls the callback function that you defined during the HTTP.request function call. This function handles the HTTP response message.
- The purpose of the callback function is to handle two events: request.on('data') and request.on('end').

```js
let options = {
  host: "some host",
  path: "some path",
  // can add other things like password, token etc
};

// http.request(options, [callback (optional)])
http
  .request(options, function (response) {
    // this is a (anonymous) callback function.
    let buffer = "";
    let result = "";
    // when nodejs module calls this (anonymous) function, events occur while it is receiving parts of the http response object
    // 'data' and 'end' are the events.
    // for these event, you define more callback functions to handle each event type.
    response.on("data", function (chunk) {
      buffer += chunk;
    });

    response.on("end", function () {
      console.log(buffer);
    });
  })
  .end();
```

- The Node.js framework emits several events during the course of the request function. You can listen to these events by using the object.on() method and passing in the event name as the first parameter. If the request is successful, a 'data' event is emitted on the response object every time data comes in, followed by an 'end' event when the response finishes. If the request fails, there is an 'error' event followed by the 'close' event.

### Creating Callback Funtions

```js
export.current = function (location, resultCallback) {
  // ...
  let options = {
  host: "some host",
  path: "some path",
  // can add other things like password, token etc
};

// http.request(options, [callback (optional)])
http
  .request(options, function (response) {
    // this is a (anonymous) callback function.
    let buffer = "";
    let result = "";
    // when nodejs module calls this (anonymous) function, events occur while it is receiving parts of the http response object
    // 'data' and 'end' are the events.
    // for these event, you define more callback functions to handle each event type.
    response.on("data", function (chunk) {
      buffer += chunk;
    });

    response.on("end", function () {
      parseString(buffer, function(error, result){
        if (error) {
          resultCallback(error);
          return;
        }

        resultCallback(null, result.current_observatin.temp_f[0]);
      });
    });
  })
  .end();
}
```

- Recall how callback functions check the first parameter to see if an error condition occurred. Instead of printing the result in the console, you call the resultCallback callback function with the error object. You pass back the error object to the resultCallback callback function of the main application. If no error occurred, you call the resultCallback function with null as the first parameter. The codes are in the custom Node.js module.
- The callback handler printed the contents of the HTTP response message body to the console. What if you wanted it to return the response message to the original calling application? If you use a return function, Node.js might call the callback function after the http.request() call completes. The application calls the exported function. The module that implements the function calls http.request so that the Node.js framework can make a web service call on its behalf. When that request is sent successfully, the framework returns control to the Node.js module. Then the Node.js module returns control to the application. When the remote server sends back a HTTP response message to the Node.js framework, the framework calls the callback handler that was defined by the Node.js module. However, there is no connection between the callback function and the main application. So, how do you link the callback function to the main application? The pattern is that when one Node.js application calls a module in a non-blocking manner, the application provides a callback function to process the result. If the main application calls http.request(), it must provide a callback handler to process the HTTP response message. If the main application calls a function that calls http.request(), there are two callback functions: The custom module has a callback function that handles the HTTP response message from http.request(). And the main application has a callback function that processes the result captured in the first callback function.
- Let’s see how this solution works. We’ll create a callback function to capture the result from the http.request function call. The application makes a call to the Node.js module. The Node.js module makes an http.request function call in order to send an HTTP request message to a remote server. Before the remote service returns an HTTP response message, the http.request function call returns control to the Node.js module as the request message was successfully sent. Then the Node.js module replies with a value to the main application. At a future point, the remote server sends back an HTTP response message. The Node.js framework calls the callback function defined by the Node.js module. This callback function calls another callback function defined by the main application. Having one callback function invoke another callback function is the only way to pass a message from the Node.js module to the main application when the Node.js module receives a response message.

### Issues with Callbacks

- Callback is a function that is passed as an argument to another function that executes the callback based on the result. They are basically functions that are executed only after a result is produced. Callbacks help us develop asynchronous JavaScript code. Callbacks make sure that a function won’t run before a prerequisite task is completed.
- Usually, these asynchronous callbacks, or async for short, are used for accessing values from databases, downloading images, reading files, and so on. Callback functions wait for a response, and when the response is sent, then they execute.
- The nesting of callback functions is often referred to as “Callback Hell” and is essentially nested callbacks stacked below one another, forming a pyramid structure. This structure is also sometimes referred to as “The Pyramid of Doom.”
- Another issue with callbacks is `inversion of control`, also called IoC. Inversion of control happens when the flow of control, such as the execution of instructions, is external to your code. Many times, callbacks hand the control over to a third party. But issues and errors with that third-party code can be difficult to catch. You are forced to trust the third-party code, or you must write additional code that ensures the third-party code does not:
  - Get called too many times or too few times,
  - Get called too early or too late,
  - Lose context, or pass back incorrect arguments.
- There are a number of ways to mitigate callback hell and trust issues: You can write comments, split functions into smaller functions, use Promises, or you can use async/await.

### Promises

- A promise is an object returned by an asynchronous method. The promise has three states, which are pending, resolved, and rejected. Promises are most useful for application programming interface (API) requests, input/output (I/O) operations, and other operations that are time consuming and can block resources.
- A method can be defined to return a promise object, if you know it is going to take time for execution and thereby block resources.
- When you call a method that returns a promise, a promise object is created. The initial state of the promise is the pending state. It is in this state until the operation is complete or some error has caused the operation to abort. When the operation is complete, the promise is said to be resolved. When there is an error, the promise is said to be rejected.
- The axios package returns a promise object. The status of the promise until it hears back from the uniform resource locator (URL) requested is pending.

```js
const axios = require("axios").default;

const connectToURL = (url) => {
  const req = axios.get(url);
  console.log(req);
  req
    .then((resp) => {
      console.log("fulfilled");
      consolelog(resp.data);
    })
    .catch((err) => {
      console.log("rejected");
    });
};
```

### Working with JSON

- Attribute: value pairs

## Week 3

### Introduction to Web Frameworks

- Node.js is a runtime environment that executes JavaScript on a server. `Runtime environments` are the hardware and software that can execute programs with a particular codebase.
- A `framework` is like a skeleton on which an application is built for a specific environment. The framework is the fundamental structure that supports the application.
- So, in order to utilize Node.js, you need to use a web framework that works in conjunction with it. A framework that works with Node.js is called a node web framework or just a node framework.
- Two approaches to building back ends that web frameworks can employ:
  - `Model-View-Controller (MVC)`: An MVC approach can be used simultaneously with REST APIs. They are not mutually exclusive. MVC is an architectural pattern that divides an application into three components: model, view, and controller. Let’s discuss what each of these components is. The model layer is responsible for managing the data of the application. It interacts with the database and handles the data logic. The view is responsible for rendering the presentation of the data that is passed to it by the model. And the controller regulates the flow of the data. It is responsible for processing the data supplied to it by the user and sends that data to the model for manipulation or storage.
  - `Representational state transfer application programming interfaces (REST API)`: REST APIs allow multiple web services to communicate with each other. RESTful APIs are subject to certain constraints. The code on the client must be completely independent of the server code. Client-side code can be updated without interfering with the server code and vice versa. Secondly, RESTful APIs are also stateless. `Stateless` means the client does not need to know the state of the server, nor does the server need to know the state of the client for communication between the two. REST APIs communicate via operations on resources, and they do not rely on a particular implementation of the API.
- When a client requests resources using a REST API using HTTP methods such as GET, POST, PATCH, or DELETE, the server responds with a representation of the state of the resource to the client. The representation of the data transferred between client and server is usually a JSON payload but can also be HTML, XLT, Python, PHP, or plain text.
- `Express.js` is one of the most popular Node Web Frameworks. It is used for routing and middleware. Its straightforward coding using JavaScript means there is a fairly small learning curve. It is easy to implement an MVC architecture pattern with Express. It provides debugging mechanisms to help easily pinpoint the errors in the application. Express delivers high performance because it handles multiple operation requests concurrently that are independent of each other with asynchronous programming. It has many HTTP helpers that make programs intelligible and reusable for handling HTTP requests. It has great content negotiation that helps the client and server to communicate by efficiently providing HTTP headers to URLs, fetching the exact data needed for the requesting client.
- `Koa` is a relatively new web framework designed by the same team who designed Express. It intends is designed to be smaller, more expressive, and provide a more robust foundation for web applications and APIs. Koa uses async functions in such a way that callbacks are not necessary, and it increases the ability to handle errors. Koa is appropriate for applications that are high-performing, demanding, complex, and developed by large, experienced teams.
- `Socket.io` is an excellent choice for developing apps where bidirectional data is exchanged between clients and servers in real-time. You can develop applications that utilize WebSocket rather than HTTP for communication. Its servers push data without the need for that data to be called by the client. It is appropriate for applications such as chat rooms, texting applications, video conferencing, and multiplayer games.
- `Hapi.js` is a reliable open source node web framework with lots of security built into it. There are many built-in plugins, so you won’t need to use unofficial middleware. It is most known for developing proxy and API servers, HTTP-proxy applications, REST APIs, and other desktop applications.
- `NestJS` framework which is appropriate for building dynamic, scalable enterprise applications in conjunction with its flexibility due to its multitude of libraries. It follows an MVC architecture. NestJS is built on top of Express, so they have similar purposes and provide comparable functions. It is compatible with TypeScript, which is a subset superset of JavaScript. It works in conjunction with the front-end Angular framework. And Nest combines both object-oriented and functional reactive programming, which potentially doubles productivity and application performance.

### Express Web Application Framework

- Express is a web application framework based on the Node.js runtime environment, however, Express abstracts low-level details. Express helps you organize your application better and develop your application faster. It provides robust mechanisms for integrating middleware packages and handling different hypertext transfer protocol (HTTP) request methods. The Express web application framework is widely used in the field today and forms the basis of other frameworks as well.
- Express is primarily used for two purposes:
  - as an API: Using Express to build APIs means setting up an HTTP interface to interact with the data layer. In the case of APIs, data is sent back to the client in JSON format using a response object, or `res` for short. The `res.json` method is used to notify the client of the content type of the data being sent, such as if it's an image or text. It can also be used to `Stringify` data, in other words, converting JavaScript to JSON format.
  - to set up templates with server-side rendering (SSR): In Server-side rendering (SSR), Express is used to set up templates. Express is responsible for using the data sent from the client supplied by an HTTP request in conjunction with the template to dynamically write HTML, CSS, and/or JavaScript. The HTML, CSS, and/or JavaScript is sent back to the client as text so that the browser can render the page. This is accomplished using the Express `res.render` method.
- Express implements an app class that you map to a web resource path. In contrast, when using the Node.js core application programming interface (API), the http.createServer function relies on your custom callback function to parse through the web resource path.
- Here is an overview of how to work with Express. There are five steps (in more detail in the next point).
  - One, declare Express as a dependency in the package manifest of a Node.js project.
  - Two, run the npm command to download any missing modules.
  - Three, import the Express module and create an Express application.
  - Four, create a new route handler.
  - Five, start an HTTP server on a given port number.
- To declare Express as a dependency in the `package.json` file, create a package.json file in your project folder. The package.json file stores information about the contents of a Node.js module including five items: name, version, description, main, and dependencies.
  - `Name` is a name for the Node.js module.
  - `Version` is a string that defines the major and minor version number of the module.
  - `Description` is a sentence that describes the purpose of the module.
  - `Main` identifies the Node.js script as the entry point into the module.
  - `Dependencies` is a list of which Node.js modules that the current module requires.
- To declare Express as a dependency, list the Express module and a version number in the dependencies property.
- When you run the npm install command inside the Node.js module directory, it resolves any missing dependent Node.js modules. The command downloads and saves any missing Node.js modules into its own node_module directory. This scheme allows you to use different versions of the same Node.js module in different packages. When you run the command npm install with no parameters, the npm application scans your package.json file. It checks your node_module directory to see if any modules are missing.

### Your First Express Web Application

- When you declare Express as a dependency in your Node.js project and download any missing modules, you can create a mynodeserver.js file in your project folder. Now you can start coding with your first Express program.

```js
app.listen(3333, () => {
  console.log(“Listening at
  http://localhost:3333)
})
```

### Introduction to Middleware & Routers

- Middleware is software that sits between applications, databases, or services and allows those different technologies to communicate. It creates seamless interactions for the end user in a distributed system.
- Express is a messaging framework used to handle routes and write middleware. The front end of an application uses Express to facilitate communication between components on the back end without the front-end and back-end services needing to use the same language. The front end communicates with the middleware, not directly with the back end.
- Messaging frameworks like Express commonly contain JSON, REST APIs, and web services. Older messaging frameworks may contain extensible markup language (XML) and simple object access protocols (SOAP) instead of JSON and REST APIs, respectively. The messaging framework provides a standardized way to handle data transfer among different applications.
- A web server is an example of middleware that connects a website to a database. The web server handles the business logic and routes the data from the database based on the request.
- A `route` is the part of the code that associates an HTTP request, such as GET, POST, or DELETE, with a URL and the function that gets called that handles that URL. Routing is used in web development to split an application’s user interface based on rules identified by the browser’s URL.
- Router functions are called “middleware” collectively. Middleware is responsible for responding to an HTTP request or calling another function in the middleware chain. Express handles router functions through the Router class, such as Router.get(). As the name suggests, Router.get() handles HTTP GET requests. Other Router functions include Router.post(), Router.put(), Router.delete() in mostly the same way. These methods take two arguments, a URL path and a callback function.
- In addition to routing, middleware is also responsible for providing secure connections among services by encrypting and decrypting data, managing application loads by distributing traffic to different servers, and sorting or filtering data before the data is returned to the client.

### Routing, Middleware, and Templating

- When there are many routes to handle, code maintenance is better with routers. A router by itself is used for branching query handling and routing each query differently.

```js
const express = require('express');
const app = new express();

let userRouter = express.Router();
let itemRouter = express.Router();

app.user('/user', userRouter)
app.user('/item', itemRouter)


userRouter.get(...,(req, res)=> {
  res.send("..")
})

itemRouter.get(...,(req, res)=> {
  res.send("..")
})
```

- `Middleware` includes functions that have access to the request and response objects and the next function. The next parameter determines what is done after the function is executed. An Express application can have more than one middleware and they can be chained to each other. Middleware is categorized based on purpose, use, and source. Five types of middleware are `application level`, `router level`, `error handling`, `built-in`, and `third party`, Middleware is useful for activities like parsing requests, adding authentication, and handling errors.

- Application-level middleware is bound to the application using `app.use`. All the client requests to this server application are routed through this middleware. This routing is useful for activities like authentication and checking session information. Consider application-level middleware as a gatekeeper. No request to the application server can go past it.

```js
const express = require("express");
const app = new express();
function myLogger(req, res, next) {
  req.timeReceived = Date();
  next();
}
app.get("/", (req, res) => {
  res.send("Request received at " + req.timeReceived + " is a success!");
});
```

- Router-level middleware is not bound to the application. Instead, it is bound to an instance of express.Router(). You can use a specific middleware for a specific route instead of having all requests going through the same middleware.

```js
const express = require(“express”);
const app = new express();
let userRouter = expess.Router();
let itemRouter = express.Router();
//router
userRouter.use(function (req, res, next){
  console.log("User query time:", Date());
  next();
})
//middleware
userRouter.get("/:id", function (req, res,
  next) {
  res.send("User "+req.params.id+ " last successful login "+Date())
})

itemRouter.use(function (req, res, next){
  console.log("Item query time:", Date());
  next();
})
itemRouter.get("/:id", function (req, res,
  next) {
  res.send("Item "+req.params.id+ " last query "+Date())
})

app.use('/user', userRouter)
app.use('/item', itemRouter)

app.listen(3333, () => {
  console.log("Listening at http://localhost:3333")
})
```

- Error-handling middleware can be bound to either the entire application or to specific routers. Error-handling middleware always takes four arguments, which are error, request, response, and the next function that it needs to be chained to. Even if you don’t use the next parameter, you still have to define it in the method signature.

```js
const express = require(“express”);
const app = new express();

app.user('/user/:id', function(req, res, next) {
  if(req.params.id ==1){
    throw new Error("Trying to access admin login")
  } else{
    next();
  }
})
//error-handling middleware.
app.user(function(err, req,res, next){
  if(err!=null) {
    res.status(500).send(err.toString())
  } else{
    next();
  }
})

app.get(...)
app.list(...)
```

- Built-in middleware is useful for activities such as rendering hypertext markup language (HTML) pages from the server, parsing JavaScript Object Notation (JSON) input from the front end, and parsing cookies.

```js
const express = require(“express”);
const app = new express();

app.usesr(express.static('...'))

app.listen(...)
```

- Creating middleware is simple. It is a function that takes three parameters, which are request, response, and next. You can define a method that takes these three parameters and then bind it with app.use or router.use. The order in which the middleware is chained depends on the order in which the .use method is used to bind them.

```js
const express = require(“express”);
const app = new express();

function myLogger(req, res, next){
  req.timeReceived = Date();
  next();
}

app.user(myLogger)

app.get('/', (res, req)=> {
  res.send("request ..." +req.timeReceived+"is a success")
})

app.listen(...)
```

- Template rendering is the ability of the server to fill in dynamic content in the HTML template.

```js
const express = require(“express”);
const app = new express();
const expressReactViews = require('express-react-views');
const jsxEngine = expressReactViews.createEngine();

app.set('view engine', 'jsx')

app.set('views', 'myviews')

app.engine('jsx', jsxengine)

app.get('/:name', (req, res)=> {
  // index is an html file name
  // name is passed to that file.
  res.render('index', {name: req.params.name})
})

app.listen(...)
```

### Introduction to Authentication and Authorization

- The `authentication` process confirms a user’s identity using credentials by validating who they claim to be. Authentication is the responsibility of an application’s backend.
- Three popular authentication methods in Node.js include:
  - Session-based
  - Token-based
  - Passwordless
- Flow of a `session-based` is as follows:
  - The user uses their credentials to log in.
  - The login credentials are verified against the credentials in a database. The database is responsible for storing which resources can be accessed based on the session ID.
  - The server creates a session with a session ID that is a unique encrypted string. The session ID is stored in the database.
  - The session ID is also stored in the browser as a cookie.
  - When the user logs out or a specified amount of time has passed, the session ID is destroyed on both the browser and the database.
- `Token-based` security entails two parts: authentication and authorization. Authentication is the process of providing credentials and obtaining a token that proves the user’s credentials. Authorization refers to the process of using that token so the resource server knows which resources the user should have access to.
- `Token-based authentication` uses access tokens to validate users. An access token is a small piece of code that contains information about the user, their permissions, groups, and expirations that get passed from a server to the client. An ID token is an artifact that proves that the user has been authenticated. The token contains three parts, the `header`, the `payload`, and the `signature`. The header contains information about the type of token and the algorithm used to create it. The payload contains user attributes, called `claims`, such as permissions, groups, and expirations. The signature verifies the token’s integrity, meaning that the token hasn’t changed during transit. A JSON web token, pronounced “jot” but spelled `JWT`, is an internet standard for creating encrypted payload data in JSON format. A user's browser makes a call to an authentication server and gets access to a web application. The authentication server then passes back an ID token which is stored by the client as an encrypted cookie. The ID token is then passed to the app on the web server as proof that the user has been authenticated.
- `Token-based Authorization`: The authorization process gets executed when the web application wants to access a resource, for example, an API that is protected from unauthorized access. The user authenticates against the Authorization server. The Authorization server creates an access token (note that the ID token and access token are two separate objects) and sends the access token back to the client, where the access token is stored. Then when the user makes requests or resources, the token is passed to the resource, also called an API server. The token gets passed with every HTTP request. The token contains embedded information about the user’s permissions without the need to access those permissions from the authorization server. Even if the token is stolen, the hacker doesn’t have access to the user’s credentials because the token is encrypted.
- With `passwordless` authentication, the user does not need login credentials, but rather, they gain access to the system by demonstrating they possess a factor that proves their identity. Common factors include biometrics such as a fingerprint, a “magic link” sent to their email address, or a one-time passcode sent to a mobile device. Password recovery systems now commonly use passwordless authentication. Passwordless authentication is achieved using Public Key and Private Key Encryption. In this method, when a user registers for the app, the user’s device generates a private key/public key pair that utilizes a factor that proves their identity, as noted above. The public key is used to encrypt messages, and the private key is used to decrypt them. The private key is stored on the user’s device, and the public key is stored with the application and registered with a registration service. Anyone may access the public key, but the private key is only known to the client. When the user signs into the application, the application generates a login challenge, such as requesting biometrics, sending a “magic link,” or sending a special code via SMS, encrypting it with the public key. The private key allows the message to be decrypted. The app then verifies the sign-in challenge and accepts the response to authorize the user.

### Authentication in NodeJS

- Following are some of the advantages of using Token based authentication. Token based authentication is more scalable as the token only needs to be stored on the client side. Also, since the server only needs to verify the token along with the user information, it is easier to handle multiple users. Token based authentication offers flexibility as they can be used across multiple servers, and they can offer authentication for diverse websites and applications at once. And JWT used in Token Based Authentication can be signed and encrypted, which means they cannot be tampered with and also cannot be read without the Private Encryption Key.

```js
const express = require("express");
const myapp = express();

myapp.get("/employees", (req, res) => {
  return res.status(401).json({ message: "please login to access" });
});

myapp.listen(5000, () => {
  console.log("api server is localhost:5000");
});
// save this in a file apiserver.js
// to verify that the endpoint cannot be accessed unless the suer is authorized, run
// curl -i localhost:5000/employee
```

- This is just a pseudocode

```js
//install josonwebtoken package

const express = require("express");
const jsonwebtoken = require("jsonwebtoken");

const JWT_SECRET = "secretString";

const myapp = express();
myapp.use(express.json());

myapp.post("/signin", (req, res) => {
  const { uname, pwd } = req.body;
});

// return the JWT token
if (uname === "user" && pwd === "password") {
  return res.json({ token: jsonwebtoken.sign({ user: "user" }, JWT_SECRET) });
}
return res.status(401).json({ message: "invalid username and/or password" });

// define GET API method
myapp.get("/employees", (req, res) => {
  let tkn = req.header("Authorization");
  if (!tkn) return res.status(401).send("no token");
  if (tkn.startWith("Bearer ")) {
    tokenValue = tkn.slice(7, tkn.length).trimLeft();
  }
});

// verify the JWT
myapp.get("/employees", (req, res) => {
  const verificationStatus = jsonwebtoken.verify(tokenValue, "secretString");
  if (verificationStatus.user == "user") {
    return res.status(200).json({ message: "access successful" });
  }
  return res;
});
```

### Express Best Practices

- Web frameworks such as Ruby on Rails, .NET, and Django have required directory structures for storing files. Express does not require a pre-defined directory structure for its applications.
- However, defining a directory structure in advance is usually a good idea because as the size of the application grows, it can be difficult to maintain otherwise.
- The following folders are conventionally used to store files. Within the project folder it is suggested you use the following directories: `node_modules`, `config`, `models`, `routes`, `views`, and `public`.
- The `node_modules` folder contains the application’s modules and packages. It is automatically created after running the “npm install” command.
- The `config` folder should contain configuration files such as database connection configuration, an environment variables file, and a credentials file containing the API keys for external services used by the application under development.
- The `models` folder contains the data models for the application. The files specify the type of datastore, such as relational or non-relational, and are defined by an object-relational mapping, or ORM, library.
- The `routes` folder is used to specify all of the routes for the different entities in different files. It should have one file for each logical set of routes, such as one file for one type of resource.
- The `views` folder contains template files. A template dynamically writes HTML, CSS, and JavaScript to send back to the client. This approach makes it easier to generate user-specific user interfaces.
- The `public` folder will contain all static content such as images, CSS, and JavaScript. It is often helpful to have a sub-folder for each type of content.
- The project folder should also contain a few files: app.js, routes.js, and package.json.
  - The app.js file is the main configuration file for your application.
  - A routes.js file is a central location to access all the routes in the application. This file requires or imports all the files in the routes folder and then exports them as a single module which is imported into the app.js file. This helps create a single point of entry for all the routes in the application.
  - The package.json file contains the metadata used to manage the project’s dependencies.
- Folder structure for an API: node_modules, config, models, and routes. And then the following files app.js, routes.js, and package.json.
- This table provides examples of HTTP routes for post, get, patch, and delete using the
- Another best practice is to black-box test your node.js REST APIs. Black-box testing means you test the code without looking at its internal structure. The system is tested as a whole without mocked or stubbed dependencies.
- Mocha, which is a JavaScript test framework that runs on Node.js, contains a simple module called SuperTest. SuperTest provides you with a way to test HTTP requests, which is exactly what you need when you want to black-box test REST APIs.
- And when your API needs to authenticate, it is best practice to use JSON Web Token, or JWT based stateless authentication. Since the REST APIs must be stateless, your authentication will need to be as well. Stateless authentication verifies users by supplying most of the session information, such as user properties, on the client side.
- The last best API practice is creating proper API documentation. The whole purpose of an API is so that someone else can use them, so you want to provide appropriate documentation for your Node.js REST API. Two open-source projects that you might find useful to create documentation for your APIs are `API Blueprint`, and `Swagger`.
- Regarding the use of node package manager,
  - use the `npm init` command when initializing a node.js project.
  - When using the npm install command to install dependencies, use the `-save` or the `-save-dev` attribute. This makes sure that if the application is moved to a different platform, the correct dependencies will be installed with it.
  - Never push a node modules repository.
  - always use npm to install.
- Use all lowercase for file names, use camel case for variables, and npm modules are named in lowercase, separated by dashes. And when using the require method for npm modules, use camel case.
