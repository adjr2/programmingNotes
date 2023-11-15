## Week 1

### Overview of Web and Cloud Development

- Content displayed by websites can contain elements that are either previously stored on the server (called “static”) or generated each time they are requested by the client (called “dynamic”). Dynamic elements can involve information coming from other systems and applications, such as databases.
- Cloud Applications are similar to Websites in that they request content that a server returns. Cloud Apps are built to work seamlessly with a Cloud-based back-end infrastructure, Cloud-based data storage and data processing, and other Cloud services, making them very scalable and very resilient.
- The front-end deals with everything that happens at the client-side – everything the user can see and interact with.
- The back-end deals with everything that happens on the server before the code and data are sent to the client. The back-end coding usually handles the logic and functionality that make the website or app work, and the authentication processes that keep data secure.

### Learning Front-End Development

- CSS is also used to create websites that have cross browser compatibility which means that they are compatible with multiple browsers and multiple devices such as PC, mobile devices, iPads etc.
- Syntactically Awesome Style Sheets (SASS) called SAAS. It is an extension of CSS that is compatible with all versions of CSS. SASS enables you to use things like variables, nested rules, and inline imports to keep things organized. SAAS allows you to create style sheets faster and more easily.
- Learner Style Sheets (LESS) or LESS. LESS enhances CSS, adding more styles and functions. It is backwards compatible with CSS. Less.js is a JavaScript tool that converts the LESS styles to CSS styles.
- Reactive or adaptive websites display the version of the website designed for a specific screen size. Responsive design of a website means that it will automatically resize to the device it is being accessed from.
- Angular framework: an open-source framework and is being maintained by Google. Angular frameworks allow websites to render the HTML pages quickly and efficiently. It has built-in tools for routing and form validation.
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

## Week 3

### HTML5 Tags and Structural Elements

- Tags provide control within an HTML5 document.
- Some tags provide structural elements: The div tag separates areas in a document into divisions, enabling you to apply different styles to different parts of a document. Dedicated elements like article, section, header, and footer are more specific than the generic div element. The aside, figure and figcaption tags enable you to group content. And the nav tags enable you to group navigational links.

### HTML5 Input Element: Attributes for the Input Tag

- The input type="color" / attribute allows the user to select a color. The dialog varies depending on the browser.
- The input type="date" attribute is a date control (year, month, day) with no time zone.
- The datetime-local attribute provides input for a date and time (year, month, day, hour, minute, AM/PM) with no time zone.
- The input type="email" attribute is displayed as a regular text input field. It provides feedback when the input does not follow the email format.
- The input type="number" takes a numeric value as input. You can optionally specify the minimum, maximum values, step size, etc.
- The input type="range" takes a numeric range as input. Only the numbers in the range of the minimum and the maximum are available for selection. The range attribute displays a slider with a range of values between the minimum and maximum. Only the slider itself is shown. Additional JavaScript code is needed in order to display the value of the slider.
- The differences between input type="search" / and input type="text" / are mostly in style.
- The input type="tel" pattern="[parameters]" attribute expects a telephone number as input. On its own, the input type="tel" provides nothing more than a text entry field in the browsers. It does not enforce numeric only input since many telephone numbers include other characters, such as the plus sign and hyphens. You need to supply your own pattern matcher if you want the browser to validate the telephone number.
- The URL attribute is used to validate that the user typed in a properly formatted URL or web address.
- The input list="some_list" uses the datalist feature. Not to be confused with the select element. The datalist options are only suggestions. Useful for auto-complete functionality. You can fill the list by nesting <option> elements inside the datalist tag.
- Placeholder text is used to provide hints of what the input text format looks like. The placeholder fills the input text field with the example values in a lighter shade of text. The form does not submit the placeholder text value if the input text is not overwritten.
- The required attribute implies that some text must be typed.
- What happens if browser-based validation is not supported for these input attributes? There are several options to performing validation in browsers that do not support all HTML5 input attributes. You can use JavaScript and JQuery libraries. You can assume that more browsers will support these features over time, and leave all final validation to server-side processing. You can code client-side validation that is attached to the form submit event handler to validate all the fields on the form when the form is submitted.

### CSS: Styling HTML

- CSS is the design that is layered over the top of an HTML web page CSS is a style sheet language that describes how HTML elements are displayed.
- The data is sent to the browser by using HTML, and the design is applied to that data by using a CSS.
- Generally, follow these guidelines: When a color is specified, use Red-Green-Blue (RGB) hexadecimal light values. When a size is specified, use pixels (indicated by a px after the number); an em, which is indicated by em after the number (that is, the size of the font multiplied by the specified number); or a percentage, which is indicated by a % after the number. Text can be aligned left, right, or center. Floats can also be left or right. Vertical alignments must be top, middle, or bottom. Fonts can be any specific font or font family (serif, sans-serif, or monospace) or even a downloadable font.
- One of the most important decisions you must make when you are determining the design of your website is whether to use a fluid or a fixed layout: A fluid layout: is a layout in which the height and width of elements is flexible and can expand or contract based on the browser window, the operating system, and other user preferences. You specify these elements mostly by using percentages and ems. A fixed layout: is a layout where you specify the height and width of elements, and those values remain the same regardless of which operating system or browser you use to access the website. You specify these elements mostly by using pixels.
- Applying CSS to HTML:
  - Inline CSS: This is used for a single HTML element; insert the "style" attribute inside any HTML element.
  - Internal CSS: `<style>` tag must be used, with your CSS code inside.
  - External CSS: To use this method, the `<link>` tag must be added to the `<head>` tag section
- All three methods can be used and follows the order of precedence: inline (high) >> Internal >> External (low)

### CSS Frameworks

- There are two types of CSS frameworks: utility frameworks and component frameworks.
- Using no framework at all and just using plain CSS (also called Vanilla CSS) requires you to write all the styling on your own. This gives you the freedom to style everything exactly as you want it, but also requires a lot of time and effort, as you must style every component. An alternative to this is to use a utility framework, which gives you “utility” classes that scope to a single CSS property. This makes it easier to apply CSS properties directly in your HTML code, which can save a lot of time while still giving you the freedom to style components as you wish. Component frameworks provide you with pre-styled components and templates which are easy to add to any website. This requires little knowledge of CSS and makes it easy to keep consistent styles, but also limits you to only the components made available by the framework.
- Utility-first frameworks provide you with an easy way to reference CSS properties. These typically come in the form of classes, called utility classes, which scope to single-purpose CSS classes. Instead of having to write out the entire CSS property, utility-first frameworks allow you to use a property by referencing its corresponding class within the “class” attribute of your desired HTML element. For example, instead of using the “text-align: center;” CSS property in your code, a utility-first framework might have a self-descriptive class, such as “text-center”, which does the same thing when added to the ”class” attribute of an HTML element. They make it easy to be consistent with color choices, spacing, typography, shadows, and everything else that makes up a well-engineered design system. However, having these styles mixed into your HTML classes reduces the separations of concern within your code, making your HTML markup more verbose. Since utility-first frameworks involve adding many classes to your HTML markup, this often causes the download size of your markup to increase, and potentially slows down your web pages. A popular utility-first CSS framework used today is Tailwind CSS.
- Component frameworks provide pre-styled components which can be easily added to your code. This results in the ability to develop well-styled websites rapidly, as significantly less time needs to be spent styling each element. It also makes it easier to keep all related elements styled uniformly, as you can simply choose the same or similar styles each time. However, having all these pre-defined styles limits you only to what the framework provides, and doesn’t give you the freedom of customizing everything exactly as you want it. They also provide a lot of overhead code that you wouldn’t otherwise get if you choose not to use any frameworks, as component frameworks will often provide you with more components than what you’ll use. One of the most popular component CSS frameworks in use today is called Bootstrap.

## Week 4

### JavaScript Language: Overview and Syntax

- JavaScript is a scripting language that is derived from the ECMAScript standard and originally designed to run on the Netscape Navigator browser.
- When a JavaScript interpreter is embedded in a browser, the result is the ability to create dynamic web pages: JavaScript adds behavior to otherwise static web content.
- JavaScript code acts on the document object model that the web browser generates.
- One of the ways that server programming and browser scripting work together is in an architecture that is called Ajax, or Asynchronous JavaScript and XML. The term "Ajax" encompasses more than asynchronous server calls through JavaScript and XML. Ajax represents a series of techniques that provide richer, interactive web applications through HTML, JavaScript, Cascading style sheets, and modifying the web page through the Document Object Model.
- In JavaScript, there are five primitive types that are associated with various primitive values:
  - Number: All numbers, such as 0 or 3.1412. The number primitive represents both integer and floating point values, the value NaN (not a number), and Infinity. All numbers in JavaScript are represented internally as double precision or 64 bit floating point numbers.
  - String: All strings, such as “Hello World”,
  - Boolean: The values true or false,
  - Null: The value null.
  - Undefined: The value undefined, since a data type has not been assigned or the variable does not exist.
- All other non-primitive data types are objects.
- The primitive types number, string, and boolean can be wrapped by their object counterparts. Wrapper objects have the same name as the primitive type, except they start with an uppercase letter. JavaScript provides built-in ways to convert between these wrapper objects and primitive values. The wrapper objects use special methods such as the valueOf and toString methods to convert between objects and primitive literals.
- The typeof keyword in JavaScript is used to find out the data type of the supplied operand.
- The keyword new is used to create the String wrapper object. This object can be converted to a primitive string type by calling the valueOf function on the object wrapper class.
- Arrays are specialized collection objects that aid the programmer in the storage and retrieval of data by indexed keys. Arrays use a zero-based indexing scheme. When declaring an array with a constructor, you use the new array keywords and specify the array elements as parameters of the new array. Array literals are created by declaring the array elements within square brackets. You then assign the array to a variable. (array constructor and array literal are fundamentally similar)
- The Date object is a specialized object that is used to hold the date and time. The constructor for a date object is in the format: new Date ([with optional parameters]). If you create a Date object without any parameters, JavaScript returns an object that contains the current local date and time. If you send this date object to the console or try to display the date object on a web page, JavaScript automatically applies a toString method to the object.
- The error object instance includes two properties that contain information about the error:
  - The message property contains a description about the error.
  - The name property identifies the type of error such as a RangeError.
- Besides a generic error, there are six other core errors types in JavaScript:
  - TypeError
  - RangeError
  - URIError
  - EvalError
  - ReferenceError
  - SyntaxError
- message in the parameter field.

### JavaScript: Variables and Control

- Variables in JavaScript are declared with the ‘var’ keyword, followed by the variable name. Since JavaScript is a loosely-typed language, you do not need to declare the data type of a variable.
- If a variable is not assigned a value, then the variable value is undefined.
- Variables declared without the var keyword have a global scope. Variables that are not initialized have a value of undefined.​
- Unlike Java, there is no block statement scope in JavaScript. Having no block statement scope means that variables declared inside one IF condition can be used outside the scope of that condition.

### JavaScript: Functions and Prototypes

```javascript
function Car(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
    this.getName() = function () {
        return this.make + ' ' + this.model + ' ' + this.year;
    }
}

var c = new Car("Meridian", "Saber GT", 2012);
alert(c.getName()); // displays "Meridian Saber GT 2012"
```

- In the Car function, the keyword "this" refers to the current instance of the Car object that is being created. In other words, an instance of Car that is associated with the variable named c. Using the "this" keyword can differentiate whether you are referring to the global or local instance of a variable. The use of "model" in this example refers to the argument that was passed into the function, while the use of "this.model" refers to the global "model" variable associated to this instance of the Car object.
- Prototypes allow you to easily define properties and methods for all instances of a particular object. All JavaScript objects which can be created with the "new" keyword inherit properties and methods from a "prototype". For example, the "Car" object we created previously inherits the make, model, and year properties from the constructor function, which are implicitly defined in the Car prototype. When a car object is created, that object inherits all the properties and methods that are defined by this prototype. Unlike objects, the methods and properties of prototypes can be changed with one call. If you want to add a new property to an object's constructor function, for example, you must add it to the function directly by adding it as an additional argument. It cannot be done simply by calling the object itself. With a prototype, however, it is possible to add a property or method with just one call. Since all objects have a prototype property, this is an easier way to add properties and functions to objects.

```javascript
function Car(make, model, year, color) {
  this.make = make;
  this.model = model;
  this.year = year;
  this.color = color;
}

// prototype
Car.prototype.color = "Red";
```

- Any object that gets instantiated inherits the current state of the prototype. If a prototype changes, all objects using it will automatically inherit the new properties and functions within that prototype. One way to change a prototype is via a script, which can override prototype properties and functions.

```javascript
// adding functions to prototypes
function Car(make, model, year) {
  this.make = make;
  this.model = model;
  this.year = year;
}

Car.prototype.getName = function () {
  return this.make + " " + this.model + " " + this.year;
};
```

- All existing instances of the Car object also inherit the getName method.
- Auto-invocation or self-executing functions start running immediately after being declared. The functions and variables inside self-executing functions are only available to the code inside the self-executing function. Auto-invocation functions can also be unnamed or anonymous functions and have the format that is shown in the code block on the slide. Self-executing functions are often used to initialize data or to declare DOM elements on the page.

```javascript
(function () {
  //statements
})();
```

### JavaScript APIs

- To retrieve a node reference for an element of a document given an id, use the document.getElementById function and pass the id value as an argument.
- The getElementsByTagName function retrieves a NodeList of elements with a specified tag name. The NodeList contains an array of elements in your document.

```javascript
var imgSet = document.getElementsByTagName("img");
var output = "";

for (var i = 0; i < imgSet.length; i++) {
  output += "<p>Source for image ";
  output += i;
  output += ": ";
  output += imgSet[i].src;
  output += "</p>";
}
document.write(output);
```

- You can use the DOM API function document.createElement(TagName) to create an element in the current document. After creating the element, you can use any number of functions to place the element in the appropriate location within the document. Examples of these functions include the insertBefore, appendChild, or replaceChild function that can be used to add the newly created element into the document.

```html
<head>
  <script>
    function addPara() {
      var newPara = document.createElement("p");
      var newText = document.createTextNode("Hello World!");
      newPara.appendChild(newText);
      document.body.appendChild(newPara);
    }
  </script>
</head>
<body onload="addPara()"></body>
```

- The function element.innerHTML retrieves or sets the contents of an HTML element. The innerHTML property returns all child elements as a text string. With the element.innerHTML function, you can change the contents of an HTML element, by setting it to a text string that can include HTML tags. Setting the innerHTML value of an element to a string removes all of the current child elements. The browser then parses the string and sets the contents of the HTML element.

- You can use the element.style method to retrieve or set the inline CSS style for a particular element. If you use element.style to set the style of an element, it overrides any setting from a CSS style sheet with one specific style. The way to set the style in JavaScript is with the format element.style.propertyName = value. In contrast, the element.setAttribute('style', …) wipes out all previously set inline CSS styles.

```html
<div id="div1" style="color: blue"></div>
<script>
  var div1 = document.getElementById("div1");
  div1.style.color = "red";
</script>
```

- The function element.setAttribute with parameters(attrName, attrValue) dynamically modifies the attribute of an element.

```js
document.getElementById("theImage").setAttribute("src", "another.gif");
```

- The function element.removeAttribute(attrName) removes an attribute from an element. The function element.getAttribute(attrName) retrieves the value of the specified attribute in the element, if it exists.

- To open a new browser window, use the window.open() function. This method returns a reference to the new window object. You can use this reference later to close the window, with the reference_name followed by the close() function. The parameters of the window.open function are: URL - A string that indicates the location of the web page to be displayed in the new window. You can pass an empty string if you are going to write some script-generated content to the new window in the current URL context. Name - A string that specifies the name of the window. Features - An optional string that specifies the features of the window, such as its placement and dimensions. The features string is a comma-separated list of name-value pairs. Replace – An optional boolean value. If true, the new location replaces the current page in the browser history.

```js
window.open(url, name, [features, replace]);
```

- The window.onload function can be used to start a function after the page is loaded. The function, window.dump("message") writes a string into the console for the web browser. The dump() function is a less intrusive way to display diagnostic information than the alert() method. Finally, the window.scrollTo(x-value, y-value) scrolls the web browser to a particular set of coordinates on a page.

```html
<script>
    onload = (function () {
        addPara();
    })();
    function addPara () {
        var newPara = document.createElement("p");
        newPara.innerHTML = "Hello World!";
        document.body.appendChild(newPara);
    }
```

- The Document Object Model (DOM) API is one of the most basic JavaScript APIs available. It connects web pages to scripts by representing the structure of a document (e.g. an HTML web page) in memory, making it accessible for modfication as required.

### Client-Side JavaScript: with HTML

- A client-side script is a program that accompanies an HTML document or might be embedded directly in the HTML document itself. The script program runs on the client device when the document loads, or at some other time such as when a link is activated or when a button is clicked.
- Although JavaScript is widely used as a scripting language in HTML, other scripting languages can be used instead.
- Scripts offer authors a means to modify and extend HTML documents in highly interactive ways. Scripts can run after an HTML document is loaded. Scripts can be used to validate forms or to process input as it is typed. Scripts can be triggered by events that occur on a web page, such as the clicking of a button. Scripts can be used to dynamically create document elements on an HTML page.

- Some users who visit your website might disable JavaScript from running, or they might be using a browser that does not support scripting. To allow for these situations, place the content for the alternative path within the noscript tag. If the browser does not support scripting, the browser runs the section of code that is within the noscript tag.
- Scripts can run on the detection of certain events that happen when the page is running in a browser session. Calling a function when an event occurs is called event binding. For example, the onload event can run a script when the browser finishes loading a page. Or a function can be performed when the onclick event occurs.

```html
<!-- Example of event binding in scripts -->
<button type="button" onclick="showAnswers()">
  Show Solution
  <script>
    function showAnswers() {
      //
      alert("A");
    }
  </script>
</button>
```

### Client-Side JavaScript: with DOM

- The document object model is the programming interface between HTML or XHTML and JavaScript. The Document Object Model (DOM) is a browser-based interface for applications and scripts to dynamically access and update the content, structure, and style of documents. JavaScript uses the DOM to access and modify web page elements in the web browser.
- Here is a representation of the basic DOM model for browsers. The window object is at the top of the DOM hierarchy and controls the environment that contains the document. The history object keeps internal details about the recent history of pages in the browser. The history object has methods for letting you simulate clicking the back or forward buttons in a browser. The location object contains information about the URL of a page. The navigator is an object representation of the client Internet browser or user agent. There is no standard that applies to the navigator object, so the property values returned when running queries on the navigator object are not consistent across browsers. The screen object is used to derive information about a user's screen, such as the dimensions of the display screen. The screen object is useful for determining the screen size of browser windows that run on mobile devices. The document object provides access to all HTML elements within a page. Each HTML document that gets loaded into a window becomes a document object.
- The window object is the outermost global container of all the objects in the DOM hierarchy. When the browser loads a page, a window object is automatically created for you. You can then access the window object properties and functions from your JavaScript code. In client-side JavaScript, the Window object serves as the global object and everything in the DOM takes place in a window.
- A number of predefined methods exist for the window object. The window.alert, window.confirm, and window.prompt dialogs that are used in web pages, come from the global window object. You can leave out the window prefix for methods in the DOM API. So the window.alert method can be coded more simply as alert with a message argument.
- There are two types of nodes in the W3C DOM, element nodes and text nodes. All HTML tags (html, head, meta, title, and body) are element nodes. The nodes that contain actual text that go between an element start tag and end tag, are text nodes.

### JavaScript DOM Objects

- The W3C DOM level 2 defines 12 different types of nodes, seven of which have direct applicability in HTML documents.
  - Element
  - Attribute
  - Text
  - Comment
  - Document
  - Document Type
  - Fragment
- For example, if you are looking at a DIV element, the node name is DIV. If the DIV element has an attribute like id=div123, then the attribute name is “id” and the attribute value is “div123”, which is the name-value pair.
- Another example: If a paragraph element is followed by some text, the text string has a node name of #text, and the node value is the text string itself.
