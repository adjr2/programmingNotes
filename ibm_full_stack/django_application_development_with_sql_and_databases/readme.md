## Week 1

### Introduction to Data and Databases

A **database** is a collection of data or information designed for the input, storage, search and retrieval and modification of data. And a **database management system**, or DBMS, is a set of programs that creates and maintains the database. It allows you to store, modify and extract information from the database using a function called querying.

There are different types of databases. Several factors influence the choice of database, such as

- the data type and structure,
- querying mechanisms,
- latency requirements,
- transaction speeds,
- intended use of the data.

**Relational databases** (RDBMSs) build on the organizational principles of flat files, with data organized into a tabular format with rows and columns. Following a well-defined structure and schema, however, unlike flat files, RDBMSs are optimized for data operations and querying involving many tables and much larger data volumes. Structured query language (SQL) is the standard querying language for relational databases.

**Non-relational databases** (NoSQL, not only SQL) emerged in response to the volume, diversity and speed at which data is being generated today. Mainly influenced by advances in cloud computing, the internet of things, and social media proliferation. Built for speed, flexibility and scale, non-relational databases made it possible to store data in a schema-less or free form fashion, NoSQL is widely used for processing big data.

### Relational Databases

A relational database is a collection of data organized into a table structure where the tables can be linked or related, based on data common to each. Tables are made of rows and columns, where rows are the records and the columns the attributes.

One of the most significant advantages of the Relational Database Approach is its ability to create meaningful information by joining tables.

Some of its other advantages include

- Flexibility: using SQL, you can add new columns, add new tables, rename relations, and make other changes while the database is running and queries are happening.
- Reduced redundancy: Relational databases minimize data redundancy.
- Ease of backup and disaster recovery: Relational databases offer easy export and import options, making backup and restore easy. Exports can happen while the database is running, making restore on failure easy. Cloud-Based Relational Databases do continuous mirroring, which means the loss of data on restore can be measured in seconds or less.
- **ACID** compliance. ACID stands for atomicity, consistency, isolation and durability. ACID compliance implies that the data in the database remains accurate and consistent despite failures and database transactions are processed reliably.

Use cases for relational databases:

- Online Transaction Processing OLTP applications are focused on transaction oriented tasks that run at high rates.
- Data Warehouses. In a data warehousing environment, relational databases can be optimized for online analytical processing or OLAP, where historical data is analyzed for business intelligence.
- IoT Solutions Internet of Things, or IoT solutions require speed as well as the ability to collect and process data from edge devices, which need a lightweight database solution.

Limitations of RDBMS.

- RDBMS does not work well with semi structured or unstructured data and is therefore not suitable for extensive analytics on such data.
- For migration between two RDBMS, schemas and type of data need to be identical between the source and destination tables.
- Relational databases have a limit on the length of data fields, which means if you try to enter more information into a field than it can accommodate, the information will not be stored.

### Non-relational Databases

Based on the model being used for storing data, there are four common types of NoSQL databases:

- **Key value store**, data in a key value database is stored as a collection of key value pairs. The key represents an attribute of the data and is a unique identifier. Both keys and values can be anything from simple integers or strings to complex JSON documents. Key value stores are great for storing user session data and user preferences, making real time recommendations and targeted advertising, and in-memory data caching. However, if you want to be able to query the data on specific data value, need relationships between data values, or need to have multiple unique keys, a key value store may not be the best fit. Redis, Memcached and DynamoDB are some well known examples in this category.
- **Document based** store each record and its associated data within a single document. They enable flexible indexing, powerful ad hoc queries, and analytics over collections of documents. Document databases are preferable for ecommerce platforms, medical records, storage, CRM platforms, and analytics platforms. However, if you're looking to run complex search queries and multi operation transactions, a document based database may not be the best option for you. MongoDB, DocumentDB, CouchDB, and Cloudant are some of the popular document based databases.
- **Column based** models store data in cells grouped as columns of data instead of rows. A logical grouping of columns, that is columns that are usually accessed together is called a column family. For example, a customer's name and profile information will most likely be accessed together, but not their purchase history, so customer name and profile information data can be grouped into a column family. Since column databases store all cells corresponding to a column as a continuous disk entry, accessing and searching the data becomes very fast. Column databases can be great for systems that require heavy write requests, storing time series data, weather data, and IoT data. But if you need to use complex queries or change your querying patterns frequently, this may not be the best option for you. The most popular column databases are Cassandra and HBase.
- **Graph based** databases use a graphical model to represent and store data. They are particularly useful for visualizing, analyzing, and finding connections between different pieces of data. The circles are nodes and they contain the data, the arrows represent relationships. Graph databases are an excellent choice for working with connected data, which is data that contains lots of interconnected relationships. Graph databases are great for social networks, real time product recommendations, network diagrams, fraud detection, and access management. But if you want to process high volumes of transactions, it may not be the best choice for you because graph databases are not optimized for large volume analytics queries. Neo4J and CosmosDB are some of the more popular graph databases.

The primary advantage of NoSQL is its ability to handle large volumes of structured, semi structured, and unstructured data. Some of its other advantages include the

- ability to run as distributed systems scaled across multiple data centers, which enables them to take advantage of cloud computing infrastructure.
- efficient and cost effective scale-out architecture that provides additional capacity and performance with the addition of new nodes and simpler design, better control over availability and improved scalability that enables you to be more agile, more flexible, and to iterate more quickly.

### Relational Data Concepts

The **relational model** is the most used data model for databases because this model allows for data independence. Data is stored in a simple data structure, Tables. This provides logical data independence, physical data independence, and physical storage independence.

An **entity relationship data model**, or ER data model, is an alternative to a relational data model. Using a simplified library database as an example, this figure shows an entity relationship diagram or ERD that represents entities called tables and their relationships.

An **entity relationship model** proposes thinking of a database as a collection of entities rather than being used as a model on its own. The ER model is used as a tool to design relational databases.

In the ER model, entities are objects that exist independently of any other entities in the database. The building blocks of an ER diagram are entities and attributes. An **entity** can be a noun: person, place, or thing. In an ER diagram, an entity is drawn as a rectangle. Entities have attributes which are the data elements that characterize the entity. **Attributes** tell us more about the entity. In an ER diagram, attributes are drawn as ovals.

The **primary key** of a relational table uniquely identifies each tuple or row in a table, preventing duplication of data and providing a way of defining relationships between tables. Tables can also contain **foreign keys** which are primary keys defined in other tables, creating a link between the tables.

## Week 2

### Introduction to Django

Django's **Object Relational Mapping (ORM)** layer, lets you define your data modules using python classes.

Django promotes an architecture where each web server instance operates independently known as the share nothing or stateless. Architecture each web server, instance handles requests and responses autonomously without relying on shared resources or maintains any server-side state between requests.

Django web framework make scaling easy because the Django app is stateless it manages your user sessions. This allows developers to add more instances of an application and transfer the user's experience across the models without losing data.

### Object-Oriented Analysis and Design

**Object oriented analysis and design (OOAD)** for short, is an approach for analyzing and designing a software system when the system will use object oriented programming languages to develop it.

At the heart of OOAD are objects. Objects contain data and they also have behaviors that prescribe the actions the object can take.

The generic version of an object is called a class.

OOAD is used for a system that can be broken down into objects that interact with each other.

**Class diagrams** are commonly used to communicate a software system structure in OOAD. The class diagram shows how the class is in an object oriented design relate to one another. Each box represents a class and shows its attributes.

### Reading: ORM Tools

**Object-Relational Mapping (ORM)** tools are widely used in modern software development to bridge the gap between object-oriented programming languages and relational databases.

### Object-Relational Mapping (ORM)

Software developers often use a database as the main data repository for their application, so they need to integrate SQL into their application code. SQL statements must be assembled in application code and executed in the database system using database APIs. The retrieved database rows are returned to application code as **Cursor**, a special control data structure for iterating over rows in a database.

**OOP models** entities using classes, objects, and attributes, whereas **SQL models** entities using tables, rows, and columns. Also, OOP models relationships using class patterns like inheritance, association, and aggregation, whereas SQL models relationships using JOIN and FOREIGN KEY. Lastly, OOP performs CRUD on data using methods, whereas SQL performs CRUD on data using data manipulation language, like the SQL statements insert, delete, and update.

The main reason people invented object-relational mapping was to bridge the gap between OOP and SQL and make it possible to use OOP languages to access databases. ORM libraries or tools can map and transfer data stored in a relational database as rows into objects or objects into rows.

Like all third-party software libraries, ORM has its pros and cons.

- Positive: With ORM, your class designs define the databases. For OOP application development, you just need to define classes and create objects. You can use databases without writing SQL. Also, you can use a single ORM interface to manage multiple database systems without worrying about differences in SQL syntax. All these benefits will speed up your application delivery.
- Negative: SQL and OOP are still two different languages with different modeling concepts, and ORM may fail to perform the mapping of objects into database tables. Also, since ORM combines data access logic with application code, any database change will require changes to both the application logic and the data access logic. Because ORM hides the implementation details, debugging can be challenging. Finally, ORM may reduce application performance. ORM adds an extra translation layer, but it cannot guarantee that the translated SQL statements are optimized.

### Django Model

In Django ORM, each Django model maps to a database table. When you create a class object, it represents a table row. Each field represents a table column. Schema and tables are automatically generated once model classes are defined. For example, we can define a User class, which is a subclass of the Django model. Django will then create a corresponding User table in the database by generating “table create” statements and creating columns based on the class fields.

Each field in a model should be defined as a Field class. Django maps each field to a column type.

Django ORM supports common relationships such as One-To-One, Many-To-One, and Many-To-Many.

Model inheritance in Django is like inheritance in Python. You need to determine if the parents are just holders of common information that will only be visible through the child models, or if parents should have their own tables. There are three scenarios for model inheritance: Use multi-table mode when you’re subclassing an existing model and want each model to have its own database table. Use abstract base classes if the parent class will just hold information. Use proxy models to modify the Python-level behavior of a model without changing fields.

### Related Objects

The Django Model provides a convenient API to read or manipulate related objects. Django only requires you to define the relationship on one side, called a forward or explicit relationship.

When you define a forward relationship, Django will automatically create a backward or implicit relationship based on the type of forward relationship you have defined.

“on delete” options specify what happens to related objects when an object is deleted.

## Week 3

### Django Model-View-Template (MVT) Pattern

The **MVC** design pattern divides application logic into three components. _Model_ accesses and manipulates data but does not present data. Model may have database interfaces such as SQL or ORM, or it may use business logic to process raw data. _View_ presents data in various forms, such as visual elements in a webpage, a mobile app user interface, or as JSON/XML format. _Controller_ coordinates between Model and View. It routes requests, processes input, requests data CRUD from Model, and updates View.

When a client application sends a request with inputs to Controller, Controller routes the request, validates and processes the input, sends CRUD requests to Model, and forwards data to View to be presented. In the Django framework implementation, there is no explicit Controller. Instead, the Django server itself performs this function. Django Model manages data modelling and database mapping as well as business logic to process data. Django View describes which data is presented, but not how it is presented. Typically, view delegates to a template, which describes how the data is presented.

When a client sends a request, the Django server routes the request to the appropriate view based on the Django URL configuration. Thus, Django follows a **Model-View-Template (MVT)**, design pattern.

### Django Admin

Django framework has a clear separation between content publishers and users. Django provides a built-in admin site to manage content.

Django Admin site is very powerful and easy to use for site managers to manage content. The look and functions can also be customized.

## Week 4

### Class-based and Generic Class Views

Whether a view is built using **function-based views** or **class-based views**, a view is essentially a Python function or callable. The main issue with the function-based view is it is normally very hard to extend or customize. To address these issues, the class-based view was created.

The only difference is that for the view argument you need to specify the `as_view` function (eg: `views.SomeView.as_view()`).
The as_view function is inherited from the View base class. The Django View class is the base class for all class-based views. The Django View class defines an as_view method, which also defines an inner_view method and will be returned as a callable. So, when we add them to the URLconf using the view.as_view class method, it returns a function.

To speed up development and solve common tasks, Django provides some built-in view classes called **generic-based views** for developers to reuse and extend with minimal code changes.

Pros and Cons:

- For the function-based view, the main pros are that it’s simple to write code and easy to understand. You can explicitly write your logic without following any extra structure or designs such as the methods defined in View base class. If you have a very specific function that’s not likely to be reused, the function-based view could be your choice. The main cons are that function-based views are difficult to extend or reuse. And they handle http request methods using conditional statements, which may increase the code complexity.
- For Class-based views, the pros include reusability and extendibility. Also, you can handle requests using class methods. And you can leverage the generic class-based views to solve common tasks. The main cons for class-based views are that adding the extra View base class inheritance makes the code harder to read. Implicit code is hidden, and developers must check the source code to understand exactly how the views are implemented.

### Django Authentication System

User authorization in Django is managed mainly by three models: User, Permission, and Group. We explained the User model in authentication. The Permission model has many-to-many relationships with User to store the types of objects and how users can access them. The Group model provides a convenient way to manage users with the same permissions. The easiest way to manage permissions and groups is with Django admin site, but you can also choose to manage them programmatically using APIs.

In Django, you can create and assign permissions to each model you have defined. The four default permissions are: View, Add, Change, and Delete.

### Deploy Your Django Apps

To deploy Dependable scalable and maintainable Django apps, you need to deploy them on web servers. Since most web servers such as Apache, HTTP and Nginx are not written in Python, Django apps need extra interfaces to talk to web servers supporting those interfaces.

The **web server Gateway Interface (WSGI)**, is the main python standard for communicating between web servers and applications. It supports synchronous code only. The start project command line will create a wsgi.py file, declaring an application callable, by default to make Django at work with wsgi, WSGI servers will try to find this application callable and use it as an entry point to communicate with your Django app. Some popular wsgi web servers are available for Django apps. Such as Gunicorn, uWSGI, Apache, and mod_wsgi.

The Django app supports the **asynchronous server Gateway Interface**, another web server interface. The main difference from wsgi is it supports asynchronous code. The start project command line, creates a asgi.py file, declaring an application. callable to work with the asgi web server. Popular asgi web servers are Daphne, Hypercorn, and Uvicorn.

Follow the following best practices and Implement various configurations to ensure scalability security and reliability, use the production database.

- In production, It's recommended to use a robust and scalable database. Like PostgreSQL, MySQL, or another suitable, relational database. Avoid using SQLite in production as it's not designed for high concurrency or heavy traffic.
- Secure database credentials. Store your database credentials and other sensitive information and environment variables, and never hard code them.
- Use HTTPS for secure communication between the server, your hosted Django app, and clients - your users accessing it in the browser.
- Static and media files. Use a cloud storage service or content delivery network, or CDN to efficiently serve static files like CSS or JavaScript and user-uploaded media files to reduce server load.
- Load balancing. With Django being stateless, make the most of it and consider using a load balancer to distribute, incoming traffic across multiple instances of your Django app ensuring that our performance and high availability.
- Horizontal scaling. Design your app to scale horizontally, adding more instances or containers as traffic increases.
- Monitoring and logging. Setup error monitoring and logging services to track and diagnose issues.
