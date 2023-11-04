## Cloud Computing

### Week 1

#### Introduction to Cloud Computing

Why Cloud Computing:

- Flexibility and Scalability: better than local hosting of the server.
- A business model with the latest trends: no need of costly update to the IT infrastructure.
- Availability: can be accessed from anywhere.

Definition: a model for enabling convenient, on-demand network access to a shared pool of configurable computing resources that can be rapidly provisioned and released with minimal management effort or service provider interaction. Example of computing resources: networks, servers, storage, application, and services.

This Cloud model is composed of five essential characteristics, four deployment models and three service models.

Five essential characteristics of the Cloud: on-demand self service, broad network access, resource pooling, rapid elasticity, and measured service.

On demand self-service, the first characteristic, means you can access Cloud resources whenever required.
Broad network access means that Cloud computing resources can be accessed through the network.
With resource pooling, consumers save on costs when using a shared model. This model provides Cloud providers economies of scale.
Rapid elasticity implies that you can increase or decrease resources as per your demand.
Measured service means that you only pay for what you use or reserve as you go.

##### History

The concept of cloud computing dates to the 1950s when large-scale mainframes with high-volume processing power became available. The practice of time sharing (or resource pooling) evolved to make efficient use of the computing power of mainframes. Using dumb terminals, whose sole purpose was facilitating access to the mainframes, multiple users could access the same data storage layer and CPU power from any terminal. In the 1970s, with the release of an operating system called Virtual Machine (VM), it became possible for mainframes to have multiple virtual systems, or virtual machines, on a single physical node. Each virtual machine hosted guest operating systems that behaved like they had their own memory, CPU, and hard drives, even though these were shared resources. Virtualization thus became a technological driver and a massive catalyst for some of the most significant evolutions in communications and computing.

A hypervisor is a small software layer that enables multiple operating systems to run alongside each other, sharing the same physical computing resources. A hypervisor also separates the Virtual Machines logically, assigning each slice of the underlying computing power, memory, and storage, preventing the virtual machines from interfering with each other.

Users could now order cloud resources from a larger pool of available resources and pay for them on a per-use basis, also known as pay-as-you-go. This pay-as-you-go or utility computing model, became one of the key drivers behind cloud computing's launching. This allowed them to switch to a more cash-flow friendly OpEx model from a CapEx model.

Agility, flexibility, and competitiveness are key drivers for moving to the cloud, provided it is done without creating business disruption or issues related to security, compliance and performance.

##### In this lesson, you have learned:

Cloud computing is the delivery of on-demand computing resources over the internet on a pay-as-you-go basis; resources are dynamically assigned and reassigned among multiple users and scale up and down in response to users’ needs.

The origins of cloud computing can be traced back to the mainframes of the 1950s, with virtualization technologies and hypervisors serving as catalysts for the emergence of modern-day cloud computing.

Organizations must consider their business needs, investment viability, and risk capacity to create a cloud adoption strategy that delivers desired benefits without causing business disruptions and security, compliance, or performance issues.

Cloud adoption is growing faster than predicted. Driving this technological wave are cloud service providers with a host of services ranging from Infrastructure, Platform, and Software services. Some major Cloud providers of our time include AWS, Alibaba Cloud, Google, IBM, and Microsoft Azure.

#### Business case for Cloud Computing

##### In this lesson, you have learned:

The adoption of cloud technologies enables enterprises, big and small, to be agile, innovative, and competitive and to create differentiated customer experiences. Organizations are asking not whether they should move to the cloud but rather what strategy they should adopt to move to the cloud.

#### Emerging Technologies Accelerated by Cloud

The Internet of Things, or IoT, is a giant network of connected things and people that have changed much of how we live our daily lives - from the way we drive, to how we make purchases, monitoring our personal health, and even how we get energy for our homes. Smart devices and sensors are continuously tracking and collecting data.

There is a three-way relationship between AI, IoT, and Cloud. Just as AI consumes the data produced by IoT devices, the IoT device's behavior can be dictated based on responses from AI. For example, smart assistants. A common type of IoT device continues to learn about the user's preferences as usage grows. Such as songs they like, their home temperature settings, preferred mealtimes, and over time they anticipate their actions based on the user's past history. What we see is a symbiotic relationship between IoT, AI, and Cloud. IoT delivers the data, AI powers the insights, and both these emerging technologies leverage Cloud scalability and processing power to provide value to individuals and businesses alike.

Blockchain is a secure distributed open technology that can help speed up processes, lower costs, and build transparency and traceability in transactional applications. It is an immutable network allowing members to view only those transactions that are relevant to them. The more open, diverse, and distributed the network, the stronger the trust and transparency in the data and transactions. Blockchain and AI, much like IoT and AI powered by the Cloud, also have a three-way relationship. Where blockchain technology provides the trusted, decentralized source of truth, AI powers the analytics and decision-making from the data collected, and Cloud provides globally distributed, scalable and cost efficient computing resources to support both the unprecedented amounts of data being collected and the processing power required to draw insights from this data.

Analytics technologies on the Cloud leverage the flexibility, scalability, and computing resources available on the Cloud. From tracking trends on social media to predict future events, to analyzing data to build machine learning models that can be deployed in cognitive applications. Cloud provides the integrated environment that is required to leverage data for continuous improvement and accelerated business growth.

##### In this lesson, you have learned

Emerging technologies powered by the cloud are disrupting existing business models and creating unprecedented opportunities for businesses to grow, innovate, and create value for their customers.

#### Module 1 Glossary

- Broad Network Access: Cloud computing resources can be accessed through the network.
- Hypervisor: A small software layer that enables multiple operating systems to run alongside each other, sharing the same physical computing resources.
- Measured Service: You only pay for what you use or reserve as you go.
- Utility model of billing: You are charged after the usage and at the end of the pre-defined period.

According to the US National Institute of Standards and Technology (NIST) definition of “cloud computing,” what is the meaning of the statement “a shared pool of configurable computing resources”?

Which key considerations drive an organization's selection of cloud computing when considering expenditure for off-the-shelf software and investments in upgrades?

### Week 2

#### Service Models

- IaaS: With IaaS, the cloud provider manages the physical resources, data centers, cooling, power, network and security, as well as computing resources that include servers and storage.
- PaaS: With PaaS the provider, in addition to the computing resources, also manages the platform infrastructure which includes the operating systems, development tools, databases, and business analytics.
- SaaS: In the SaaS model, in addition to the infrastructure and the platform resources, the provider also hosts and manages the applications and data.

##### IaaS

Infrastructure-as-a-Service is a form of cloud computing that delivers fundamental compute, network, and storage resources to consumers on-demand, over the internet, on a pay-as-you-go basis. The cloud provider hosts the infrastructure components traditionally present in an on-premises data center as well as the virtualization or hypervisor layer. In an IaaS Cloud environment, customers can create or provision virtual machines (or VMs) in their choice of Region and Zone available from the Cloud Provider. These VMs typically come pre-installed the customer’s choice of operating system. The customers can deploy middleware, install applications, and run workloads on these VMs. They can also and create storage for their workloads and backups. Cloud providers often provide customers the ability to track and monitor the performance and usage of their cloud services and manage disaster recovery.

Key components of cloud infrastructure:

- Physical data centers: IaaS providers manage large data centers that contain the physical machines required to power the various layers of abstraction on top of them. In most IaaS models, end users do not interact directly with the physical infrastructure but experience it as a service provided to them.
- Compute: IaaS providers manage the hypervisors and end-users programmatically provision virtual instances with desired amounts of compute, memory, and storage resources. Cloud compute typically comes with supporting services like auto scaling and load balancing that provide scalability and high performance.
- Network: Users get access to networking resources on the cloud through virtualization or programmatically, through APIs.
- Storage: There are three types of cloud data storage: object, file, and block storage. Object storage is the most common mode of storage in the cloud, given that it is highly distributed and resilient.

Use Cases:\
Organizations today are using cloud infrastructure services to enable their teams to set up test and development environments faster, helping create new applications more quickly. By abstracting the low-level components, cloud infrastructure is helping developers focus more on business logic than infrastructure management. Business continuity and disaster recovery require a significant amount of technology and staff investments. IaaS is helping organizations reduce this cost and make applications and data accessible as usual during a disaster or outage. Organizations are using cloud infrastructure to deploy their web applications faster and also scale infrastructure up and down as demand fluctuates. Organizations are leveraging the high-performance computing capabilities of cloud infrastructure to solve complex problems involving millions of variables and calculations such as climate and weather predictions and financial modeling. Mining massive data sets to locate valuable patterns, trends, and associations requires a huge amount of processing power. Cloud infrastructure not only provides the required high-performance computing but also makes it economically viable. While there are some concerns regarding the lack of transparency in the cloud infrastructure’s configuration and management and dependency on a third-party for workload availability and performance,

#### PaaS

Platform as a service is a cloud computing model that provides customers a complete platform to develop, deploy, manage and run applications created by them or acquired from a third party. The PaaS provider hosts everything: servers, networks, storage, operating system, application runtimes, APIs, middleware, databases and other tools at their data center. The provider also takes responsibility for the installation, configuration, and operation of the application infrastructure, leaving the user responsible for only the application code and its maintenance. Customers pay for this service on a usage basis and purchase resources on demand. With IaaS, the cloud provider offers access to raw computing resources such as servers, storage, and networking, while the user is responsible for the platform and application software. With PaaS, the cloud service provider delivers and manages the entire platform infrastructure, abstracting users from the lower level details of the environment.

Essential characteristics of PaaS. PaaS clouds are distinguished by the high level of abstraction they provide to the users, eliminating the complexity of deploying applications, configuring infrastructure, and provisioning and configuring supporting technologies like load balancers and databases. PaaS clouds provide services and APIs that help simplify the job of developers in delivering elastically scalable and highly available cloud applications. These services typically include a variety of capabilities such as APIs for distributing, caching, queuing and messaging, file and data storage, workload management, user identity, and analytics, thus eliminating the need to integrate disparate components. The PaaS runtime environment executes end user code according to policies set by the application owner and cloud provider. Many of the PaaS offerings provide developers with rapid deployment mechanisms or push and run mechanism for deploying and running applications. PaaS offerings support a range of application infrastructure or middleware capabilities such as application servers, database management systems, business analytics servers, mobile backend services, integration services, business process management systems, rules engines, and complex event processing systems. Such an application infrastructure assists developers by reducing the amount of code that must be written while expanding the application's functional capabilities. The most important use case for PaaS is strategic, build, test, deploy, enhance and scale applications rapidly and cost effectively.

Use cases for PaaS:

- API development and management: Organizations are using PaaS to develop, run, manage and secure APIs and microservices, which are loosely coupled, independently deployable components and services.
- Internet of Things: PaaS clouds support a broad range of application environments, programming languages, and tools used for IoT deployments.
- Business analytics, or intelligence: PaaS tools allow organizations to analyze their data to find business insights that enable more informed business decisions and predictions.
- Business Process management: Organizations are using the PaaS cloud to access BPM platform delivered as a service.
- Master data management: Organizations are leveraging the PaaS cloud to provide a single point of reference for critical business data, such as information about customer transactions and analytical data to support decision-making.

Advantages of using PaaS:

- Scalability, made possible because of the rapid allocation and deallocation of resources with a pay-as-you-use model offered by PaaS.
- The APIs support services and middleware capabilities that PaaS clouds provide assist developers in focusing their efforts on application development and testing, resulting in faster time-to-market for their products and services. Middleware capabilities also reduce the amount of code that need to be written while expanding the application's functional capabilities.
- Greater agility and innovation: because using PaaS platforms means that you can experiment with multiple operating systems, languages and tools without having to invest in these resources. You can evaluate and prototype ideas with very low risk exposure, resulting in faster, easier, less risky adoption of a wider range of resources.

PaaS clouds do come with some risks such as information security threats and dependency on the service provider's infrastructure. Services can get impacted when a service provider's infrastructure experiences downtime. Customers also don't have any direct control over the changes that may take place when a provider makes changes in its strategy, service offerings or tools.

#### SaaS

Software-as-a-Service is a cloud offering that provides users with access to a service provider’s cloud-based software. SaaS providers maintain the servers, databases, and code that constitute an application. They also manage access to the application, including security, availability, and performance. Applications reside on a remote cloud network, and users use these applications without having to maintain and update the infrastructure.

Core business processes supported by SaaS today include email and collaboration via offerings such as Microsoft's Office 365 and Google's Gmail, Customer Relationship Management via services such as NetSuite CRM and Salesforce, Human Resource Management via services from Workday and SAP SuccessFactors, financial management, billing and collaboration, and many more.

Key characteristics: SaaS clouds have a multitenant architecture. Infrastructure and code are maintained centrally and accessed by all users. SaaS makes it easy for users to manage privileges, monitor data use, and ensure everyone sees the same information at the same time. Security, compliance, and maintenance are all part of the offering.

In SaaS, customizations are often limited, however some SaaS applications may allow certain types of customizations like branding; they can modify data fields and enable or disable features within the business process. These customizations are preserved through upgrades. Users pay for the use of the services via a subscription model. The use of resources can be scaled easily, depending on service needs.

Key benefits of adopting SaaS: Businesses can directly procure solutions without upfront capital and assistance from IT, greatly reducing the time from decision to value from months to days. SaaS greatly increases workforce productivity and efficiency. Users can access core business apps from wherever; they can also buy and deploy apps in minutes reducing the typical obstacles enterprises have to test the products they might use. Using SaaS applications, individuals and small enterprises can spread out their software costs over time.

Use cases for SaaS:\
Organizations are moving to SaaS for their core business needs as part of their strategic transformation to reduce on-premises IT infrastructure and reduce capital expenditure. Organizations are leveraging SaaS to avoid the need for ongoing upgrades, maintenance, and patching, done traditionally by internal IT resources; applications run reliably with minimal input, for example, email servers and office collaboration and productivity tools. Organizations are increasingly opting for SaaS eCommerce Platforms to manage their websites, marketing, sales, and operations. With SaaS, organizations are able to take advantage of the resilience and business continuity of the cloud provider. Enterprises are now developing SaaS integration platforms (or SIPs) for building additional SaaS applications, moving SaaS beyond standalone software functionality to a platform for mission-critical applications.

Concerns: Primary among them being data ownership and data safety. Security is an important consideration when you’re allowing a third-party to maintain business-critical data. And application access relies on a good network connection.

##### In this lesson, you have learned

- With IaaS, the cloud provider manages physical resources.
- With PaaS, the provider manages the platform infrastructure.
- In the SaaS model, the provider hosts and manages the applications and data.
- Infrastructure-as-a-Service is a form of cloud computing that delivers fundamental computer, network, and storage resources to consumers on-demand, over the network, on a pay-as-you-go basis.
- The key components of cloud infrastructure are:

  - Physical data centers
  - Compute
  - Network
  - Storage

- Platform-as-a-Service is a cloud computing model that provides customers with a complete platform—hardware, software, and infrastructure.
- The high level of abstraction, support services, runtime environments, rapid deployment mechanisms, and middleware capabilities distinguishes PaaS clouds.
- PaaS advantages are:

  - Scalability
  - Faster time to market products and services.
  - Greater agility and innovation

- Software-as-a-Service is a cloud offering that provides users with access to a service provider’s cloud-based software.
- SaaS characteristics are:

  - Multitenant architecture
  - Security, compliance, and maintenance
  - Customization of applications
  - Subscription model
  - Scaling

- SaaS advantages are:
  - Direct procurement of solutions
  - Improved workforce productivity and efficiency
  - Enable distribution of software costs

#### Deployment Models

Deployment models indicate where the infrastructure resides, who owns and manages it, and how cloud resources and services are made available to users. The four cloud deployment models include—Public Cloud, Private Cloud, Community Cloud and Hybrid Cloud.

##### Public Cloud

- In a public cloud model, users get access to servers, storage, network, security, and applications as services delivered by cloud service providers over the internet. Using web consoles and APIs, users can provision the resources and services they need. The cloud provider owns, manages, provisions, and maintains the infrastructure, renting it out to customers either for a subscription charge or usage-based fee. Users don’t own the servers their applications run on or storage their data consumes, or manage the operations of the servers, or even determine how the platforms are maintained.
- Public clouds offer significant cost savings in terms of Total Cost for Ownership (TCO) as the provider bears all the capital, operational, and maintenance expenses for the infrastructure and the facilities they are hosted in. It makes scalability as easy as requesting more capacity. However, with a public cloud, the user does not have any control over the computing environment and is subject to the performance and security of the cloud provider’s infrastructure.

Characteristics of a public cloud: A public cloud is a virtualized multi-tenant architecture enabling tenants or users to share computing resources, residing outside their firewalls The cloud provider's pool of resources, including infrastructure, platforms, and software, are NOT dedicated for use by a single tenant or organization Resources are distributed on an as-needed basis offered through a variety of subscription and pay-as-you-go models.

Public clouds have significant benefits: Vast on-demand resources are available, allowing applications to respond seamlessly to fluctuations in demand. Considering the large number of users that share the centralized cloud resources on-demand, the public cloud offers the most significant economies of scale. The sheer number of server and network resources available on the public cloud means that a public cloud is highly available —if one physical component fails, the service still runs unaffected on the remaining available components.

Concerns users have regarding public clouds—key among them being security and data sovereignty compliance. Security issues such as data breaches, data loss, account hijacking, insufficient due diligence, and system and application vulnerability seem to be some of the fears users continue to have concerning security in the public cloud. With data being stored in different locations and accessed across national borders, it has also become increasingly critical for companies to be compliant with data sovereignty regulations governing the storage, transfer, and security of data. A service provider’s ability to not just keep up with the regulations, but also the interpretation of these regulations, is a concern shared by many businesses.

Use cases for public cloud: Organizations are increasingly opting to access cloud-based applications and platforms so their teams can focus on building and testing applications, and reducing time-to-market for their products and services. Businesses with fluctuating capacity and resourcing needs are opting for the public cloud. Organizations are using public cloud computing resources to build secondary infrastructures for disaster recovery, data protection, and business continuity. More and more organizations are using cloud storage and data management services for greater accessibility, easy distribution, and backing up their data. IT departments are outsourcing the management of less critical and standardized business platforms and applications to pubic cloud providers.

##### Private Cloud

The National Institute of Standards and Technology defines private cloud as cloud infrastructure provisioned for exclusive use by a single organization comprising multiple consumers, such as the business units within the organization. It may be owned, managed, and operated by the organization, a third party or some combination of them, and it may exist on or off premises.

Private cloud platforms can be implemented internally or externally. When the platform is provisioned over an organization's internal infrastructure, it runs on-premises and is owned, managed, and operated by the organization. When it is provisioned over a cloud providers infrastructure, it is owned, managed, and operated by the service provider. This external private cloud offering that resides on a cloud service providers infrastructure is called a Virtual Private Cloud or VPC. A VPC is a public cloud offering that lets an organization establish its own private and secure cloud-like computing environment in a logically isolated part of a shared public cloud. Using a VPC, organizations can leverage the dynamic scalability, high availability, and lower cost of ownership of a public cloud, while having the infrastructure and security tailored to the organization's unique needs.

Private cloud provide you with:

- the ability to leverage the value of cloud computing using systems that are directly managed or under perceived control of the organization's internal IT.
- the ability to better utilize internal computing resources, such as the organization's existing investments in hardware and software, thereby reducing costs.
- better scalability through virtualization and cloud bursting. That is, leveraging public cloud instances for a period of time, but returning to the private cloud when the surge is meet.
- controlled access and greater security measures customized to specific organizational needs.
- the ability to expand and provision things in a relatively short amount of time, providing greater agility.

Use cases for a private cloud:

- a private cloud is an opportunity for organizations to modernize and unify their in-house and legacy applications. Moving these applications from their dedicated hardware to the cloud also allows them to leverage the power of the compute resources and multiple services available on the cloud.
- using the private cloud, organizations are integrating data and application services from their existing applications with public cloud services. This allows them to leverage their private cloud's compute capability for the larger jobs while pulling data into an application on a private cloud to leverage public cloud services. Essentially, opening their data centers to work with cloud services.
- application portability is a key feature of cloud platforms. Using the private cloud gives organizations the ability to build applications anywhere and move them anywhere without having to compromise security and compliance in the process.
- some of the key reasons that may prevent an organization for moving to a public cloud include security and regulatory concerns and data sensitivity. A private cloud offers these organizations the benefits of on-demand enterprise resources while exercising full control over critical security and compliance issues from within the environment of their dedicated cloud.

##### Hybrid Cloud

Hybrid Cloud is a computing environment that connects an organization's on-premise private Cloud and third-party public Cloud, into a single flexible infrastructure for running the organizations applications and workloads.

You can leverage public Cloud instances for a period of time, but returned to the private Cloud when the search is met, also known as Cloud bursting.

The key tenants of a hybrid Cloud are interoperability, scalability, and portability.

- Hybrid Cloud is interoperable, which means that the public and private Cloud services can understand each other's APIs, configuration, data formats, and forms of authentication and authorization.
- When there's a spike in demand, a workload running on the private Cloud can leverage the additional public Cloud capacity making it scalable.
- A hybrid Cloud is also portable. Since you're no longer locked in with a specific vendor, you can move applications and data not just between on-premise and Cloud systems, but also between Cloud service providers.

There are two common types of hybrid Clouds, hybrid mono Cloud and hybrid multi-Cloud. Hybrid mono Cloud is a hybrid Cloud with one Cloud provider while a hybrid multi-Cloud is an open standards-based stack that can be deployed on any public Cloud infrastructure. The difference lies in the flexibility that the hybrid multi-Cloud offers organizations to move workloads and environments from one vendor to another.

However, hybrid Clouds are complex and challenging to deploy and maintain since they involve synchronization, redirection, latency, security, portability, interoperability, and compatibility of policies, applications and data and so on.

Common Hybrid Cloud use cases:

- Software-as-a-service integration. Through Hybrid Integration, Organizations are connecting software-as-a-service applications available in the public Cloud to their existing public Cloud, private Cloud and traditional IT applications to deliver new solutions.
- Data and AI integration. Organizations today are creating richer and more personal experiences by combining new data sources on the public Cloud, such as weather, social, the Internet of Things, CRM, and ERP, with existing data and analytics, machine learning and AI capabilities.
- Enhancing legacy apps. An increasing number of organizations are using public Cloud services to upgrade the user experience of their on-premises applications and deploy them globally to new devices while incrementally modernizing their core business systems.
- VMware migration. More and more organizations are lifting and shifting their on-premises virtualized workloads to a public Cloud without conversion or modification to reduce their on-premises datacenter footprint, and position themselves to scale without added capital expense.
- Leveraging public Cloud services. Using the private Cloud, organizations are integrating data and application services from their existing applications with public Cloud services. This allows them to leverage their private Cloud compute capability for the larger jobs while pulling data into an application on a private Cloud to leverage public Cloud services, essentially, opening their datacenters to work with Cloud services.

Key concepts that make up a hybrid Cloud architecture:

- Connectivity and interoperability
- modernization
- Security

##### Community Cloud

Cloud infrastructure \[that\] is provisioned for exclusive use by a specific community of consumers from organizations that have shared concerns (e.g., mission, security requirements, policy, and compliance considerations). It may be owned, managed, and operated by one or more of the organizations in the community, a third party, or some combination of them, and it may exist on or off premises.

##### In this lesson, you have learned

- Deployment models indicate where the infrastructure resides, who owns and manages it, and how cloud resources and services are made available to users. There are four main deployment models available on the cloud—public, private, hybrid, and community.
- In the public cloud model, the service provider owns, manages, provisions, and maintains the physical infrastructure such as data centers, servers, networking equipment, and storage, with users accessing virtualized computing, networking and storage resources as services.
- In the private cloud model, the provider provisions the cloud infrastructure for exclusive use by a single organization. The private cloud infrastructure can be internal to the organization and run or on-premises. Or it can be on a public cloud, as in the case of Virtual Private Clouds (VPC), and be owned, managed, and operated by the cloud provider.
- In the hybrid cloud model, an organization’s on-premise private cloud and a third-party, public cloud are connected as a single, flexible infrastructure that leverages the features and benefits of both Public and Private clouds.
- In the community cloud model, the provider provisions the cloud infrastructure for use by a community of organizations with shared concerns. One or more of the organizations in the community, a third-party provider, or both are responsible for the ownership, management, and operation of this infrastructure.
