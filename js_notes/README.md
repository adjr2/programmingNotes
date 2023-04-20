# JavaScript notes

#### I am following a YT video [Frontend Web Development Bootcamp Course (JavaScript, HTML, CSS)](https://www.youtube.com/watch?v=zJSY8tbf_ys)

#### How to change the background colour of a webpage everytime user clicks?

- Read the codes of `change_color.js`.

### Variable and Data Type

- The following the declarationa and assignment of the variable. The value stored in this variable can't be changed later in the program.

```js
const firstvariable = "hello world";
console.log(firstvariable);
```

- The following first declare and then assign a value to a variable. Unlike `const`, variables declared using `let` can be changed later.

```js
let secondvariable;
secondvariable = 10;
// let secondvariable = 10; is also valid.
console.log(secondvariable);
```

- Another way of declaring and assigning variable is using `var` keyword. However, it has a problem:

```js
var thirdvariable = 10;
var thirdvariable = 20; // this doesn't throw error which is problematic.
```

- The following called an **object** declaration in JS and `obj1` and `obj2` are called property. `.` is used to access the properties:

```js
const firstobject = { obj1: 1, obj2: "asd" };
firstobject.obj1;
//another way to access the property
firstobject["obj1"];
```

#### Comparison Operators

- The `===` is a comparison operators which compare both the value and the type of the variables being compared.

```js
const result1 = 20 === 20;
// true
```

- The `==` compares just the value and not the type of the variables being compared. It converts the value of one variable.

```js
const stringValue = "10";
const numberValue = 10;
stringValue == numberValue;
// true
stringValue === numberValue;
// false
```

- However, the operators don't work with objects and arrays. Use library `lodash` for comparing arrays and objects.

```js
const firstArray = [1, 2, 3, 4];
const secondArray = [1, 2, 3, 4];
firstArray == secondArray;
//false and same for ===

const firstObj = { a: 1, b: 2 };
const secondObj = { a: 1, b: 2 };
firstObj == secondObj;
// false and same for ===
```

#### Conditional Statement

- The following is the syntax:

```js
if (...){
    ...;
} else if (...) {
    ...;
} else {
    ...;
}
```

```js
switch (...) {
    case ...:
        ...;
        break;
    default:
        ...;
}
```

#### Loops

- The following is the syntax:

```js
for (let i = 0; i < condition; i++) {
    ...;
}
```

#### Function

- The following is the syntax:

```js
function firstFunction () {
    ...;
}

function_name();
//or
const firstFunction = function () {
    ...;
}
// or
const arrowFunction = () => {
    ...;
}
```

- The following is a syntax to declare and invoke the function at the same time:

```js
(function anotherFunction() {
    ...;
}) ();
```

#### Callback Function

- The following is an example to understand the callback function concept:

```js
function myCallback(someNumber) {
  return someNumber * 2;
}

function mainFunction(randomNumber, shouldCall, callback) {
  let result = randomNumber;
  if (shouldCall) {
    result = callback(randomNumber);
  }
  return result;
}
mainFunction(20, true, myCallback); // 40

// another way to call the mainFunction
mainFunction(20, true, (num) => {
  return num * 20;
});

// further simplification
mainFunction(20, true, (num) => num * 2); // paranthesis around num are not required as well.
// 40
```

- Why to use Callback Functions?

  - Reusability

  ```js
  const arr = [1, 2, 3, 4, 5];
  arr.map((x) => x ** 2);
  // [1, 4, 9, 16, 25]
  ```

  - Asynchronous programming: meaning code that doesn't run immediately.

#### Primitive vs Object

- The following example explains the difference:

```js
// here String is a class and we are instantiating an object of this class. The keyword new is need to create an object.
const firstString = new String("hello world");

// here just declaring a string. However, in the background secondString will also be an object as well (like everything else in JS).
const secondString = "hello world";
```

# HTML Notes

- The following is the basic structure of the `html` file:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>

    <!-- This connects your CSS stylesheet -->
    <link rel="stylesheet" href="css/styles.css" />
  </head>
  <body>
    <!-- The is where most of the HTML goes -->

    <!-- This connects your JS to the HTML -->
    <script src="js/scripts.js"></script>
  </body>
</html>
```

- The `body` tag contains what one sees on the webpage.
- Two important things about HTML code: **Tags** and **Attributes**.

```html
<p class="...">...</p>
<!-- in the example, 'p' is a tag and the class is an attribute. -->
```

- Some examples of tags:

```html
<!-- Normal tags -->
<p></p>
<h1></h1>
<div></div>
<span></span>
<strong></strong>

<!-- self closing tags -->
<img />
<input />
<meta />
<link />
```

- The different between self closing tags and normal tags is that one can put other tags in normal tags.

```html
<!-- the following is valid -->
<div>
  <p></p>
</div>
<!-- The following is not valid (can render though) -->
<img <p></p>/>
```

- The type of attributes:
  - Global attribute: available to any HTML element.
  - Element specific attribute.

# DOM

- Document Object Model (DOM) is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as nodes and objects. A web page is a document that can be either displayed in the browser window or as the HTML source. In both cases, it is the same document but the Document Object Model (DOM) representation allows it to be manipulated. As an object-oriented representation of the web page, it can be modified with a scripting language such as JavaScript.

- When you create a script, whether inline in a `<script>` element or included in the web page, you can immediately begin using the API for the `document` or `window` objects to manipulate the document itself, or any of the various elements in the web page (the descendant elements of the document).

- Different ways to find particular tag:

```js
// selects the first button tag it founds
document.querySelector("button");

// . is used with class attribute
document.querySelector(".btn-1");

// # is used with id attribute
document.querySelector("#my-btn");

// specifically getting the elements by id or class
document.getElementById("btn-1");
document.getElementsByClassName("my-btn");
```

- Ways to register an event (here click event):

```js
// first way:
const btn = document.querySelector("#btn-1");

function addParagraph() {}

btn.addEventListener("click", addParagraph);
```

```js
//second way
const btn = document.querySelector("#btn-1");

function addParagraph() {}

btn.onclick = addParagraph;
```

```html
<!-- in html, third way -->
<button id="btn-1" class="my-btn" onclick="addParagraph()">CLICK ME</button>
<!-- with addParagraph defined in js -->
```

- Ways to select the elements and their children:

```js
const list = document.querySelector("ul");

// the following gives the node type
list.nodeType;

// lists the children
list.children;

// to select a specific children
list.children.item(1);
```
