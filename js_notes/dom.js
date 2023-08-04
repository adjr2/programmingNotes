// const elementNode = document.createElement('p');
// const textNode = document.createTextNode('Content');
// const attributeNode = document.createAttribute('class');

// elementNode.appendChild(textNode);
// attributeNode.value = 'some-class';

// elementNode.setAttributeNode(attributeNode);

// document.body.appendChild(elementNode);

// document.querySelector('button');
// document.querySelector('.btn-1');
// document.querySelector('#my-btn');

// document.getElementById('btn-1');
// document.getElementsByClassName('my-btn');

const btn = document.querySelector('#btn-1');

function addParagraph () {
    // the following will work in console only
    // console.log("the button is working"); 

    const randomNum = Math.floor(Math.random() * 100);
    const pContent = 'The random number is: ' + randomNum;

    const elementNode = document.createElement('p');
    elementNode.textContent = pContent;
    document.body.appendChild(elementNode);
    // const attributeNode = document.createAttribute('class');
    // elementNode.appendChild(textNode);
}

// btn.addEventListener('click', addParagraph);
btn.onclick = addParagraph;