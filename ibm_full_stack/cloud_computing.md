# Cloud Computing

## Week 1

### Introduction to Cloud Computing

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

### History

The concept of cloud computing dates to the 1950s when large-scale mainframes with high-volume processing power became available. The practice of time sharing (or resource pooling) evolved to make efficient use of the computing power of mainframes. Using dumb terminals, whose sole purpose was facilitating access to the mainframes, multiple users could access the same data storage layer and CPU power from any terminal. In the 1970s, with the release of an operating system called Virtual Machine (VM), it became possible for mainframes to have multiple virtual systems, or virtual machines, on a single physical node. Each virtual machine hosted guest operating systems that behaved like they had their own memory, CPU, and hard drives, even though these were shared resources. Virtualization thus became a technological driver and a massive catalyst for some of the most significant evolutions in communications and computing.

A hypervisor is a small software layer that enables multiple operating systems to run alongside each other, sharing the same physical computing resources. A hypervisor also separates the Virtual Machines logically, assigning each slice of the underlying computing power, memory, and storage, preventing the virtual machines from interfering with each other.

Users could now order cloud resources from a larger pool of available resources and pay for them on a per-use basis, also known as pay-as-you-go. This pay-as-you-go or utility computing model, became one of the key drivers behind cloud computing's launching. This allowed them to switch to a more cash-flow friendly OpEx model from a CapEx model.

Agility, flexibility, and competitiveness are key drivers for moving to the cloud, provided it is done without creating business disruption or issues related to security, compliance and performance.

##### In this lesson, you have learned:

Cloud computing is the delivery of on-demand computing resources over the internet on a pay-as-you-go basis; resources are dynamically assigned and reassigned among multiple users and scale up and down in response to users’ needs.

The origins of cloud computing can be traced back to the mainframes of the 1950s, with virtualization technologies and hypervisors serving as catalysts for the emergence of modern-day cloud computing.

Organizations must consider their business needs, investment viability, and risk capacity to create a cloud adoption strategy that delivers desired benefits without causing business disruptions and security, compliance, or performance issues.

Cloud adoption is growing faster than predicted. Driving this technological wave are cloud service providers with a host of services ranging from Infrastructure, Platform, and Software services. Some major Cloud providers of our time include AWS, Alibaba Cloud, Google, IBM, and Microsoft Azure.

### Business case for Cloud Computing

##### In this lesson, you have learned:

The adoption of cloud technologies enables enterprises, big and small, to be agile, innovative, and competitive and to create differentiated customer experiences. Organizations are asking not whether they should move to the cloud but rather what strategy they should adopt to move to the cloud.

### Emerging Technologies Accelerated by Cloud

The Internet of Things, or IoT, is a giant network of connected things and people that have changed much of how we live our daily lives - from the way we drive, to how we make purchases, monitoring our personal health, and even how we get energy for our homes. Smart devices and sensors are continuously tracking and collecting data.

There is a three-way relationship between AI, IoT, and Cloud. Just as AI consumes the data produced by IoT devices, the IoT device's behavior can be dictated based on responses from AI. For example, smart assistants. A common type of IoT device continues to learn about the user's preferences as usage grows. Such as songs they like, their home temperature settings, preferred mealtimes, and over time they anticipate their actions based on the user's past history. What we see is a symbiotic relationship between IoT, AI, and Cloud. IoT delivers the data, AI powers the insights, and both these emerging technologies leverage Cloud scalability and processing power to provide value to individuals and businesses alike.

Blockchain is a secure distributed open technology that can help speed up processes, lower costs, and build transparency and traceability in transactional applications. It is an immutable network allowing members to view only those transactions that are relevant to them. The more open, diverse, and distributed the network, the stronger the trust and transparency in the data and transactions. Blockchain and AI, much like IoT and AI powered by the Cloud, also have a three-way relationship. Where blockchain technology provides the trusted, decentralized source of truth, AI powers the analytics and decision-making from the data collected, and Cloud provides globally distributed, scalable and cost efficient computing resources to support both the unprecedented amounts of data being collected and the processing power required to draw insights from this data.

Analytics technologies on the Cloud leverage the flexibility, scalability, and computing resources available on the Cloud. From tracking trends on social media to predict future events, to analyzing data to build machine learning models that can be deployed in cognitive applications. Cloud provides the integrated environment that is required to leverage data for continuous improvement and accelerated business growth.

##### In this lesson, you have learned

Emerging technologies powered by the cloud are disrupting existing business models and creating unprecedented opportunities for businesses to grow, innovate, and create value for their customers.

##### Module 1 Glossary

- Broad Network Access: Cloud computing resources can be accessed through the network.
- Hypervisor: A small software layer that enables multiple operating systems to run alongside each other, sharing the same physical computing resources.
- Measured Service: You only pay for what you use or reserve as you go.
- Utility model of billing: You are charged after the usage and at the end of the pre-defined period.

According to the US National Institute of Standards and Technology (NIST) definition of “cloud computing,” what is the meaning of the statement “a shared pool of configurable computing resources”?

Which key considerations drive an organization's selection of cloud computing when considering expenditure for off-the-shelf software and investments in upgrades?

## Week 2

### Service Models

- IaaS: With IaaS, the cloud provider manages the physical resources, data centers, cooling, power, network and security, as well as computing resources that include servers and storage.
- PaaS: With PaaS the provider, in addition to the computing resources, also manages the platform infrastructure which includes the operating systems, development tools, databases, and business analytics.
- SaaS: In the SaaS model, in addition to the infrastructure and the platform resources, the provider also hosts and manages the applications and data.

#### IaaS

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

### Deployment Models

Deployment models indicate where the infrastructure resides, who owns and manages it, and how cloud resources and services are made available to users. The four cloud deployment models include—Public Cloud, Private Cloud, Community Cloud and Hybrid Cloud.

### Public Cloud

- In a public cloud model, users get access to servers, storage, network, security, and applications as services delivered by cloud service providers over the internet. Using web consoles and APIs, users can provision the resources and services they need. The cloud provider owns, manages, provisions, and maintains the infrastructure, renting it out to customers either for a subscription charge or usage-based fee. Users don’t own the servers their applications run on or storage their data consumes, or manage the operations of the servers, or even determine how the platforms are maintained.
- Public clouds offer significant cost savings in terms of Total Cost for Ownership (TCO) as the provider bears all the capital, operational, and maintenance expenses for the infrastructure and the facilities they are hosted in. It makes scalability as easy as requesting more capacity. However, with a public cloud, the user does not have any control over the computing environment and is subject to the performance and security of the cloud provider’s infrastructure.

Characteristics of a public cloud: A public cloud is a virtualized multi-tenant architecture enabling tenants or users to share computing resources, residing outside their firewalls The cloud provider's pool of resources, including infrastructure, platforms, and software, are NOT dedicated for use by a single tenant or organization Resources are distributed on an as-needed basis offered through a variety of subscription and pay-as-you-go models.

Public clouds have significant benefits: Vast on-demand resources are available, allowing applications to respond seamlessly to fluctuations in demand. Considering the large number of users that share the centralized cloud resources on-demand, the public cloud offers the most significant economies of scale. The sheer number of server and network resources available on the public cloud means that a public cloud is highly available —if one physical component fails, the service still runs unaffected on the remaining available components.

Concerns users have regarding public clouds—key among them being security and data sovereignty compliance. Security issues such as data breaches, data loss, account hijacking, insufficient due diligence, and system and application vulnerability seem to be some of the fears users continue to have concerning security in the public cloud. With data being stored in different locations and accessed across national borders, it has also become increasingly critical for companies to be compliant with data sovereignty regulations governing the storage, transfer, and security of data. A service provider’s ability to not just keep up with the regulations, but also the interpretation of these regulations, is a concern shared by many businesses.

Use cases for public cloud: Organizations are increasingly opting to access cloud-based applications and platforms so their teams can focus on building and testing applications, and reducing time-to-market for their products and services. Businesses with fluctuating capacity and resourcing needs are opting for the public cloud. Organizations are using public cloud computing resources to build secondary infrastructures for disaster recovery, data protection, and business continuity. More and more organizations are using cloud storage and data management services for greater accessibility, easy distribution, and backing up their data. IT departments are outsourcing the management of less critical and standardized business platforms and applications to pubic cloud providers.

### Private Cloud

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

### Hybrid Cloud

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

### Community Cloud

Cloud infrastructure \[that\] is provisioned for exclusive use by a specific community of consumers from organizations that have shared concerns (e.g., mission, security requirements, policy, and compliance considerations). It may be owned, managed, and operated by one or more of the organizations in the community, a third party, or some combination of them, and it may exist on or off premises.

##### In this lesson, you have learned

- Deployment models indicate where the infrastructure resides, who owns and manages it, and how cloud resources and services are made available to users. There are four main deployment models available on the cloud—public, private, hybrid, and community.
- In the public cloud model, the service provider owns, manages, provisions, and maintains the physical infrastructure such as data centers, servers, networking equipment, and storage, with users accessing virtualized computing, networking and storage resources as services.
- In the private cloud model, the provider provisions the cloud infrastructure for exclusive use by a single organization. The private cloud infrastructure can be internal to the organization and run or on-premises. Or it can be on a public cloud, as in the case of Virtual Private Clouds (VPC), and be owned, managed, and operated by the cloud provider.
- In the hybrid cloud model, an organization’s on-premise private cloud and a third-party, public cloud are connected as a single, flexible infrastructure that leverages the features and benefits of both Public and Private clouds.
- In the community cloud model, the provider provisions the cloud infrastructure for use by a community of organizations with shared concerns. One or more of the organizations in the community, a third-party provider, or both are responsible for the ownership, management, and operation of this infrastructure.

## Week 3

### Cloud Infrastructure

- The infrastructure layer is the foundation of the cloud. This layer consists of physical resources that are housed in Regions, Zones and Data Centers.
- A cloud Region, is a geographic area or location where a Cloud provider’s infrastructure is clustered. The cloud Regions are isolated from each other.
- Each Cloud Region can have multiple Zones (or Availability Zones or AZ for short), which are typically distinct Data Centers with their own power, cooling and networking resources. The isolation of zones improves the cloud’s overall fault tolerance, decreases latency, and avoids creating a single shared point of failure. The Availability Zones (and DataCenters within them) are connected to other AZs and regions, private datacenters and the Internet using very high bandwidth network connectivity.
- Computing Resources: Cloud providers offer several compute options – Virtual Servers, Bare Metal Servers, and “Serverless” computing resources. Most of the servers in a cloud datacenter run hypervisors to create virtual servers or virtual machines (also called VMs for short), that are software-based computers, based on virtualization technologies. Other servers in the racks are bare metal servers that are physical servers that aren’t virtualized. Customers can provision VMs and Bare Metals servers as and when they need them and run their workloads on them. Cloud users can also run their workloads on serverless computing resources, which are an abstraction layer on top of virtual machines.
- Storage: Information and data can consist of files, code, documents, images, videos, backups, snapshots, and databases and can be stored in many different types of storage options on the Cloud. Bare Metal Servers and Virtual Servers are provisioned with default storage in local drives.
- Networking: Networking infrastructure in a cloud datacenter includes traditional networking hardware like routers and switches, but more importantly for users of the Cloud, the Cloud providers have Software Defined Networking (or SDN) options where certain networking resources are virtualized or made available programmatically, through APIs. This allows for easier network provisioning, configuration, and management in the cloud. When servers in the cloud are provisioned, you need to setup their public and private network interfaces. The public network interfaces connect the servers to the public internet, whereas the private ones provide connectivity to your other cloud resources and help keep them secure. Network interfaces in the cloud need to have IP addresses and subnets either assigned automatically or configured. In a cloud environment it is even more important to configure which network traffic and users can access your resources, which can be done by setting up Security Groups and Access Control Lists (or ACLs). For further security and isolation of your resources in the cloud, most Cloud providers provide Virtual Local Area Networks (VLANs), Virtual Private Clouds (VPCs), and Virtual Private Networks (VPNs).
- Some of the traditional hardware appliances such as firewalls, load balancers, gateways and traffic analyzers can also be virtualized and made available as services in the cloud. Another networking capability provided by the Cloud Providers is Content Delivery Networks or CDNs, that distribute content to multiple points throughout the world so users accessing the content can access it more quickly by getting it from a point nearest to them.

### Virtualization and Virtual Machines

- Virtualization is the process of creating a software based, or virtual, version of something, whether that be compute, storage, networking, servers, or applications and what makes virtualization feasible, is something called the hypervisor.

- Hypervisor is a piece of software that runs above the physical server, or host and what they do is essentially pull the resources from the physical server and allocate them to your virtual environments. There are two types of hypervisors:

  - Type 1: A Type 1 hypervisor is installed directly on top of the physical server. They're also called bare-metal hypervisors. These are the most frequently type of used hypervisors and they're most secure, they lower the latency.
  - Type 2: what makes these different is that there is a layer of host OS that sits between the physical server and the hypervisor. So, by that nature they are also called, Hosted. These are a lot less frequent.

- Once you have your hypervisor installed, you can build virtual environments. A VM is simply a software based computer. They're run like a physical computer. They have an operating system and applications, and they're completely independent of one another but you can run multiple of them on a hypervisor and the hypervisor manages the resources that are allocated to these virtual environments from the physical server. So, because they're independent you can run different operating systems on different virtual machines making them extremely portable.

- Key Benefits:
  - Cost Savings
  - Agility and Speed
  - Lower downtime: as VMs can be easily installed on a new physical server (in case the one it is currently running on goes down).

### Types of VMs

- Shared or Public Cloud VMs are provider-managed, multi-tenant deployments that can be provisioned on-demand with predefined sizes. Being multi-tenant means that the underlying physical server is virtualized and is shared across other tenants or users.
- Transient or Spot VMs take advantage of unused capacity in a cloud data center. Cloud providers make this unused capacity available to users at a much lower cost than regular VMs of similar sizes. Although the Transient VMs are available at a huge discount, the Cloud provider can choose to de-provision them at any time and reclaim the resources for provisioning regular, higher-priced, VMs. Because you run the risk of losing these VMs when capacity in the data center decreases, these VMs are great for non-production workloads such as testing and developing applications. They are also useful for running stateless workloads, testing scalability, or running big data and high performance computing (HPC) workloads at a low cost.
- Reserved virtual server instances allow you to reserve capacity and guarantee resources for future deployments. You reserve desired amount of virtual server capacity, provision instances from that capacity when you need them.
- Dedicated hosts offer single-tenant isolation. Dedicated hosts are typically used for meeting compliance and regulatory requirements or meet specific licensing terms.

### Bare Metal Servers

- A bare metal server is a single tenant, dedicated physical server.
- The Cloud provider manages the server up to the operating system or OS, which means if anything goes wrong with the hardware or rack connection, they will fix or replace it, and then reboot the server. The customer is responsible for administering and managing everything else on the server.
- Bare metal servers are either pre-configured by the Cloud provider to meet workload packages or they can be custom-configured as per customer specifications. This includes the processors, RAM, hard drives, specialized components, and the OS. Customers can also install their own OS and can install certain hypervisors that aren't available from the Cloud provider, and thus create their own virtual machines and farms.
- With bare metal servers, you can also add GPUs, which are designed for accelerating scientific computation, data analytics, and rendering professional grade virtualized graphics.
- Clients have full access and control of bare metal servers because there's no hypervisor required. As there is no sharing underlying server hardware with other customers, bare metal servers fulfill the demanding needs of high-performance computing or HPC, and data intense applications that require minimal latency related delays. These servers also excel in big data analytics applications and GPU-intensive solutions.
- Some workload examples that bare metal servers satisfy are ERP, CRM, AI, deep learning, and virtualization. If you use any applications that require high degrees of security control or apps that you've typically run in an on-premises environment, then a bare metal server is a good alternative in the Cloud.
- Bare metal servers work best for CPU and I/O intensive workloads, excel with highest performance and security, satisfy strict compliance requirements, and offer complete flexibility, control, and transparency, but come with added management and operational overhead. Whereas virtual servers are rapidly provisioned, provide an elastic and scalable environment, and are low cost to use. However, since they share underlying hardware with other virtual servers, they can be limited in throughput and performance.

### Securing Networking in Cloud

- How to build a secure Cloud networking presence: The notion of building a Cloud network is not much different from deploying a network in an on-premises data center. The main difference: in the Cloud we use logical instances of networking elements as opposed to physical devices. For example, network interface controllers or NICs would be represented by vNICs in cloud environments.
- To create a network in the Cloud, one starts by defining the size of the network or the IP address range that establishes the boundaries or the Cloud network. Cloud networks are deployed in networking spaces that are logically separated segments of the networks using options including Virtual, Private Cloud, or VPC that in turn can be divided into smaller segments called subnets. Cloud resources such as VMs or Virtual Server Instances, VSIs, storage, network connectivity, and load balancers are deployed into subnets. Subnets are also the main area where security is implemented in the Cloud. Every subnet is protected by access control lists or ACLs that serve as a subnet-level firewall. Within the subnet, one could create security groups that provide security at the instance level, such as VSIs.

### Containers

- Containers are an executable unit of software in which application code is packaged, along with its libraries and dependencies, in common ways so that it can be run anywhere, whether it be on desktop, traditional IT, or the cloud. Containers are small, fast, and portable, and unlike virtual machines, they do not need to include a guest OS in every instance and can, instead, simply leverage the features and resources of the host OS.
- There's a three-step process when kind of doing anything container related:
  - Manifest
  - Create the actual image
  - Actual container
  - Example: We create a docker file. We build out the image. We push it to a registry, and we have our container and we can start pushing this out as containers.
- The difference between VMs and containers:
  - in containers, there is no hypervisor, instead there is something like runtime engine. For example, for Docker, it will be Docker Engine.
  - containers are lightweight
  - There is no OS (in VMs there is OS)
  - if some of the container processes aren't utilizing the CPU or memory, all of that shared resources become accessible for the other containers running within that hardware.
  - Containers are portable.

##### In this lesson, you have learned

- Cloud infrastructure consists of data centers, storage, networking components, and computing resources.
- Virtualization is the process of creating a software-based version of physical resources, made possible by hypervisors.
- A few different types of Virtual Machines can be provisioned on the cloud. These include:
  - Shared or Public Cloud VMs that are provider-managed, multi-tenant deployments that can be provisioned on-demand with predefined sizes
  - Transient or Spot VMs that take advantage of unused capacity in a cloud data center
  - Reserved VMs that allow you to reserve capacity and guarantee resources for future deployments
  - Dedicated hosts that offer single-tenant isolation
- Bare metal servers are single-tenant physical servers that are dedicated to a single customer. Bare metal servers fulfill the demanding needs of high-performance computing (HPC) and data-intense applications. They are ideal for applications that have a high degree of security or compliance requirements.
- Networking capabilities in the cloud are delivered as a service rather than in the form of rack-mounted devices. Cloud resources such as VMs (or VSIs), storage, network connectivity, and load balancers are deployed into subnets within Virtual Private Clouds (VPCs). Using private and public subnets allows users to deploy multi-tier enterprise applications securely. Load balancers distribute the traffic and allow applications to be responsive.
- Containers are executable units of software in which application code, its libraries, and its dependences are packaged in a common way, so that it can be run anywhere, from desktops, traditional IT, to the cloud. Containers are more lightweight and consume fewer resources than Virtual Machines, helping streamline the development and deployment of cloud native applications.

### Cloud Storage and Content Delivery Networks

- Cloud storage is where you save data files in the cloud. Certain storage must be attached to a compute node before the storage can be accessed, whereas other storage types can be directly accessed either through the public Internet or a dedicated private network connection.
- Cloud storage is available in four main types – Direct Attached, File Storage, Block Storage and Object Storage.
- Direct Attached storage (or Local Storage), is storage which is presented directly to a cloud-based server and is effectively either within the host server chassis or within the same rack. This storage is fast and normally only used to store a server’s operating system. The main two reasons why direct attached storage is not so great for other uses is that it’s typically Ephemeral – meaning that it only lasts as long at the compute resource it’s attached to – it cannot be shared with other nodes and while you can use [RAID](https://www.javatpoint.com/what-is-raid) techniques, it’s not as resilient to failure as other types of storage.
- File storage is typically presented to compute nodes as ‘NFS Storage’. NFS stands for Network File System and means that the storage is connected to compute nodes over a standard ethernet network. NFS-mounted storage tends to be slower than either direct-attached storage or block storage because the data travels over an ethernet network. It also tends to be lower cost than either direct attached or block storage. One advantage of File Storage is that it can be mounted or used on multiple servers at once.
- Block storage is presented to compute nodes using high-speed fibre connections, which means that read and write speeds are typically much faster and reliable than with file storage, making block storage suitable for use with databases and other applications where disk speed is important.
- IOPS stands for ‘Input/Output Operations Per Second’ and relates to the speed of the storage or to put it another way, how quickly data can be read from or written to the storage.
- Persistence is a term that is used when provisioning File or Block storage and relates to what happens to the storage once the compute node it is attached to is terminated. If the storage is set to ‘persist’ then it will not be deleted along with the compute node. Otherwise Ephemeral.
- Snapshots are a way to create backup data.
- Object storage is accessed via an API. Of all the storage types, Object Storage is by far the cheapest and also the slowest in terms of read and write speeds, but it is infinite in size to the end user. It is useful for all sorts of unstructured data types, large and small, including documents, video, logs, backups, data from IoT, application binaries and virtual machine images.

### File Storage

- File storage is mounted from remote storage appliances. That is, the physical disks are contained in a separate, specialised piece of hardware and they are then connected to the compute node via the underlying infrastructure in the data center. These storage appliances are not only extremely resilient to failure, the data is also far more secure in them as these storage appliances provide services such as encryption in transit.
- File Storage is mounted to compute nodes via an ethernet network.
- One of the issues with ethernet networks is that their speed can vary – the more loaded an ethernet network is, the more likely it becomes that its speed or bandwidth will be affected. Therefore, File storage tends to be used for workloads where consistently high network speeds are not a requirement.
- The ability for File Storage to be mounted to multiple compute nodes at a time make it an ideal solution where some sort of common storage is required.
- Also used with unstructured data.

### Block Storage

- Block storage is storage where data is written in raw blocks on the storage and it's accessed by the servers that you have through a storage area network and stores each block separately under a unique address. Block storage must be attached to a compute node before it can be utilized for your workloads. Block storage can be mounted from remote storage appliances, making it extremely resilient to failure, and keeping data far more secure in them, on account of encryption in transit, and encryption at rest services, available on these appliances.
- Block storage is mounted as a volume to compute nodes using a dedicated network of fibers, through which signals move at the speed of light. These fiber optic networks are more expensive to build than the ethernet ones which deliver File Storage, which is one reason why Block Storage tends to have a higher price-point. However, since the traffic is moving faster and with speed consistency, they are perfect for workloads that need low-latency storage to work effectively.
- Block Storage is normally mounted onto only one compute node at a time. Since these disks run at a consistent high speed, they are perfect for workloads that need consistently fast storage, such as databases and mail servers.

### Object Storage

- You do not connect Object Storage to a particular compute node. Instead, you provision an object storage service instance and use an API or application programming interface to upload, download, and manage your data.
- Object storage is less expensive than other Cloud storage options.
- Object storage is effectively infinite.
- A bucket is a bit like a folder, in the sense that you can give them meaningful names and have different buckets for different object types. But you cannot place a bucket with in a bucket. When an object is placed in a bucket, it also has some metadata such as an object ID. This metadata helps applications to both locate and access the object
- Object storage would not be suitable for running operating systems, nor applications such as databases or anything else where the contents of the files changes.
- Object Storage buckets have storage tiers, or classes, associated with them and these tiers are based on how frequently the data is accessed.
  - A standard tier bucket is where you would store objects that are frequently accessed.
  - A vault or archive tier is where you might store documents that are only accessed perhaps only once or twice a month, or less.
  - Cold vault tier, where you would store data that is typically accessed only once or twice a year.
- Object Storage does not come with IOPS options.
- Object Storage in the Cloud offers an effective Backup and Disaster Recovery Solution.

### CDN - Content Delivery Networks

- A content delivery network, or CDN, is a distributed server network that delivers temporarily stored, or cached, copies of website content to users, based on the user's geographic location. A CDN stores this content in distributed locations and reduces the distance between your website visitors, and your website server.
- It also reduces the traffic, load and amount capacity needed at the host server (content server) to serve all the users.
- Also increases the uptime of the host server as less users are interacting with it.
- Also results in increase in security through obscurity.

##### In this lesson, you have learned

- Cloud storage is available in four main types–Direct Attached, File, Block, and Object Storage. These storage types differ in how they can be accessed, the capacity they offer, how much they cost, the types of data they are best suited to store, and their read-write speed.
- Direct Attached (or Local) Storage is storage that is presented directly to a cloud-based server and is effectively either within the host server chassis or within the same rack.
- File Storage is typically presented to compute nodes as a Network File System (NFS), which means that the storage is connected to compute nodes over a standard ethernet network.
- Block Storage is presented to compute nodes using high-speed fiber connections, typically provisioned in volumes, which are mounted onto a compute node.
- Object Storage is accessed via an API and doesn’t need an underlying compute node.
- Object Storage offers infinite capacity as you can keep adding files to it and just pay for what you use. Compared to the other storage types, object storage is slowest in terms of read and write speeds.
- A Content Delivery Network (CDN) is a distributed server network that accelerates internet content delivery by delivering temporarily stored or cached copies of website or media content to users based on their geographic location.

## Week 4

### Hybrid Multi-Cloud, Microservices, and Serverless

### Hybrid Multi-Cloud

- Hybrid cloud, as we covered in the previous lesson, is a computing environment that connects an organization's on-premise private cloud and third-party public cloud into a single infrastructure for running the organization's applications.
- Multi-cloud is a cloud adoption strategy that embraces a mix of cloud models from different service providers, public, private, and managed, across infrastructure, platform, or software services.

Use Cases:

- Cloud Scaling:
- Composite Cloud
- Modernize
- Data and AI
- Prevent lock-in to a specific vendor's cloud platform.

### Microservices

- Microservices architecture is an approach in which a single application is composed of many loosely coupled and independently deployable smaller components or services. These services typically have their own stack running on their own containers. They communicate with one another over a combination of APIs, event streaming, and message brokers.
- For a business, what this means is that application components can be developed and updated more efficiently by multiple developers working independently. Teams can use different stacks and runtime environments for different components. Components facing too much load can be scaled independently, reducing the waste and cost associated with having to scale entire applications.
- A container is the distribution method for each microservice, meaning it delivers the code where it needs to go. Containers are plug-and-play, so if one microservice isn't working for an application, developers can take it out and put in a different one without disrupting how the rest of the app functions.
- Service Discovery: a roadmap microservices to communicate. When microservices find each other, they communicate using an application programming interface or an API.

### Serverless

- Serverless is an approach to computing that offloads responsibility for common infrastructure management tasks such as scaling, scheduling, patching, and provisioning application stacks to cloud providers.
- Serverless doesn't mean there are no servers, only that the management of the underlying physical or virtual servers is removed from their users.

Key Attributes

- The serverless model requires no provisioning of servers, installation of application stacks and software or operation of the infrastructure by the developer.
- Serverless computing runs code only on-demand on a per request basis.
- Serverless enables end users to pay only for resources being used, never paying for idle capacity, which is unlike virtual servers on the cloud, where end users pay for VMs as long as they are running, even if idle.

Applications that qualify for a serverless architecture include some of the following characteristics, short-running stateless functions, seconds or minutes, seasonal workloads with varying off peak and peaks, production volumetric data that shows too much idle time, event-based processing or asynchronous request processing for implementing use cases.

##### In this lesson, you have learned:

- Hybrid multi-cloud is a cloud adoption strategy that makes it possible for public clouds, private clouds, and on-premises IT to interoperate seamlessly while leveraging the best cloud-based services from different public cloud providers.

- Microservices architecture is an approach in which an application is built as a collection of loosely coupled and independently deployable components or services, leading to efficient development, maintenance, and upgradation cycles.

- Serverless computing is an approach to computing that offloads responsibility for common infrastructure management tasks for application runtimes to cloud providers, allowing developers to focus their time and effort on development and testing, and not have to worry about provisioning, maintaining and scaling compute resources.

### Cloud Native Applications, DevOps, and Application Modernization

### Cloud Native Applications

- Cloud native application is an application developed from the outset to to work only in the cloud environment, or an existing app that has been refactored and reconfigured with cloud native principles.

- A cloud native application consists of microservices.
- Microservices Architectural approach: break applications down to single-function microservices.

- Different components of Cloud Native Apps:
  - Cloud infrastructure: private, public, or enterprise infrastructure
  - Scheduling and Orchestration: control planes, like kubernetes.
  - Application and Data Services: being able to integrate our application code with existing services that may be available on other clouds, or even on-premise.
  - Application runtime: middleware
  - Application Code
- Benefits:
  - Innovation
  - agility
  - commoditization

### DevOps

- Development teams need to design, develop, deliver, and run software as reliably and efficiently as possible. Operations teams need to identify and resolve problems as soon as possible by monitoring, predicting failure, managing the environment, and fixing issues. Combining development and operations with the ability to monitor and analyze and optimize bottlenecks gives us DevOps.
- A DevOps approach applies agile and lean thinking principles to all stakeholders in an organization who develop, operate, or benefit from the business's software systems, including customers, suppliers, partners.
- DevOps capabilities improve productivity through
  - accelerated customer feedback cycles.
  - Unified measurements and collaboration across an enterprise.
  - reduced overhead, duplication, and rework.
- The DevOps process involves
  - continuous delivery, which is about delivering small, well-designed, high quality increments of software to customers.
  - Continuous integration, creating packaged builds of the code changes released as immutable images. Where immutable implies that when modifications are needed, the entire component is replaced with an upgraded version.
  - Continuous deployment, which involves progressing each new packaged build through the deployment lifecycle as rapidly as possible.
  - Continuous monitoring with tools that help developers understand the performance and availability of their applications even before they are deployed to production.
  - Delivery pipeline, which is an automated sequence of steps that involves the stages of ideation, coding, building, deploying, managing, and continuous improvement, which loops back to the ideation phase in the delivery pipeline.

Harnessing the Power of DevOps on Cloud Platforms
Introduction:
Organizations strive to deliver software solutions swiftly, reliably, and efficiently in our ever-evolving digital landscape. DevOps, a collaborative approach that unifies software development and operations, has emerged as a significant change. This topic will explain the essence of DevOps, explore its benefits when applied to cloud platforms, and provide real-world use cases that demonstrate its transformative capabilities on popular cloud providers such as AWS, Azure, GCP, and IBM Cloud.

What is DevOps?
DevOps is an approach that fosters collaboration between development and operations teams, streamlining the entire software delivery lifecycle. By promoting a culture of collaboration, automation, and continuous feedback, DevOps enables organizations to deliver software products more efficiently and reliably.

The DevOps Process:
To better understand the DevOps process, let's explore its key components:

Continuous Integration (CI): Developers integrate their code changes into a shared repository frequently, ensuring early detection of integration issues. Version control systems like Git and Subversion support this process.

Continuous Delivery (CD): Continuous delivery ensures that code changes are always in a state that can be released immediately. This state allows organizations to deploy software anytime with minimal manual intervention. Tools like Jenkins and Bamboo facilitate the automation of build, test, and deployment processes.

Continuous Deployment (CDep): Continuous deployment takes automation further, enabling organizations to automatically deploy software changes into production environments after passing the necessary tests.

Continuous Monitoring (CM): Continuous monitoring provides real-time insights into application and infrastructure performance, allowing organizations to detect issues promptly and take proactive measures. Tools like Prometheus and ELK Stack are commonly used for monitoring in DevOps.

Benefits of DevOps on Cloud Platforms:
Implementing DevOps practices on cloud platforms offers several significant advantages:

Scalability and Flexibility:
Cloud platforms provide the scalability and flexibility required for DevOps workflows. Organizations can leverage cloud resources to scale infrastructure dynamically, accommodate varying workloads, and optimize resource utilization based on demand.

Rapid Provisioning and Deployment:
DevOps on the cloud facilitates rapid provisioning and deployment of infrastructure and applications. Cloud services offer pre-configured environments, automated provisioning, and deployment pipelines, enabling faster time-to-market and reducing manual effort.

Cost Optimization:
Cloud-based DevOps enables cost optimization by leveraging the pay-as-you-go model. Organizations can scale resources up or down based on demand, eliminating the need for upfront infrastructure investments, and reducing operational costs.

Collaboration and Team Efficiency:
DevOps practices on the cloud foster collaboration and enhance team efficiency. Cloud platforms provide centralized repositories, version control systems, and collaboration tools that facilitate seamless communication and shared code repositories, enabling effective collaboration across teams.

Continuous Integration and Delivery:
Cloud services seamlessly integrate with popular DevOps tools, enabling continuous integration and delivery (CI/CD). This automation streamlines build, test, and deployment processes, reducing errors and facilitating faster, more reliable software releases.

DevOps Use Cases on Cloud Platforms
Let's explore real-world use cases that highlight the benefits of DevOps on different cloud platforms:

DevOps on Amazon Web Services (AWS):
Organizations leveraging DevOps on AWS can take advantage of services such as AWS CodePipeline for CI/CD pipelines, AWS Elastic Beanstalk for simplified application deployment, and AWS Lambda for serverless computing. This use case enables seamless scalability, efficient resource management, and rapid delivery of software solutions.

DevOps on Microsoft Azure:
DevOps on Azure empowers organizations with services like Azure DevOps for collaboration, Azure Kubernetes Service (AKS) for container orchestration, and Azure Functions for serverless computing. Organizations can achieve automated deployments, efficient scaling, and improved application performance by leveraging these services.

DevOps on Google Cloud Platform (GCP):
DevOps on GCP offers services such as Cloud Build for CI/CD pipelines, Google Kubernetes Engine (GKE) for container management, and Cloud Functions for serverless computing. This use case enables organizations to automate infrastructure provisioning, manage complex containerized applications effectively and optimize resource utilization.

DevOps on IBM Cloud:
DevOps on IBM Cloud provides services like IBM Continuous Delivery for automated deployments, IBM Kubernetes Service (IKS) for container orchestration, and IBM Functions for serverless computing. These use cases allow organizations to achieve streamlined software delivery, efficient infrastructure management, and seamless scaling on the IBM Cloud platform.

Conclusion
When combined with cloud platforms, DevOps empowers organizations to streamline software delivery, enhance collaboration, and leverage scalable resources. By implementing DevOps on popular cloud providers such as AWS, Azure, GCP, and IBM Cloud, organizations can accelerate their software delivery cycles, reduce time-to-market, and adapt to changing business needs effectively. It is a winning combination that enables organizations to stay competitive in today's fast-paced digital landscape

### Application Modernization

This is happening at 3 fronts (past -> present -> future):

- Architecture: Monoliths -> Service oriented Architecture -> Microservices
- Infrastructure: Physical Servers -> VM -> Cloud
- Delivery: Waterfall -> Agile -> DevOps (or Site Reliability Engineering)

##### In this lesson, you have learned:

Cloud native applications are applications that are built or refactored to work in the cloud environment. These applications, developed using DevOps methodologies, consist of microservices packaged in containers that can run in any environment—making it possible to create and update features in quick iterative cycles.

DevOps is a collaborative approach that enables development and operations teams to continuously deliver software in quick iterative cycles while reducing overhead, duplication, and rework. DevOps’ tools, practices, and processes help tackle the complexities and challenges posed by the cloud, allowing solutions to be delivered and updated quickly and reliably.

Application modernization helps organizations accelerate their digital transformation, take advantage of new technologies and services, and become more responsive to changing market dynamics. Cloud computing is one of the key enablers of application modernization.

## WEEK 5

### What is Cloud Security - Part 1

- A DDoS attack targets the server on the enterprise by overloading it with traffic from multiple synchronized systems. The attack works through Simple Network Management Protocol (SNMP) used for modems, printers, switches, routers, and servers.
- Different security models used in cloud computing:
  - A shared responsibility model is a cloud security framework where the organization hands off certain IT security responsibilities to the cloud computing provider. Each party, the cloud provider and the user are accountable for different aspects of the security, and they work together for the full security coverage. There are different types of shared security models for IaaS, PaaS, and SaaS. In IaaS, the provider looks after the physical security of the infrastructure at their data centers. IaaS users are responsible for the security of the software including the OS required to run their applications and their data. In PaaS, the provider secures the platform including the OS, user subscriptions and login credentials, but the user is responsible for the security of any code or data -- or other content -- produced on the platform. However, in SaaS, the provider is responsible for almost every aspect of security, including underlying infrastructure, service application, and the data the application produces. Users still have some security responsibilities such as protection of login credentials.

### What is Cloud Security - Part 1

- To secure data, you can improve maturity across people, process, and technology. Identify your most critical data assets, who has access to them, and how they are protected. You can prevent data loss by detecting, preventing, and enforcing policy violations to avoid accidental data loss. Implement data security governance by establishing process, metrics, and continuous steady-state data discovery and classification.
- management of access controls and authentication: develop Cloud identity and access management (IAM) strategies that provide and work on zero trust architecture, risk protection, and constantly authenticate any user to any resource.
- Another element of cloud security is cloud network security which refers to the security measures, technology, policies, controls, and processes used to protect data on public, private, and hybrid cloud networks.
- There are some critical steps under three phases that you can follow. First is identifying your cloud usage state and risks. Second is protecting your cloud system, and third is responding to attacks.
- The first phase comprises: Identifying how your data is accessed Detecting unknown cloud usage Checking your configurations for cloud services Monitoring for signs of malicious usage of cloud data.
- In the second phase, you can protect your cloud system by: Assigning protection policies Encrypting sensitive data Formulating policies for data sharing Restricting data sharing to unknown devices Implementing a bot protection and mitigation solution Using a proper anti-malware solution
- The third phase offers best practices for responding to attacks and attempts to attack: Add additional authentication and verification steps for high-risk access scenarios Add new policies for new cloud services.

- NIST's five pillars of a cybersecurity framework: Identify, Protect, Detect, Respond, and Recover.

- Another emerging technology in cloud security that supports cybersecurity framework is cloud security posture management (CSPM). CSPM solutions are designed to address a common error in many cloud environments, that is, misconfigurations. CPSM also addresses issues by helping in the deployment of the core components of cloud security. They include identity and access management (IAM), regulatory compliance management, traffic monitoring, threat response, risk mitigation, and digital asset management.
- The current major trend in cloud security includes multi-cloud strategies such as cybersecurity mesh, zero-trust security models, hybrid and multi-cloud environment, cloud-native tools and applications, deployment of DevSecOps, securing remote workforces, and AI and machine learning for threat detection.

### Policies and Principles of Access Management

#### Policies

- A policy in cloud security refers to a set of rules and guidelines that determine how users should access and protect resources within a cloud environment. These policies provide a framework for maintaining security, ensuring compliance with industry regulations, and mitigating potential risks.

- The format of a policy typically includes the following:

  - A title that provides a descriptive name or identifier for the policy
  - The scope of the policy, which defines the specific resources, systems, or individuals to which the policy applies
  - The objective of the policy, or its goals and purpose
  - A policy statement that lists the rules, procedures, and restrictions of the policy
  - The roles and responsibilities of the individuals and groups that are enforcing and adhering to the policy
  - Compliance and enforcement details or the measures taken to monitor and ensure policy compliance
  - A review and revision section which outlines how often to review and update the policy to remain relevant and effective

#### Service provider and customer-managed policies

- Cloud service providers (CSPs) typically have security policies that govern the overall security of their infrastructure, data centers, and services. These policies ensure a baseline level of security and protection for customer data. Service provider policies cover various aspects such as physical security, network security, data encryption, access controls, and incident response.

- In addition to service provider policies, customers can implement their own policies, also known as customer-managed policies. These policies allow customers to tailor security measures according to their requirements, industry regulations, and risk tolerance. Customer-managed policies can include additional security controls, access restrictions, data protection measures, and compliance frameworks.

- By combining service provider and customer-managed policies, organizations can establish a comprehensive security framework that aligns with their unique needs while benefiting from the underlying security measures provided by the cloud service provider.

#### Principle of Least Privilege

The principle of least privilege is a key concept in access control that minimizes the risk of unauthorized access or accidental misuse of resources. It dictates that organizations should grant users only the minimum necessary permissions required to perform their tasks. By following the principle of least privilege, organizations limit the potential damage caused by compromised user accounts.

#### User Access Level

- In a cloud environment, user access levels vary depending on their roles and responsibilities. Some users may only need access to the console, or the graphical user interface (GUI) provided by the cloud service provider for resource management and configuration. These users interact with the cloud through the console to perform tasks such as provisioning resources, monitoring, and administration.

- On the other hand, users involved in software development may require access to the development environment. This environment includes tools, APIs, and services necessary for building, testing, and deploying applications in the cloud. These users interact with the cloud infrastructure using APIs and command-line interfaces (CLIs) rather than relying solely on the console.

- Depending on the organization’s requirements, certain users may have access to both the console and development environment, enabling them to perform a broader range of tasks and responsibilities.

#### Identity and Access Management (IAM)

- Identity and Access Management (IAM) enables organizations to manage and authenticate users’ identities and access to resources in a cloud environment. It involves the processes and policies that ensure that only authorized individuals have access privileges to sensitive systems, applications, and data. IAM simplifies user management by centralizing user provisioning, authentication, and authorization processes, making granting or revoking access rights easier as needed. This process helps organizations enhance security, protect sensitive information, enforce compliance with regulations, and streamline administrative tasks related to user access.

#### Standard Password Policy

- A standard password policy for users logging into the cloud should adhere to best practices to ensure strong password security. Typically, a password policy includes requirements for password complexity, such as a minimum length and a combination of upper and lowercase letters, numbers, and special characters. The policy may also define password expiration intervals, after which users must change their passwords. Additionally, enforcing a password history, which is a required number of unique passwords used before reusing an old password, adds an extra layer of protection against password reuse. Other password policies may include account lockout, multi-factor authentication, and user awareness and training. The specific requirements of a password policy will depend on the organization’s needs, requirements, and risk assessments.

#### Identity provider standards (SAML, OpenID)

- Identity provider standards are protocols and frameworks that define how identity providers (IdPs) and service providers (SPs) securely exchange authentication and identity information. These standards ensure consistent and standardized approaches to authentication and access management. Two widely used identity provider standards are:

  - Security Assertion Markup Language (SAML) - SAML is an XML-based standard for exchanging authorization and authentication data between IdPs and SPs. It enables secure single sign-on (SSO) and identity federation. SAML allows users to authenticate once with their IdP and access multiple SPs without needing separate authentication. SAML assertions contain information about the user’s identity and attributes, which SPs rely on to grant access to their resources.

  - OpenID Connect - OpenID Connect is a modern standard built on the OAuth 2.0 protocol. It provides a framework for authentication and identity federation. OpenID Connect allows users to authenticate using their chosen OpenID provider and obtain an ID token that contains information about their identity. Service providers can use the ID token to authenticate users and provide access to their resources.

- These identity provider standards offer secure and interoperable solutions for managing authentication and access control in various contexts, including cloud environments, web applications, and enterprise systems. They enable organizations to establish trust relationships between identity providers and service providers, simplify user authentication experiences, and enhance security by centralizing identity management.

### Identity and Access Management (IAM)

- There are three main types of users: Administrative Users, Developer Users, and Application Users.
- key components of identity and access management, and how they work.
  - Authentication, or the identity service, enables applications deployed to the cloud to authenticate users at an application level, based on a range of identity providers such as the cloud directory, social identity providers such as Google, LinkedIn, Facebook, and Twitter, enterprise-hosted identity provider, and cloud-hosted identity provider.
  - Multifactor authentication is used to combat identity theft by adding an additional layer of authentication for application users, such as single-use passwords or pins, certificates, tokens, risk-based authentication, (such as changes in the user’s location, past activity, and preferences.)
  - Cloud Directory services are used to securely manage user profiles and their associated credentials and password policy inside a cloud environment. A directory service within a cloud means that applications hosted on the cloud do not need to use their own user repository.
  - Reporting helps provide a user-centric view of access to resources or a resource-centric view of access by users. Reports typically give information about which users have access to which resources, which users have changes in access rights, which access is being exploited by each user, and under which conditions.
  - Audit and compliance is a critical service within identity and access management framework, both for cloud provider, and cloud consumer. Auditors use these processes to validate implemented controls against an organization's security policy, industry compliance, and risk policies--and to report deviations.
  - User and service access management capability enables cloud application and service owners to provision and de-provision customer, partner, and vendor user profiles with minimal human interaction.
- Some of the controls that can help secure these sensitive accounts include: provisioning users by specifying roles on resources for each user; password policies that control the usage of special characters, minimum password lengths and other similar settings; multifactor authentication like time-based one-time passwords; and immediate de-provisioning of access when users leave or change roles.
- create access groups, add users to access groups, and manage access for existing users. An access group is a group of users and service IDs created so that the same access can be assigned to all entities within the group with one or more access policies. Access policies define how users, service IDs, and access groups in the account are given permission to access account resources. Policies include: a subject, which can be users, service IDs, or access groups; a target, which is the resource or provisioned service offering, to which you want to provide access; and role, which defines the actions allowed on the target of the policy, that is, the resource to which the access is being granted.

### Cloud Encryption

- encryption plays a key role and is often referred to as the last line of defense in a layered security model.
- Encryption is defined as scrambling data in a way that makes it illegible. There are two parts to an encryption system, the encryption algorithm and the decryption key. The encryption algorithm defines the rules by which data will be transformed so that it becomes illegible. And the decryption key defines how the encrypted data will be transformed back to legible data.
- Data needs protection in three states: at rest, in transit, and when it is in use. Encryption at rest protects data while it is physically stored in a database or the storage layer. Depending on the application and business requirements, there could be multiple options for encrypting data at rest, such as encryption for block and file storage, built-in encryption, in object storage, and database encryption services. Encryption in transit protects data while it is transmitted from one location to another. Encryption in transit includes encrypting the data before transmission, authenticating endpoints, and decrypting and verifying data on arrival. Secure Sockets Layer or SSL and Transport Layer Security, TLS are commonly used protocols for encryption in transit. They are not only used when accessing websites securely, but also for data moving between servers and services within the cloud. Encryption in use protects data when it is in use in memory for computations. It allows computations to be performed on encrypted text without needing to decrypt the data.
- Cloud storage encryption could be server-side or client-side. Server-side encryption occurs after Cloud storage receives your data, but before the data is written to disk and stored. For server-side encryption you can either create and manage your own encryption keys, known as customer supplied encryption keys, or you can generate and manage your encryption keys using key management services offered by the cloud storage provider, known as customer managed encryption keys. Client-side encryption occurs before data is sent to Cloud storage. This way, users can utilize encryption keys and algorithms that are not visible to the cloud provider, making it virtually impossible for cloud providers to decrypt hosted data.
- Encryption does not eliminate data security risk, it separates the security risk from the data itself by moving security to the encryption keys. These keys need to be managed and protected against threats in order to keep the data secure. Key management services offered by some cloud providers help perform lifecycle management for encryption keys that are used in cloud services or customer-built applications.

### Cloud Monitoring Services

- Cloud monitoring solutions assess data, application, and infrastructure behaviors for: performance, resource allocation, network availability, compliance, and security risks and threats.
- Cloud monitoring helps to: Accelerate the diagnosis and resolution of performance incidents. Control the cost of your monitoring infrastructure. Mitigate the impact of abnormal situations with proactive notifications. Get critical Kubernetes and container insights for dynamic microservice monitoring. Troubleshoot your applications and infrastructure
- They provide: Data in real-time with round the clock monitoring of virtual machines, services, databases, and applications. Multilayer visibility into application, user, and file access behavior across all cloud-based applications and services. Advanced reporting and auditing capabilities for ensuring regulatory standards are being met. Large-scale performance monitoring integrations across multicloud and hybrid cloud environments.
- One way to categorize cloud monitoring tools solutions is to break them down into Infrastructure, Database, and Application Performance monitoring. Infrastructure monitoring tools help identify minor and large-scale hardware failures and security gaps so that developers and administrators can take corrective action before problems affect user experience. Database monitoring tools help track processes, queries, and availability of services to ensure the accuracy and reliability of database management systems. Application Performance Monitoring, or APM, measures application availability and performance, providing tools needed to troubleshoot issues in an application's environment. APM solutions help improve user experience, meet application and user service level agreements (SLAs), minimize downtime, and lower overall operational costs.
- To get the most benefit from your cloud-based deployments, you can follow some standard cloud monitoring best practices. Leverage end-user experience monitoring solutions to capture the performance of an application from the point of view of its end users. These solutions monitor user journeys to track parameters such as application response time and frequency of use under varied conditions. These insights will help you to improve customer experience significantly. Consider moving all aspects of your infrastructure, whether in private, public or hybrid clouds, under one unified monitoring platform. This can help you to manage all your KPIs in one place with complete visibility into performance optimization. Use monitoring tools that can help you track the usage and cost of your cloud resources and services. Increase cloud monitoring automation. This can help you gain significant operational efficiencies. Simulate outages and breach scenarios to evaluate how well your monitoring tools capture and alert against failures.

### Cloud Monitoring and Benefits

#### Introduction:

- Cloud computing has transformed the business landscape, offering scalability, flexibility, and cost-efficiency. However, it also introduces unique challenges in ensuring the security, performance, and availability of cloud-based services. Monitoring plays a critical role in proactively detecting and addressing potential issues. In this blog post, we will explore how monitoring can be achieved in the cloud using techniques such as alarms, logs, metrics, events, and service-based monitoring, including Infrastructure as Code (IaC).

- IaC has emerged as a powerful approach to automate the provisioning and configuration of cloud resources. With IaC, organizations define their infrastructure requirements through code, allowing consistent and repeatable deployments. Monitoring IaC deployments is crucial in ensuring a strong infrastructure that can detect any configuration drift. By incorporating IaC monitoring alongside other monitoring approaches, organizations can achieve greater control and visibility over their cloud infrastructure.

- Additionally, we will delve into the importance of tracking API calls for audit purposes. API calls are a gateway for interacting with various cloud services, making the calls crucial for security and compliance. Organizations can maintain an audit trail by tracking and storing API calls, ensuring transparency, accountability, and regulatory compliance. Furthermore, we will discuss attacks, vulnerabilities, risks, and mitigation measures associated with cloud monitoring to provide a comprehensive understanding of the potential risks and the steps needed to mitigate them effectively.

- Through this exploration, we aim to equip readers with the knowledge and insights to establish robust cloud monitoring practices, effectively track API calls, and mitigate potential risks. By embracing comprehensive monitoring strategies, including service-based and IaC monitoring, organizations can optimize their cloud infrastructure, enhance security, and deliver exceptional services in the dynamic and ever-evolving cloud environment.

1. The Fundamentals of Cloud Monitoring:
   Monitoring in the cloud environment encompasses several vital components. Alarms are set to be proactive for specific events or thresholds, enabling organizations to respond promptly to critical situations. Logs are essential in collecting and analyzing data to gain insight into system behavior. Log management services provide efficient storage and retrieval capabilities, while log aggregation and analysis tools help detect anomalies and troubleshoot issues.

Metrics allow organizations to collect and visualize performance data through cloud-provided metrics. Establishing baseline metrics makes it easier to identify anomalies and make informed decisions. Monitoring dashboards offer real-time visibility into system health, enabling quick responses to potential issues.

Events capture and process real-time events within the cloud infrastructure. Event-driven architectures leverage them to trigger actions based on specific criteria. Organizations can efficiently mitigate potential threats by integrating event monitoring with incident response workflows.

2. Service-Based Monitoring for Enhanced Cloud Management:
   Service-based monitoring focuses on specific cloud services to optimize performance and ensure efficient resource utilization. Load balancing monitoring involves tracking workload distribution and identifying potential bottlenecks. Alarms monitor load balancer health and performance issues, enabling organizations to respond promptly.

Content delivery monitoring involves monitoring content delivery networks (CDNs) for efficient content distribution. Performance, latency, and cache hit rates are proactively tracked to ensure an optimal user experience. In the event of content delivery issues, troubleshooting measures can rectify the situation promptly.

Auto-scaling monitoring is essential for dynamically adjusting resource capacity in response to changing demands. By monitoring auto-scaling groups, organizations can track scaling events and evaluate the effectiveness of scaling policies. Coordination between monitoring and scaling activities ensures seamless scalability.

Infrastructure as Code (IaC) monitoring is critical for organizations utilizing automation and provisioning resources through code. Monitoring IaC deployments enables verification of infrastructure changes and detects any drift from the desired state. Configuration issues need to be identified and rectified promptly to maintain the integrity of the infrastructure.

3. Tracking API Calls for Audit Purposes:
   API monitoring is essential for security and compliance in cloud environments. Organizations must recognize the significance of API calls and the risks associated with unauthorized or malicious API activity. By implementing API monitoring, organizations can configure audit trails and access controls to track API activities. Analyzing logs and detecting anomalies help identify suspicious API behavior, ensuring transparency and accountability in cloud service usage.

The following are examples of cloud services that track API calls.

- Amazon Web Services (AWS) CloudTrail: AWS CloudTrail is a service that enables organizations to monitor, log, and retain API activity across their AWS accounts. It records API calls made to AWS services and provides detailed information such as the caller's identity, the time of the API call, and the parameters used. By enabling CloudTrail, organizations can maintain an audit trail of API activities, ensuring transparency and accountability. The CloudTrail logs are analyzed to identify unauthorized or suspicious API behavior.

- Google Cloud Audit Logging: Google Cloud Platform (GCP) provides Audit Logging, which captures API calls and system events across various GCP services. It allows organizations to track activities related to resource creation, deletion, modification, and access control changes. Audit Logging provides detailed logs that are monitored and analyzed to detect anomalous API behavior. By leveraging Audit Logging, organizations can maintain an audit trail for API activities and enforce compliance with security policies.

- Microsoft Azure Activity Logs: Azure Activity Logs record API calls and other administrative actions performed. These logs capture the operation type, resource actions, and the caller's identity. By enabling Azure Activity Logs, organizations can track API activities, detect unauthorized or malicious behavior, and maintain an audit trail for compliance.

- Salesforce Event Monitoring: Salesforce offers Event Monitoring, a service that logs API calls and user activities within the Salesforce platform. It provides detailed information about API operations, user logins, data exports, and other system events. Event Monitoring enables organizations to track API activities, monitor user behavior, and identify potential security risks or policy violations.

These examples highlight how specific cloud services can track API calls and maintain audit trails. Organizations can effectively monitor and analyze API activities by utilizing services like AWS CloudTrail, Google Cloud Audit Logging, Azure Activity Logs, and Salesforce Event Monitoring, ensuring transparency, accountability, and compliance with security policies and regulations.

4. Likely Attacks, Vulnerabilities, Risks, and Mitigation Measures:
   Cloud environments are susceptible to various attacks and vulnerabilities. Distributed Denial of Service (DDoS) attacks can overwhelm cloud resources with excessive traffic, leading to disruptions. Data breaches risk unauthorized access to sensitive data stored in the cloud. Misconfigurations, such as insecure or improper setup of cloud services, can also expose vulnerabilities.

To mitigate these risks, organizations must implement strong authentication and access controls. Data encryption at rest and in transit is crucial for protecting sensitive information. Regular vulnerability assessments and penetration testing help identify potential weaknesses while monitoring network traffic and behavior analytics enable the detection of anomalies and early response to potential threats.

Cloud environments face various attacks, vulnerabilities, and risks. Let's explore some examples:

- Distributed Denial of Service (DDoS) Attacks: DDoS attacks aim to overwhelm cloud resources by flooding them with excessive traffic, leading to service disruptions. Cloud service providers offer services that help mitigate DDoS attacks. For instance, AWS provides AWS Shield, a managed DDoS protection service. It automatically detects and mitigates DDoS attacks, ensuring the availability of cloud resources even during an attack. Similarly, Google Cloud offers the Cloud Armor service, which protects against DDoS attacks through global HTTP(S) load balancing and security system rules.

- Data Breaches: Data breaches pose a significant risk in cloud environments, as they can result in unauthorized access to sensitive data stored in the cloud. Cloud service providers offer robust security measures to protect data. For example, Microsoft Azure provides Azure Key Vault, enabling organizations to store and manage cryptographic keys and secrets securely. AWS offers AWS Key Management Service (KMS), allowing organizations to encrypt data at rest and control access to encryption keys.

- Misconfigurations: Misconfigurations in cloud services can lead to security vulnerabilities and expose sensitive data to unauthorized access. For example, misconfigured access control policies or open storage buckets can provide unintended access to data. Cloud service providers often offer security configuration tools and services. AWS provides AWS Config, allowing organizations to continuously assess and audit resource configurations. Google Cloud delivers Cloud Security Command Center, a centralized security management and data risk assessment platform.

- Insider Threats: Insider threats involve unauthorized or malicious actions by individuals with legitimate access to cloud resources. These individuals may intentionally abuse their privileges or inadvertently cause security incidents. Cloud service providers offer identity and access management services to mitigate insider threats. For instance, Azure Active Directory provides robust authentication and access controls to ensure only authorized users can access resources.

#### Conclusion: 

Monitoring is vital to cloud management, ensuring cloud-based services' security, performance, and availability. Organizations can proactively address potential issues and optimize their cloud infrastructure by utilizing techniques such as alarms, logs, metrics, events, service-based monitoring, and tracking API calls for audit purposes. Understanding attacks, vulnerabilities, risks, and mitigation measures help organizations fortify their cloud environment. Robust monitoring practices and thorough audit trail tracking are essential for maintaining a secure and efficient cloud ecosystem. By embracing comprehensive cloud monitoring strategies, organizations can optimize their cloud infrastructure and deliver exceptional services while mitigating potential risks.

### Case Studies and Jobs
