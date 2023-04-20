// How to modify a specific child
// START
const list = document.querySelector(".main-ul");

// // the following gives the node type
// list.nodeType;

// // lists the children
// list.children;

// // to select a specific children
const listItem = list.children.item(1);

// const listItem = list.children.item(1);
listItem.textContent = 'some new content';

list.appendChild(document.createElement('li'));
list.children.item(3).textContent = 'list added in JS'
//END 

// how to add before a particular tag
const pElement = document.querySelectorAll('p').item(1);
const parent = document.querySelector('.main-body');

const newP = document.createElement('p');
newP.textContent = "new paragraph added through JS";
parent.insertBefore(newP, pElement);