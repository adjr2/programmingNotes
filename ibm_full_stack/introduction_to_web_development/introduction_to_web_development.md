## Week 1
### Overview of Web and Cloud Development
- Content displayed by websites can contain elements that are either previously stored on the server (called “static”) or generated each time they are requested by the client (called “dynamic”). Dynamic elements can involve information coming from other systems and applications, such as databases.
- Cloud Applications are similar to Websites in that they request content that a server returns. Cloud Apps are built to work seamlessly with a Cloud-based back-end infrastructure, Cloud-based data storage and data processing, and other Cloud services, making them very scalable and very resilient.
- The front-end deals with everything that happens at the client-side – everything the user can see and interact with.
- The back-end deals with everything that happens on the server before the code and data are sent to the client. The back-end coding usually handles the logic and functionality that make the website or app work, and the authentication processes that keep data secure.

### Learning Front-End Development
-  CSS is also used to create websites that have cross browser compatibility which means that they are compatible with multiple browsers and multiple devices such as PC, mobile devices, iPads etc.
- Syntactically Awesome Style Sheets (SASS) called SAAS. It is an extension of CSS that is compatible with all versions of CSS. SASS enables you to use things like variables, nested rules, and inline imports to keep things organized. SAAS allows you to create style sheets faster and more easily.
- Learner Style Sheets (LESS) or LESS. LESS enhances CSS, adding more styles and functions. It is backwards compatible with CSS. Less.js is a JavaScript tool that converts the LESS styles to CSS styles.
- Reactive or adaptive websites display the version of the website designed for a specific screen size. Responsive design of a website means that it will automatically resize to the device it is being accessed from.
-  Angular framework: an open-source framework and is being maintained by Google. Angular frameworks allow websites to render the HTML pages quickly and efficiently. It has built-in tools for routing and form validation. 
- React.js has been developed and maintained by Facebook. It is a JavaScript library that builds and renders components for a web page. It is not a complete suite of tools. For example, routing is not a part of this framework and will need to be added using a third-party tool. React.js only helps build and drop components into a page. 
- Vue.js is maintained by the community and its main focus is the view layer which includes user interface, buttons, and visual components. It is flexible, scalable and integrates well with other frameworks. It is very adaptable. It can be a library, or it can be the framework.

### Introducting Application Development
- Frameworks define the workflow that you must follow, unlike libraries, which allow you to call functions as and when required. When using a framework, it can sometimes feel like you, as a developer, are not in full control of the development process. This sense of the framework and its predefined workflow controlling the development process is referred to as inversion of control.

### More Application Development Tools
- Tools that can help in app development:
    - CI/CD
    - Build Tools
    - Packages
    - Package Managers

- CI/CD refers to continuous integration and either continuous delivery or continuous deployment. CI/CD enables developers to deliver frequent changes reliably. Implemented through a build-automation server, Continuous Integration (CI) ensures that all the code components work together smoothly. A CI build environment enables you to integrate newly developed code frequently, depending on how quickly the project changes. Continuous delivery (CD) begins where CI ends. The CI process automatically builds and tests your code, then CD deploys all code changes in a build to a testing or staging environment.
- A build tool transforms your source code into the binaries needed for installation. Build tools organize your source code, set compile flags, and manage dependencies. They are most important in environments where there are many inter-connected projects, with multiple developers contributing to each project. In these environments, it can be very difficult to keep track of what changes were made, in what order, what dependencies exist, and what needs to be incorporated in the next build, so automation is key to keeping everything running smoothly. Build automation can automate a wide variety of tasks that developers do in their day-to-day activities like: 
    - Downloading dependencies. 
    - Compiling source code into binary code. 
    - Packaging that binary code. 
    - Running tests. 
    - And deployment to production systems.
- You can initiate a build from the command line or from an IDE. There are two categories of Build Tools widely in use: 
    - Build-automation utilities, which generate build artifacts like executables, by compiling and linking source code. 
    - Build-automation servers, which execute build-automation utilities on a scheduled or triggered basis.
- Some examples of build tools are: 
    - Webpack – a module bundler for JavaScript. 
    - Babel – a JavaScript compiler. 
    - And Web Assembly - a binary instruction format that runs in your browser.

- The app needs to be simple and trouble-free for the user to install, so a commonly used technique is to collect all the necessary files and bundle them together into a package. Packages are archive files that contain the app files, instructions for installation, and any metadata that you choose. They have their own metadata too, including the package description, package version, and any dependencies, like other packages that need to be installed beforehand.
- Once you have bundled your app into a package, you can use a package manager to distribute it. Package managers take care of the tasks of finding, installing, maintaining or uninstalling. software packages at the user's request.
- Package management systems: 
    - Coordinate with file archivers to extract package archives. 
    - Verify checksums and digital certificates to ensure the integrity and authenticity of the package. 
    - Locate, download, install, or update existing software from a software repository. 
    - And manage dependencies to ensure a package is installed with all packages it requires.
- Some commonly used package managers for each of the major platforms are listed here: 
    - On Linux - Debian Package Management System (DPKG). 
    - Red Hat Package Manager (RPM). 
    - On Windows - Chocolatey. 
    - On Android - Package Manager. 
    - On MacOS - Homebrew and MacPorts.
- Here are some examples of package managers for popular languages: 
    - For Node.js/Javascript - npm. 
    - For Java - Gradle and Maven. 
    - For Ruby - RubyGems. 
    - For Python - Pip and Conda.

### Importanct of Back-End Development
- A front-end developer creates websites and Cloud applications, using HTML, CSS, and JavaScript to create what the user sees and interacts with in the client software. A back-end developer creates and manages all the resources that are needed to respond to the requests that the user makes through the client. The back-end developer’s tasks focus on enabling the server infrastructure, or back-end, to process requests, supply data, and provide other services securely.
- Back-end developers use APIs, routes, and endpoints to process incoming requests: An API is code that works with data, usually using JSON or XML. APIs have set rules and structure. A route is a path to a website or page that the user interacts with. Routes generally take user input and show results based on the input. An endpoint may be an API or may simply be a path. When a request from the front-end arrives at the back-end, it is routed to the correct service. If the backend has an end point defined for the request by using routing, the request will be addressed and replied to. If the end point is missing, the server returns a 404 error. Back-end developers must create and maintain this server-side routing. Along with backend APIs, routes effectively allow the front-end client to plug into the correct socket at the back-end. APIs provide a mechanism for Cloud apps, mobile apps, and other types of software to access resources from the back-end.
- To help handle requests from databases, back-end developers can use object-relational mapping tools (ORM) to connect to the database and retrieve the correct data.

## Week 2
### Introduction to HTML
- HTML Elements are the building blocks of an HTML page. The pieces of content that form the page are assigned labels such as “paragraph,” “list,” and “table”. They are represented by tags. Browsers do not display the tags but use them to render the content.
- The World Wide Web Consortium (W3C) made a number of recommendations to the HTML standards over the years. Initially, the Web Hypertext Application Technology Working Group (WHATWG) worked on recommendations independently. Then, in 2007, W3C formed a working group chartered to work with the WHATWG on the development of the HTML5 specification.
- The HTML5 specification, as drafted by W3C, includes the following objectives: 
    - The HTML5 specification defines a single language called HTML5 that can be written in HTML or XML syntax. 
    - The HTML5 specification defines a processing model that can interoperate with earlier HTML implementations. 
    - HTML5 improves the markup for documents. HTML5 includes markup and APIs for idioms, such as web storage, video, and audio content.

### HTML Features
- HTML5 features? 
    - It provides the means to categorize web pages into different sections, and includes tools for effective data management, drawing, video, and audio. 
    - Facilitates the development of cross-browser applications for the web and portable devices. 
    - Allows greater flexibility, permitting the development of exciting and interactive websites. 
    - Helps to create a more engaging user experience. 
    - Pages that are designed by using HTML5 can provide an experience similar to desktop applications. 
    - Allows for enhanced, multiple-platform development by combining the capability of an application programming interface (API). 
    - By using HTML5, developers can create a modern application experience that is uniform across platforms and devices.
- The !DOCTYPE is a declaration tag that represents the document type. The !DOCTYPE declaration is not an HTML tag; it is an instruction to the web browser about what version of HTML the page is written in. Although this declaration is not required, it should be the first line of the HTML code if the developer decides to include it.
- The html tag is the root element of this tree. It contains all of the other HTML elements, except the !doctype tag.
- The head element can contain the following tags: title, scripts, style, style sheet links, meta information, browser support information and other initialization functions.
- The body tag contains all content that is displayed on the webpage.
- HTML user agents, commonly known as browsers, parse the markup, turning it into a DOM (Document Object Model) tree. A DOM tree is an in-memory representation of a document. DOM trees contain several kinds of nodes, which include a DOCTYPE node, elements such as headers and paragraphs, text nodes, and comment nodes.
- Extensible Markup Language (XML) documents look similar to HTML documents, except they have an XML tag on the first line. In addition, with XML documents, the Content-type must be specified as an XML media type such as application or xml.
- How do you decide whether to use HTML or XHTML for developing web pages? 
    - Both HTML and XHTML use the same semantic or tags. However, XHTML tags all need to be in lowercase, while the case used does not matter in HTML. In addition, XHTML must be well-formed. Every element must have an end tag. All attributes must have a value and double or single quotation marks must surround all attribute values. If an XML parser encounters a situation where the syntax is not well-formed, it stops processing. In HTML, different case, unmatched quotation marks, and non-terminated and uncontained elements are allowed and commonplace. In this regard, HTML syntax is less rigorous than XHTML syntax.

### HTML Management and Support
- Key themes of the HTML5 specification. 
    - The syntax it defines is compatible with HTML4 and XHTML1 documents. 
    - HTML5 is defined in a way that it is compatible with earlier versions in the way browsers handle deployed content. 
    - It separates conformance requirements for user agents and authors. In other words, how browsers treat HTML5 code and how page authors treat HTML5 code is different. For user agents, HTML5 is defined in a way that supports elements and attributes of the earlier specifications. For authors, several elements and attributes have been removed in order to simplify the language. 
    - HTML5 includes some elements and application programming interfaces that help in the creation of web applications. Examples include video and audio elements, and an API that supports the creation of offline applications.
- What do you think makes HTML suitable for creating web applications? There are a number of possible reasons: 
    - The range of devices that all have built-in browsers that support HTML5 features. 
    - The number of APIs that enhance the user experience, such as the advanced animation, drawings, audio, and video elements. 
    - The efficient use of HTML and CSS, while reducing the number of images, can lead to faster load times for rendering web pages. 
    - Search engine optimizations can use keywords that are taken from HTML attributes to improve the visibility of a website when search results are displayed. The meta tags shown are used to provide information to search engines.
- New structural elements are part of the HTML5 specification. 
    - New APIs such as canvas, audio, and video help with graphics and embedded content. 
     -New attributes were added to the input element attributes. Examples include the email, datetime, and number types. The browser automatically validates the input field according to the input attribute, without the need for custom validation scripts. 
     - By using web storage APIs, you can store data in the browser. The web workers feature can be used for non-interactive processing. 
     - Web workers provide a way to run processing-intensive tasks without blocking the user interactions to the current page.

### HTML Scripting
- The use of scripting within a website, often through the use of JavaScript, can be done directly within your HTML code within the `script` tag, or within a separate file which is called in your HTML code. Scripting provides a more interactive user experience when browsing websites. It can be used for various tasks, such as form validation, dynamically changing the content of a website, and manipulating images.
- Since scripting can be turned off, the recommendation is to use scripting but not to rely on it. Scripting is enabled for a browser context when the conditions shown on the slide are true.
    - The browser in use supports scripting and the user has scripting enabled. 
    - HTML5 also defines a sandboxed media type which specifies an extra set of content restrictions and can be used when hosting untrusted content. This sandboxed browsing context can be set at the page level or specified as an attribute for embedded objects.
- Running a page that contains an embedded object without the sandbox attribute grants the embedded object the same permissions as the rest of your page. This implicitly gives a third-party vendors permission to run scripts with the same permissions that you have for that page, which is one way that you can inadvertently allow advertisements to occur in your application. So, to prevent granting implicit permissions to embedded objects, use the sandbox attribute on any tag that contains an embedded object.
- Each HTML document that is loaded into a browser page becomes a Document object. The Document object provides access to all HTML elements in a page and can be accessed from within a script. The DOM tree accessors are HTML document APIs that provide access to all the HTML elements on a page. The property to access is prefixed by the word document. For example, `document.head` returns the first head element that is a child of the html element, if there is one, otherwise null. The function `document.images` returns an HTMLCollection of the image elements in the document. The function `document.scripts` returns an HTMLCollection of the script elements in the document. Here are some common HTML DOM tree methods:
    - The document.getElementById(‘id’) function has one required parameter which is the id of the element you want to access. The id is specified as an attribute on one of the elements that is coded elsewhere on the page. 
    - The document.getElementsByTagName(‘tag’) function has one required parameter which is the tag name of the element you want to access. This function returns a nodelist of all the elements with the tag that matches the required parameter.

### HTML5 Browser Support
- Not all browsers fully support all the features that are described in the HTML5 and CSS3 specifications.
- You can also use JavaScript to check whether a certain HTML5 element is supported by a browser. First, create a DOM element by typing document.createElement() and include the element type as a parameter argument. As a result, the DOM object gets created. If the browser does not support that element, the DOM object that gets created has a set of common properties, but nothing specific for that element. You then test for a known property or method on the DOM object that you created. If that property or method does not exist, then the browser does not yet fully support the DOM element (or the HTML5 tag) that has been created. Browsers that do not support the element can revert to a fallback or default behavior such as displaying the field as a regular text field.