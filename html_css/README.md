## HTML Notes

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

- The `body` tag contains what one sees on the webpage whereas `head` tag contains non-printing information (the meta-deta).
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

- Printing special characters; example:

```html
<p>Less than &lt;</p>
<p>Greater than &gt;</p>
<p>Ampersand &amp;</p>
<p>etc</p>
```

- HTML Links
- One of the key thigs about HTML is making a set of pages and making "hypertext" links amongst those pages.
- Links are what make the "web" a "web" - it is a web of interlinked documents.
- The `anchor` tag is used to create the links which has `href` ("hypertext reference").

```html
<!-- The following is an Absolute Reference -->
<a href="http://www.google.com">Google</a>
<!-- The following is an Relative Reference; used to move on the same server -->
<a href="index.html">Second Page</a>
```

- The spacing and new lines don't matter in HTML. To print exactly how you have written use the `pre` tag.

## CSS Notes

- It is not sequential. However, the order does matter because what comes later has more importance.
- To add a separate CSS file to the HTML file:

```html
<head>
  <title>Including CSS From a File</title>
  <link type="text/css" rel="stylesheet" href="rules.css" />
</head>
```

- All the old tags come with styling built in them. Therefore, new tags were created that had no styling whatsoever. Example: `span` and `div`. The main difference is that `div` is a [**block element**](https://en.wikipedia.org/wiki/HTML_element#Block_elements) whereas `span` is an [**inline element**](https://en.wikipedia.org/wiki/HTML_element#Inline_elements). This means that to use them semantically, divs should be used to wrap sections of a document, while spans should be used to wrap small portions of text, images, etc. It is illegal to place a block-level element within an inline element:

```html
<!-- Illegal -->
<div>
  Some
  <span
    >text that
    <div>I want</div>
    to mark</span
  >
  up
</div>
```

- `p` tags have spacing around them which is not there for `div` and `span`.
- A **Class** (`.`) name can be used by multiple HTML elements, while an **ID** (`#`) name must only be used by one HTML element within the page. The following shows that multiple definitions can form one definition:

```html
<style>
  .loud {
    color: red;
  }
  .shout {
    text-transform: uppercase;
  }
  #extra p {
    color: blue;
  }
</style>
<body>
  <p class="loud">Loud</p>
  <p class="shout">Shout</p>
  <p class="loud shout">Loud Shout!</p>
  <div id="extra">
    <p>Extra</p>
  </div>
</body>
```

- The `#extra p` only transforms the `p` tag in the `div extra`.
- `em` is the height of the current font.
- `padding` is around the text; `margin` is around the block/tag.
- Use `em` wherever possible instead of `px` value because `em` will take care of zooming. Also use `overflow = scroll` in case character overflows the block (or if you have put data in a box).
- `position: relative` (or `absolute`): the tag moves with the scroll bar; `position: fixed`: the tag stays at the fixed position (may be useful for navigation bar).
- `z-index` sets which tags will be shown on top in case multiple tags overlap.
