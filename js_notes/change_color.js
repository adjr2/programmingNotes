const html_body = document.querySelector('body');

const randomclickfunction = function() {
    const colour = ["#f8a3cc", "#7c9ff7", "#338cc7", "#ff7008"];

    const randomindex = Math.floor(Math.random() * colour.length);

    const randomcolour = colour[randomindex];

    html_body.style.backgroundColor = randomcolour;

    console.log("clicked this colour" + randomcolour);
}

// the following will change the colour wheneve it is called.
randomclickfunction()

// to make it change the colour every time user click:
html_body.onclick = randomclickfunction;