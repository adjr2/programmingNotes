## Week 1

### Twelve-Factor App Methodology

The twelve-factor app methodology is suited for Web-App (or SaaS).

Microservices are not a requirement for twelve-factor apps. However, microservices are often used in conjunction with the twelve-factor application methodology.

The twelve factors can be grouped into the _code_, _deploy_, and _operate_ phases of the software delivery lifecycle.

**Code phase**

- Factor 1: _Codebase_. You should always track the codebase for an application in a version control system, such as Git. There is a one-to-one relationship between a codebase and an app. An app should be contained in a single codebase. However, there will be multiple deploys, or instances, of the app. And while the codebase is the same across those deploys, different app versions can be present in each deployment. For example, dev or test environments can have changes that have yet to reach production.
- Factor 5: _Build, release, and run_. This phase demonstrates how a codebase becomes a production deployment. The build stage compiles the code, gathers dependencies, and then transforms the codebase into an executable unit called a build. The release stage combines the build with the deployment’s current configuration so that the code is ready to run. Then, the run stage implements the application. You should strictly separate these three stages. For example, the code should not be changeable at runtime, as that would prevent those changes from being included in the build stage.
- Factor 10: _dev/prod parity_. This factor minimizes the differences between development and production environments, which is necessary to enable continuous delivery to quickly promote changes into production. This action reduces the chance that code runs appropriately in one environment but not in another. Parity is particularly essential for backend services. If you use a MySQL database in production, you should use the same version of MySQL database in your development environments. Parity helps catch failures earlier in the development process.
- Factor 2: _Dependencies_. An app is only as reliable as its least reliable dependency. As a result, twelve-factor apps do not rely on the implicit existence of any packages, dependencies, or tools. You must explicitly declare all dependencies. This way, when a new developer grabs the codebase, there is no assumption that any dependencies already exist on their machine.

**Deploy phase**

- Factor 3: _Config_. The configuration is everything that can differ between deployments. Different databases are likely used in staging and production, so a developer should configure that database’s credentials and location per deployment. You should avoid storing configurations as constants since configurations might differ among environments. Store the config within environment variables, which are easy to change across deployments without changing the code.
- Factor 4: _Backend services_. A twelve-factor app should not distinguish between local and third-party services. Both should be accessible via a URL or other locator information along with any credentials so that a developer can easily swap out the backend service without changing the code. For example, if a database experiences problems, a new database can be spun up and substituted in without having to change code.
- Factor 6: _Processes_. An app executes in an environment as one or more processes. Processes should be stateless and share nothing. You should store persistent data in a backend service like a database since memory and filesystems aren’t shared across processes. If another process handles a subsequent transaction, the subsequent transaction won’t have access to data within the prior process. As a result, data needs to be centrally stored.
- Factor 7: _Port binding_. When you create a web-facing service, a web server should not be injected into an application at runtime. Instead, the web app should export HTTP by binding to a port and listening to incoming requests on that port. You can use port binding for HTTP and other services. Binding a port is generally done in the code by declaring a web server library as a dependency. Subsequently, because these apps are accessible via a URL, they can become backend services for other apps.

**Operate phase**

- Factor 8: _Concurrency_. An application runs concurrent processes to handle the increasing load. Since processes are stateless and share nothing, an application can start additional processes to scale horizontally and handle additional incoming requests without creating interdependencies among processes.
- Factor 9: _Disposability_. It specifies that application processes require minimal startup time and should end gracefully when terminated. Quick startup lets you quickly deploy changes to code or config. You can also easily scale apps because new deploys start quickly.
- Factor 11: dictates how to handle _logs_. Logs give visibility into application performance, so an app should not concern itself with storing logs. Instead, an application environment should handle logs as a stream of events written to standard output. The execution environment can capture the log streams for all running apps, aggregate them, and route them to their destination. This action is especially beneficial when the destination is a log analysis tool.
- Factor 12: _Admin processes_. Admin processes are one-off processes for managing an app, such as a database migration. Admin processes run against a release using the same codebase and config. Additionally, the application code should include admin processes so that they remain synchronized with the app.

### What are Microservices?

Microservices architecture is an approach in which a single application is composed of many loosely coupled and independently deployable smaller services. These services typically have their own technology stack, inclusive of the database and data management model. Teams can even choose different programming languages for different components as they are dependent on each other via an API endpoint. Microservices components communicate with one another over a combination of REST APIs, event streaming, and message brokers, and they are segregated and organized by business functionality, with the line separating services referred to as a bounded context.

Benefits:

- Since there is no interdependency between services, you can update code more easily to add new features or functionality without touching the entire application.
- Each team can choose its own technology stack which suits its needs and expertise to build components for which the team is responsible.
- And these components can be scaled independently of one another, reducing the waste and cost associated with having to scale entire applications because a single feature might be facing too much load.

Wherever you see scaling of microservices, it usually involves horizontal scaling. Horizontal scaling means scaling by adding more instances of resources, also described as “scaling out”. With microservices, individual services can be individually deployed and scaled.

An API call is often an effective way of initially establishing the state for a given service. However, it’s not a particularly effective way of staying up to date on progress. This is where _event streaming_ can help broadcast the state change, which helps in scaling the microservice by introducing this message broker.

### Comparison of Monolith vs SOA vs Microservices

A **monolithic application** has all or most of its functionality within a single process. And the application is managed in internal layers or libraries. The layers are tightly connected and dependent on each other. And this is where the benefits of a monolithic design lie; in its simplicity and less cross-cutting of features and functionalities since everything is in the same code base. However, over time, most products develop and increase in scope, and the design becomes more complex and difficult to modify. It also becomes a barrier to adapting to new technology which would mean re-writing the whole application.

A **Service Oriented Architecture (SOA)** is designed and built with a service provider and consumer approach. The services provided work as a discrete unit of functionality, integrated seamlessly, and are easily reused. Each SOA service consists of three components. The _interface_ defines how a service provider will execute requests from a service consumer, the _contract_ defines how the service provider and service consumer should interact, and the _implementation_ is the service code. The benefits of having these three separate components are that they help increase reliability and support parallel development due to a fixed contract between the services. However, due to these expectations and requirements, an SOA design can become complex and obstruct rapid application development. And the SOA design is an expensive investment, and therefore usually only suits enterprise teams, who can invest the required resources and expertise.

**Microservices architectures** comprise loosely coupled, reusable, and specialized components that often work independently of one another. And even the data in a microservice is not shared with other services, which helps you to scale individual microservices independently, and being independent also means you have the liberty to select the underlying technology. This architecture provides benefits such as ease of development, where you can define individual work units as a service. And since each service has a designated responsibility, you have the flexibility to add new technology. But while there is a compelling case for using microservices, there are some challenges associated with it too. The first one is the security aspect. Now that you have so many different services independently hosted, each will need its own security paradigm. And the second is that debugging and isolating issues can also become harder, since each service runs independently, meaning you may find it challenging to locate the root cause. Microservices architecture is an application-scoped concept. Like an E-commerce website.

### Microservices Patterns

Microservices have numerous patterns available that enable some of the more common challenges and opportunities. Examples are the _single-page application (or SPA) pattern_, the _Backend for Frontend (or BFF) pattern_, the _Strangler pattern_, and the _service discovery pattern_.

With the convergence of more powerful browsers, faster networks, and client-side languages, many web interfaces began incorporating all functionality into **single-page applications**. The user enters through one interface that never reloads the landing page or navigates away from that initial experience. Built using a combination of HTML, CSS, and JavaScript, these applications respond to user input through dynamic service calls to backend REST-based services that update portions of the screen instead of redirecting to an entirely new page. This application architecture often simplifies the front-end experience, with the tradeoff of more responsibility on the backend services.

While a single-page application works well for single-channel user experiences, it delivers poor results across user experiences through different channels, like mobile and web. A **Backend for Frontend** pattern inserts a layer between the user experience and the resources that the experience calls on. This design allows for customized user experiences between channels. For example, an app used on a desktop will have a different screen size, display, and performance limits than an app used on a mobile device. The BFF pattern allows developers to create and support one backend type per user interface using the best options for that interface rather than trying to support a generic backend that works with any interface but may negatively impact frontend performance.

The **Strangler pattern** helps manage the refactoring of a monolithic application in stages. The pattern gets its metaphorical name from the garden phenomenon of a vine that strangles a tree. Think of a web application built using individual URLs that map functionally to different aspects of a business domain. With the Strangler pattern, you use the structure of a web application to split an application into multiple functional domains and replace those domains with a new microservices-based implementation for one domain at a time. These two aspects form separate applications that exist side-by-side in the same URL space. Over time, the newly refactored application replaces the original application until finally, you can shut off the monolithic application. The Strangler Pattern includes these steps: First, _transform_. This creates a parallel new site on a cloud platform or within your existing environment. Next, _coexist_. This leaves the existing site functional and live for a specified time. It incrementally redirects from the current location to the new site for newly implemented functionality. And finally, _eliminate_. This removes the outdated functionality from the existing site or stops maintaining that functionality when you redirect traffic from the original site.

A **service discovery pattern** helps applications and services discover each other. This pattern is needed because, in a microservices architecture, service instances change dynamically due to scaling, upgrades, service failure, and even service termination. A load balancer could also use this pattern to do health checks and rebalance traffic on service failures.

Other patterns include

- **entity and aggregate pattern**, which could be used in an e-commerce site, where an order would be an aggregate of products grouped by a buyer.
- **adapter pattern**. Think of it in the way you think of plug adapters when traveling to another country. The purpose of adapter patterns is to help translate relationships between objects that are otherwise incompatible. For example, if you have integrated with a third-party API.

### Microservices Anti-Patterns

**Don’t build microservices**

- The first rule of microservices is don’t start with microservices. When you determine that the monolithic application's complexity negatively affects application development and maintenance, consider refactoring that application into smaller services.
- When the application becomes too large to update and maintain easily, these microservices will become ideal for breaking down the complexity and making the application more manageable.
- However, until you feel that pain, you don’t even have a monolith that needs refactoring.`

**Not taking automation seriously**

- If you have a monolith application, you only need to deploy one piece of software. Once you move to a microservices architecture, you will have more than one application with each having different code, test, and deploy cycles.

- Attempting to build microservices without either of the below is asking for a lot of unnecessary trouble:

1. proper deployment and monitoring automation, or
2. managed cloud services to support your now sprawling, heterogenous infrastructure

- So, when you are building microservices, always use DevOps or cloud services.

**Don’t build nanoservices**

- If you go too far with the micro in microservices, you could easily find yourself building nanoservices! The complexity of which will outweigh the overall gains of microservices architecture.
- Lean toward creating larger services and create smaller services when:

1. Deploying changes becomes difficult
2. The common data model becomes overly complex
3. Loading and scaling requirements no longer synchronize and affect application performance

**Don’t turn into SOA**

- The two concepts; microservices and service-oriented architecture (SOA) are often confused with one another because, at their most basic level, both build reusable individual components that can be consumed by other applications.
- However, microservices are fine-grained with independent data storage for each, that is, the bounded context.
- A microservices project that morphs into an SOA project will likely buckle under its own weight.

**Don’t build a gateway for each service**

- Instead of implementing end-user authentication, throttle, orchestrate, transform, route, and analytics in each service, you should use an API Gateway.
- An API gateway is an API management tool that sits between a client and your collection of backend services.
- This will become central to the above-mentioned non-functional concerns and will avoid re-engineering them with each service.

## Week 2

### What is REST?

**REST** stands for Representational State Transfer. REST APIs provide a flexible, lightweight way to integrate applications, and have emerged as the most common method for connecting components in microservices architectures. It is an architectural style that defines how applications should communicate with each other within a network.

An API has three characteristics that classify it as RESTful. It manages all requests through HTTP, It provides stateless, client-server communication, and it consists of a uniform interface between components.

REST APIs are stateless, meaning that each request contains all the information required to process it.
Each request from client to server must contain all of the information necessary to understand the request, and cannot take advantage of any stored context on the server. Session state is therefore kept entirely on the client.

The main benefit of RESTful APIs is the uniform interface, regardless of where the request originates. The REST API should ensure that the same piece of data, such as the product id, belongs to only one uniform resource identifier (or URI).

### Introduction to API Gateway

An **API Gateway** is an API management tool that sits between a client and a collection of backend services. It aggregates the various services required to fulfill them and returns the appropriate result.

Why do you use an API Gateway? An API Gateway can help you to protect your APIs from malicious usage or overuse. Thus, you can use an authentication service with rate limiting. It also helps to understand how your APIs are used, using an analytics and monitoring service. In addition, you can monetize your APIs using a billing system. A gateway also presents a single point of contact to your various microservices and provides a single response to a request. Finally, you can seamlessly add or remove APIs without the client’s knowledge about the services running at the back end.

So, how does a client access the microservices? This is a problem when you need to interact with multiple APIs. An API Gateway can remove this complication and allow you to: change hosts and their locations, increase or decrease the number of service instances, and replace your existing service, for example, an ordering service, with a new one. The client’s access to the services remains undisturbed.

The benefits of using an API Gateway are as follows: It insulates the clients from how the application is partitioned into microservices. In other words, it simplifies the client side by moving the logic for calling multiple services from the client to the API Gateway. It also provides the optimal API for each client, regardless of who the client is. It reduces the number of requests or round trips. For example, the API Gateway enables clients to retrieve data from multiple services with a single round trip. And irrespective of how your microservices communicate internally, an API Gateway will provide a standard protocol to communicate with the outside world.

Although an API Gateway provides many benefits, it also has some drawbacks. It’s another component that needs to be developed and maintained. In addition, if not designed carefully, it can become a single point of failure in an application. Also, a Gateway will increase the response time due to this additional network step in the execution of the application.

### Making API Requests using cURL and Postman

Transferring data to and from a server requires tools that support the necessary network protocols. Linux has multiple tools created for this purpose, the most popular being curl. curl, short for "Client URL” is a command line tool that enables data transfer over various network protocols.

### Documenting and Testing REST API with Swagger

Swagger saves time writing API documentation by running through the OpenAPI specification to ensure you meet the guidelines. Swagger allows you to describe the structure of your APIs so that machines can read them. With the API’s structure, Swagger automatically builds engaging UI and interactive API documentation. This structure is defined in a JSON or YAML file that adheres to OpenAPI specifications.

### Basics of GraphQL

**GraphQL** is a query language for your API. It provides a standard way to allow clients to request only the data that they need from the API. And it can be developed using any programming language, as it is language agnostic. GraphQL enables you to retrieve exactly what you need from the API. This means you don’t receive the data that you didn’t request. It also means you receive exactly what you require, even from different resources. Unlike the RESTful API, GraphQL requires just one endpoint to retrieve everything you require.

With REST, your APIs are the resources that provide endpoints to perform a particular operation using an HTTP method. In GraphQL, the types you define in the schema are the nodes. With REST, you make multiple calls and receive whatever is sent by the server. But in GraphQL, you only request and receive what you require. Extending your GraphQL API doesn’t need a new version; you add the new fields without breaking the existing clients, as they were only requesting what they required. A Query is used for querying your data, more like a GET request in a RESTful API. At its simplest, GraphQL makes requests for specific fields on objects. A mutation is used for manipulating and modifying your data. Every field in the mutation type can be thought of as a POST, PUT, or DELETE request in a RESTful API.

## Week 3

### Introduction to Serverless Computing

The Cloud Native Computing Foundation (or CNCF) defines **serverless** as "The concept of building and running applications that do not require server management. "It describes a finer-grained deployment model where applications, bundled as one or more functions, are uploaded to a platform and then executed, scaled, and billed in response to the exact demand needed at the moment." In other words, serverless computing offloads the responsibility of infrastructure management to cloud providers, enabling developers to focus on the application business logic.

Serverless computing exhibits the following characteristics:

- It is hostless, meaning developers do not have to procure, manage, and maintain servers.
- It’s elastic because autoscaling is immediate and inherent for serverless.
- It offers automated load balancing that distributes the incoming traffic across multiple backend systems.
- It is stateless, which results in faster performance and higher scalability.
- It’s event driven, meaning functions are triggered only when events occur.
- It provides high availability with no extra effort or cost.
- It is usage-based with granular billing.

To accomplish the goal of zero operational considerations,

- cloud providers take responsibility for routine infrastructure management and maintenance tasks such as maximizing compute, memory, and networking utilization while minimizing costs,
- providing server management that includes OS updates and security patches,
- enabling autoscaling,
- maintaining high availability,
- implementing security,
- configuring high performance (or low latency),
- setting up monitoring and logging.

In the IaaS model,

- you manage: OS, Middleware, Runtime, Data and Application
- cloud provider manages: Virtualization, Servers, Storage, and Network.

In the PaaS model,

- you manage: Application and Data
- cloud provider manages: OS, Middleware, Runtime, Virtualization, Servers, Storage, and Network.

In the Serverless model,

- you manage: only the Application layer
- cloud provider manages the remaining layers.

In the SaaS model,

- cloud provider manages the entire stack.

### Introduction to the FaaS Model

**Function-as-a-Service** or FaaS, is a type of cloud-computing service that allows you to execute code in response to events without the complex infrastructure typically associated with building and launching microservices applications.

FaaS includes the following characteristics:

- It is a subset of serverless computing.
- It creates applications in the form of multiple functions where a function is a piece of software written in any programming language.
- FaaS can be deployed on hybrid clouds as well as on-premises environments.
- It is stateless but can maintain state using external caches.
- Functions execute in milliseconds and process individual requests in parallel, thus making them instantaneously scalable.
- It is lightweight and uses the decoupling architecture mechanism.
- FaaS is billed on the time taken to run functions and not on server instance sizes.

Benefits of FaaS:

- With FaaS, you can divide the server into functions that can be scaled automatically and independently so you don’t have to manage infrastructure. This allows you to focus on the app code that reduces time-to-market.
- One of the biggest benefits of the FaaS model is the cost. You pay only when an action occurs. When the action is complete, everything stops—no code runs, no server idles, and no costs are incurred.
- Since the functions are stateless, small and independent pieces of code, they can be scaled automatically, independently, and instantaneously, as required. If demand drops, they automatically scale back down.
- FaaS offers inherent high availability because it is spread across regions and availability zones and can be deployed without incremental costs.

A serverless stack comprises of _three main components_, namely: Functions-as-a-service or FaaS, Backend-as-a-service or BaaS, and an API Gateway. Let's look at how the components in a serverless stack work. Event requests are received from different channels like an HTTP request, webhooks from repositories such as Github and Docker Hub, and scheduled jobs. These requests go through the API Gateway which identifies and forwards them to the respective functions. The functions then process these requests, and they are further directed (if necessary) toward the backend services (such as file and object storage, block storage, notification services, and so on) for further processing and/or storage. The output or response is then sent back to the client through the FaaS component and the API Gateway.

FaaS functions should be designed to do a single piece of work in response to an event. So, make your code scope limited, efficient, and lightweight so that functions load and execute quickly. The value of FaaS is in the isolation of functions. Too many functions will increase your costs and remove the value of the isolation of your functions. Using too many third-party libraries can slow down the initialization of a function and make them harder to scale.

Some of the common managed FaaS providers are: AWS Lambda from Amazon, Google Cloud functions, Azure functions from Microsoft, Cloud functions by IBM, OpenShift Cloud Functions from Red Hat, and a few others like Netlify, Oracle, and Twilio. There are many self-managed FaaS choices available too if you don’t want to depend on third-party managed platforms. These include: Fission, which is a framework for serverless functions on Kubernetes, Fn Project, a container-native serverless platform, Knative, a Kubernetes-based platform to build, deploy, and manage serverless workload, and OpenFaaS, which allows you to turn any Linux or Windows process into a function.

### The Serverless Framework

The Serverless Framework is a free and open-source web framework written using Node.js.

**Serverless Framework** is a command line interface or CLI that offers structure, automation and best practices out-of-the-box, allowing you to focus on building sophisticated, event-driven, serverless architectures, comprising of functions, events, resources, and services.

A **function** is merely code, deployed in the cloud, that is most often written to perform a single task. Each function is an independent unit of execution and deployment, like a microservice. Functions are triggered by events, and events come from other resources, for example: An HTTP request on an API Gateway URL or a new file uploaded in an S3 bucket.

A **task** can be saving a user to the database or performing a job at a specified time.

**Resources** are infrastructure components which your functions use, such as a database provided to you as a service by your cloud provider, or an S3 bucket to store files.

A **service** is the Framework's unit of organization. You can think of it as a project file, though you can have multiple services for a single application. A service is configured via a _serverless.yml_ file where you define your functions, events and resources to deploy. When deploying with the Framework CLI, everything in the configuration file is deployed at once.

### Serverless Reference Architecture and Use Cases

The use cases for serverless web applications are Event streaming, Post-processing, and Multi-language.

## Week 4

If you choose to self-host your microservices, you need to make detailed adjustments and tackle many non-trivial challenges carefully.

- First, you need to deliberately configure and build your microservices to make them production-ready, including necessary assets like library dependencies, resources, credentials, and so on.
- Then compile and build them into one executable binary to run on hosting environments.
- Next, you need to carefully choose the infrastructure to run your microservices, such as web servers, operating systems, networks, databases, and so on.

Your team needs to select from numerous options carefully.

- Since your microservices undergo fluctuating traffic, you will need to scale up or down dynamically. For example, e-commerce websites will always have peak traffic on holidays that can decrease significantly after several days or a week.
- In most cases, you will need to deploy multiple related microservices that work and communicate.
- The communication among the microservices needs to be reliable and secure.
- Activities like logging, monitoring, and working on dashboards are also required to ensure all microservices are stable and any production issues are identifiable or even foreseen.
- There can be other challenges of self-hosting which are dependent and specific to the implementation and build of the microservices.

For Python-based microservices, there are two main types of interfaces available:

- **Web Server Gateway Interface, or WSGI**, is the main Python standard for communication between web servers and web applications or microservices. It supports synchronous service calls only. There are many popular WSGI web servers, such as Green Unicorn and uWSGI.
- **Asynchronous Server Gateway Interface, or ASGI**. The main difference from WSGI is that it supports asynchronous code so that your microservice can be called asynchronously. Some popular ASGI web servers are Daphne and Hypercorn.

IBM Cloud Code Engine has three main use cases or deployment modes.

- The first use case involves deploying a built application to Code Engine. An application here may represent a microservice, a web app, or a console app.
- The second use case is pushing the source code directly. The Code Engine can build your application from source code, either from a remote repository like GitHub repo or your local workspace. The built application can then be automatically deployed without worrying about the building process, which is convenient and time-saving.
- The third use case is creating and running batch jobs like a data processing or analytics task. For example, if one of your microservices needs to analyze results, you can deploy a batch job to perform the analytics tasks on the same platform. So, all your deployed microservices and jobs can work seamlessly together because they are all hosted within the same infrastructure.

### Project, Application, Build, and Jobs

The term **project** in Code Engine represents a group that contains and manages its resources and entities. A grouping in Code Engine contains entities such as build, app, job, and certificate for Transport Layer Service (or TLS) HTTPs connections, and so on. One important function of a _project_ is providing a namespace for its entities. A _namespace_ provides a mechanism for isolating groups of entities and resources within a single group. Names of entities need to be unique within a namespace, but not across namespaces. Another important function is managing resources and providing access control.

In Code Engine, your code will run the application. Like regular deployed web applications, your running application can serve HTTP requests or provide REST APIs. In addition to traditional HTTP requests, Code Engine also supports applications that use WebSockets. A **WebSocket** is a communication protocol based on Transmission Control Protocol (or TCP). It is mostly used for long-running and session-based communication between clients and servers, such as a chat application.

In the Code Engine context, a **build**, or image build, is a mechanism you can use to create a container image from your source code. A container image includes every asset that a container needs to run, such as executable source code, dependencies, resources, container engines, system libraries, configuration settings, and so on. The Code Engine supports building from a _Dockerfile_, which is a text file that includes all the commands to build a docker container image. Alternatively, it can use a Cloud Native Buildpack. A _buildpack_ is another popular way to build the container image. It contains executables to perform tasks such as inspecting source code, creating a build plan, or executing the build plan to produce an image. After your container image is built from the source code, you can deploy your built container image to the Code Engine and create an application accordingly.

A **job** is a one-time execution of your code. Like an application, a job runs executable code. Depending on the workload, the Code Engine will create one or more instances of a job. Unlike applications, which primarily handle HTTP requests or WebSocket sessions, jobs are designed to run one time and exit. Before you run a job in the Code Engine, you can specify workload configurations that are used each time the job runs. Some typical jobs are: Data processing jobs to query and transform data in batches, machine learning model training jobs, reporting jobs to generate reports based on a preset schedule, and billing jobs to create and send bills.

### Updating Deployed Applications

You have the following four common scenarios for updating your code engine applications: update environment variables such as database location or secret key; update application visibility, such as changing the URL of an application from public to private or project-only; update your application's image reference or GitHub repo; or update the runtime resources of your application.

When you deploy your application, it is assigned with two types of URLs: internal and external. Internal URLs help to communicate with other applications within your application. External URLs can be public, external, or IBM private network only. The selection of the type of URL defines the visibility of your application.
