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