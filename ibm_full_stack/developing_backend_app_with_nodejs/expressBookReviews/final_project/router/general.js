const express = require("express");
let books = require("./booksdb.js");
let isValid = require("./auth_users.js").isValid;
let users = require("./auth_users.js").users;
const public_users = express.Router();

public_users.post("/register", (req, res) => {
  const username = req.body.username;
  const password = req.body.password;

  if (!username || !password) {
    res.status(404).json({ message: "Please provide username and password." });
  } else {
    if (!isValid(username)) {
      users.push({ username: username, password: password });
      res.status(201).json({ message: "username " + username + " added." });
    } else {
      res.status(404).json({ message: "Username already exists." });
    }
  }
});

function allBooks() {
  return new Promise((resolve, reject) => {
    resolve(books);
  });
}

public_users.get("/", function (req, res) {
  allBooks().then((books) => res.send(JSON.stringify(books)));
});

// Get book details based on ISBN
function getBooksByISBN(isbn) {
  return new Promise((resolve, reject) => {
    if (books[isbn]) {
      resolve(books[isbn]);
    } else {
      reject({ status: 404, message: "ISBN not found. " + isbn });
    }
  });
}

public_users.get("/isbn/:isbn", function (req, res) {
  getBooksByISBN(req.params.isbn).then(
    (isbnBooks) => res.send(isbnBooks),
    (err) => res.status(err.status).json({ message: err.message })
  );
});

// Get book details based on author
function getBooksByAuthor(author) {
  return new Promise((resolve, reject) => {
    for (let key in books) {
      if (books[key]["author"] === author) {
        resolve(books[key]);
      } else {
        continue;
      }
    }
    reject({ status: 404, message: "author not found. " + author });
  });
}

public_users.get("/author/:author", function (req, res) {
  const author = req.params.author;
  getBooksByAuthor(author).then(
    (authorBooks) => res.send(authorBooks),
    (err) => res.status(err.status).json({ message: err.message })
  );
});

// Get all books based on title

function getBooksByTitle(title) {
  return new Promise((resolve, reject) => {
    for (let key in books) {
      if (books[key]["title"] === title) {
        resolve(books[key]);
      } else {
        continue;
      }
    }
    reject({ status: 404, message: "title not found. " + title });
  });
}

public_users.get("/title/:title", function (req, res) {
  const title = req.params.title;
  getBooksByTitle(title).then(
    (titleBooks) => res.send(titleBooks),
    (err) => res.status(err.status).json({ message: err.message })
  );
});

//  Get book review

function getReview(isbn) {
  return new Promise((resolve, reject) => {
    if (books[isbn]) {
      resolve(books[isbn]["reviews"]);
    }
    reject({ status: 404, message: "ISBN not found. " + isbn });
  });
}

public_users.get("/review/:isbn", function (req, res) {
  const isbn = req.params.isbn;
  getReview(isbn).then(
    (review) => res.send(review),
    (err) => res.status(err.status).json({ message: err.message })
  );
});

module.exports.general = public_users;
