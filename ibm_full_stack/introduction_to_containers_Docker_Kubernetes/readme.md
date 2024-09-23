## Week 1

### Introduction to Containers

Cloud-native is the newest application development approach for building scalable, dynamic, hybrid cloud-friendly software. Container technology is a powerful part of that approach.

Containers solve the problem of making software portable so that applications can run on multiple platforms.
A **container**, powered by the containerization engine, is a standard unit of software that encapsulates the application code, runtime, system tools, system libraries, and settings necessary for programmers to build, ship, and run applications efficiently.

Operations and underlying infrastructure issues are no longer blockers. You can quickly move applications from your laptop to a testing environment, from a staging environment to a production environment, from a physical machine to a virtual machine, or a private cloud or public cloud, and always know that your application will work correctly.

Challenges with traditional environments:

- In traditional environments, developers can’t isolate the app and allocate or designate specific storage and memory resources for apps on physical servers.
- Servers are often underutilized or overutilized, leading to poor utilization and a poor return on investment.
- Traditional deployments require comprehensive provisioning resources and expensive maintenance costs.
- The limits of physical servers can constrain application performance during peak workloads.
- Applications are not portable across multiple environments and operating systems.
- Implementing hardware for resiliency is often time-consuming, complex and expensive.
- Traditional on premises IT environments have limited scalability.
- Automation is challenging when distributing software to multiple platforms and resources using traditional environments.

**Container engines** virtualize the operating system and are responsible for running containers. **Platform-independent containers** are lightweight, fast, isolated, portable, and secure and often require less memory space. Binaries, libraries, and other entities within the container enable apps to run, and one machine can host multiple containers.

Containers enable organizations to:

- Quickly create applications using automation.
- Lower deployment time and costs.
- Improve resource utilization, including CPU and memory.
- Port across different environments, and support next-gen applications, including microservices.

Challenges of containerization:

- Server security can become an issue if its operating system is affected.
- Developers can become overwhelmed when managing thousands of containers.
- Converting monolithic legacy applications can be a complex process.
- Developers can experience difficulty right-sizing containers for specific scenarios.

Some of the more popular container vendors:

- **Docker** is a robust platform and the most popular container platform today.
- **Podman** is a daemon-less container engine that is more secure than Docker.
- Developers often prefer **LXC** for data-intensive applications and operations.
- **Vagrant** offers the highest levels of isolation on the running physical machine.

### Introduction to Docker

Docker is an open platform for developing, shipping, and running applications as containers.

Features of Docker:

- Docker isolates applications from infrastructure, including the hardware, the operating system, and the container runtime.
- Docker is written in the Go programming language.
- Docker uses Linux kernel features to deliver its functionality.
- Docker also uses *namespaces* to provide an isolated workspace called **the container**.
- Docker creates a set of namespaces for every container and each aspect runs in a separate namespace with access limited to that namespace.

Docker methodology has inspired additional innovations, including:

- Complementary tools such as Docker CLI, Docker Compose, and Prometheus, and various plugins, including storage plugins;
- Orchestration technologies using Docker Swarm or Kubernetes;
- Development methodologies using microservices and serverless.

Docker offers the following benefits:

- Docker’s consistent and isolated environments result in stable application deployments. Deployments occur in seconds.
- Because Docker images are small and reusable, they significantly speed up the development process.
- Docker automation capabilities help eliminate errors, simplifying the maintenance cycle.
- Docker supports Agile and CI/CD DevOps practices.
- Docker’s easy versioning speeds up testing, rollbacks, and redeployments.
- Docker helps segment applications for easy refresh, cleanup, and repair.
- Developers collaborate to resolve issues faster and scale containers when needed.
- Docker images are platform-independent, so they are highly portable.

Docker is not a good fit for applications with these qualities:

- Require high performance or security,
- are based on Monolith architecture,
- use rich GUI features, or perform standard desktop or limited functions.

### Docker Objects

Docker contains objects such as the Dockerfile, images, container, network, storage volumes, and other objects, such as plugins and add-ons.

A **Dockerfile** is a text file that contains instructions needed to create an image.

A **Docker Image** is a read-only template with instructions for creating a Docker container. The Dockerfile provides instructions to build the image. Each Docker instruction creates a new layer in the image. When you change the Dockerfile and rebuild the image, the Docker engine only rebuilds the changed layers. Images can share these layers, which saves a lot of disk space as well as network bandwidth when sending and receiving images. When you instantiate this image, you get a running container. At this point, a writeable container layer is placed on top of the read-only layers. The writeable layer is needed because containers are not immutable as images.

How images are named:

- An image name has a unique format that consists of three parts: the hostname, the repository, and the tag. The _hostname_ identifies the image registry. A _repository_ is a group of related container images. The _tag_ provides information about a specific version or variant of an image. Example: docker.io/ubuntu:18.04.

What is a Docker container?

- A Docker container is a runnable instance of an image. You can use the Docker API or CLI to create, start, stop, or delete an image. You can connect to multiple networks, attach storage to the container, or create a new image based on its current state. Docker keeps containers well isolated from each other and their host machine.
- When using Docker, networks help isolate container communications. By default, data doesn’t persist when the container no longer exists. Docker uses volumes and bind mounts to persist data even after a container stops. Plugins, such as storage plugins, provide the ability to connect to external storage platforms.

### Docker Architecture

The Docker client-server architecture provides a complete application environment. Docker components include the client, the host, and the registry.Let’s take a high-level view of how Docker works.

- You’ll use either the Docker command line interface or REST APIs via the Docker client to send instructions to the Docker host server, commonly called the _host_. The Docker host contains the daemon, known as **dockerd**. The daemon listens for Docker API requests or commands such as “docker run” and processes those commands. The daemon does the heavy lifting to build, run, and distribute Docker containers. Then, Docker stores the container images in a registry.

The Docker host also includes and manages: Images Containers Namespaces Networks Storage Plugins and add-ons. You can use the Docker ​ client to communicate with local ​ and remote Docker hosts. You can run the Docker client and daemon on the same system or​ connect your Docker client to a remote Docker daemon.​ And Docker daemons can also communicate with other daemons to manage Docker services.

Docker stores and distributes images in a registry. Registry access is either public, such as Docker Hub, which is accessible by everyone, or private.

Next, let’s learn about moving images into the registry. First, developers build and push the images using automation or a build pipeline into a registry, where Docker stores these images. Then, local machines, cloud systems, and on-premises systems can pull those images.

## Week 2

### Container Orchestration

To create, scale, and manage large numbers of containers, container orchestration is needed. **Container orchestration** is a process that automates the container lifecycle of container-based (or “containerized”) applications. This includes deployment, management, scaling, networking, and availability.

Container orchestration is a necessity in large, dynamic environments, since it:

- Streamlines complexity.
- Enables hands-off deployment and scaling.
- Increases speed, agility, and efficiency.
- Seamlessly integrates into CI/CD workflows and DevOps practices.
- Allows development teams to use resources more efficiently.

Container orchestration is often a critical part of an organization’s security, orchestration, automation, and response requirements, also known as “SOAR” requirements.

Container orchestration tools have a wide variety of features. These features include:

- Defining which container images make up the application, and where they are located (in what registry)
- Improving provisioning and deployment of containers for a more automated, unified, and smooth process.
- Securing network connections between containers.
- Ensuring availability and performance by relocating the containers to another host if an outage or shortage of system resources occurs.
- Scaling containers to meet demand, and load balance requests.
- Handling resource allocation and scheduling of containers to the underlying infrastructure.
- Performing rolling updates and roll backs.
- Conducting health checks to ensure applications are running, or performing the necessary actions when checks fail.

Container orchestration uses configuration files written in YAML or JSON.

- These files configure each container so it can find resources, establish a network, and store logs.
- Container orchestration also automatically schedules the deployment of a new container to a cluster, and finds the right host based on predefined settings or restrictions.
- Container orchestration manages the container's lifecycle based on specifications in the configuration file. This includes system parameters (like CPU and memory), and file parameters (like proximity and file metadata).
- Container orchestration supports scaling and enhances productivity, through automation.

The benefits of container orchestration for developers and administrators include:

- Increased productivity: Removing the burden of individually installing and managing each container, which, in turn reduces errors and frees development teams to focus on application improvement.
- Faster deployments: Iteratively releasing new features and capabilities faster and deploying containers and containerized applications rapidly.
- Reduced costs: Being cost-effective since containers have lower overhead and use fewer resources than virtual machines or traditional servers.
- Stronger security: Sharing resources and isolating application processes, improving the container’s overall security.
- Easier scalability: Scaling applications using a single command.
- Faster error recovery: Maintaining high availability by detecting and resolving issues like infrastructure failures automatically.

### Introduction to Kubernetes

The official Kubernetes documentation describes Kubernetes as “an open-source system for automating deployment, scaling, and management of containerized applications.”

Kubernetes facilitates declarative management in which it automatically performs the necessary operations towards achieving the called for state.

Here’s what Kubernetes is not.

- It is not a traditional, all-inclusive platform as a service.
- It is not rigid or opinionated but, more of a flexible model that supports an extremely diverse variety of workloads, including stateless, stateful, and data-processing workloads.
- It can work with all applications that can be containerized.
- It does not provide continuous integration/ continuous delivery pipelines to build applications or deploy source code.
- It does not prescribe logging, monitoring, and alerting solutions. Organizations are free to select and integrate third-party and open source tools.
- It does not provide built-in middleware, databases, or other services.

Concepts of Kubernetes include the following:

- **Pods** represent the smallest deployable compute object and the higher-level abstractions to run workloads.
- **Services** expose applications running on sets of Pods. Each Pod is assigned a unique IP address. Sets of Pods have a single DNS name. Kubernetes supports both persistent and temporary storage for Pods.
- **Configuration**, which refers to the provisioning of resources for configuring Pods.
- **Security measures** for cloud-native workloads, which enforce security for Pod and API access.
- **Policies** for groups of resources, ensuring that Pods match to Nodes so that the kubelet can find them and run the Pods.
- **Scheduling and Eviction** that runs and proactively terminates one or more Pods on resource-starved Nodes.
- **Preemption**, which is all about prioritization. Preemption terminates lower priority Pods so that Pods with higher priority can schedule and run on Nodes.
- **Cluster administration** provides the details necessary to create or administer a cluster.

Kubernetes capabilities include:

- Automated rollouts of changes to application or configuration, health monitoring and rolling back changes.
- Storage orchestration that mounts a chosen storage system including local storage, network storage, or public cloud.
- Horizontal scaling of workloads based on metrics, or via commands.
- **Automated bin packing** that increases utilization and cost savings using a mix of critical and best-effort workloads. Automated bin packing performs container auto-placement based on resource requirements and conditions without sacrificing high availability.
- Kubernetes includes Secret and configuration management of sensitive information including passwords, OAuth tokens, and SSH keys, and handles deployments and updates to secrets and configuration without rebuilding images.
- Kubernetes assigns both IPv4 and IPv6 addresses to Pods and Services.
- Kubernetes manages batch and continuous integration workloads and automatically replaces failed containers. It self-heals failing or unresponsive containers. It discovers Pods using IP addresses or a DNS name, and load balances traffic for better performance and high availability, and Kubernetes adds features to your cluster without modifying source code.

Kubernetes ecosystem includes services like: Building container images. Storing images in a container registry. Application logging and monitoring, and CI/CD capabilities. The Kubernetes ecosystem is a huge collection of products, services and providers. Leading public cloud providers include Prisma, IBM, Google, and AWS.

### Kubernetes Architecture

A deployment of Kubernetes is called a **Kubernetes cluster**. A Kubernetes cluster is a cluster of nodes that runs containerized applications. Each cluster has one _master node_ (the _Kubernetes Control Plane_) and one or more _worker nodes_. The control plane maintains the intended cluster state by making decisions about the cluster and detecting and responding to events in the cluster.

**Nodes** are the worker machines in a Kubernetes cluster. In other words, user applications are run on nodes. Nodes are not created by Kubernetes itself, but rather by the cloud provider. This allows Kubernetes to run on a variety of infrastructures. The nodes are then managed by the control plane.

In the Kubernetes control plane, the Kubernetes API server exposes the Kubernetes API. The API server serves as the front-end for the control plane. All communication in the cluster utilizes this API

The main implementation of a Kubernetes API server is **kube-apiserver** which is designed to scale horizontally—by deploying more instances. You can run several instances of kube-apiserver and balance traffic between those instances.

**Etcd** is a highly available, distributed key value store that contains all the cluster data. When you tell Kubernetes to deploy your application, that deployment configuration is stored in etcd. Etcd defines the state in a Kubernetes cluster, and the system works to bring the actual state to match the desired state.

The **Kubernetes scheduler** assigns newly created Pods to nodes. This basically means that the **kube-scheduler** determines where your workloads should run within the cluster. The scheduler selects the most optimal node according to Kubernetes scheduling principles, configuration options, and available resources.

The **Kubernetes controller manager** runs all the controller processes that monitor the cluster state, and ensure the actual state of a cluster matches the desired state.

The **cloud controller manager** runs controllers that interact with the underlying cloud providers. These controllers effectively link clusters into a cloud provider’s API. Since Kubernetes is open source and would ideally be adopted by a variety of cloud providers and organizations, Kubernetes strives to be as cloud agnostic as possible. The cloud-controller-manager allows both Kubernetes and the cloud providers to evolve freely without introducing dependencies on the other.

**Nodes** are the worker machines in a Kubernetes cluster. In other words, user applications are run on nodes. Nodes can be virtual or physical machines. Each node is managed by the control plane and contain the services necessary to run applications. Nodes include pods, which are the smallest deployment entity in Kubernetes. Pods include one or more containers.

Containers share all the resources of the node and can communicate among themselves. The **kubelet** is the most important component of a worker node. This controller communicates with the kube-apiserver to receive new and modified pod specifications and ensure that the pods and their associated containers are running as desired. The kubelet also reports to the control plane on the pods’ health and status.

In order to start a pod, the kubelet uses the container runtime. The **container runtime** is responsible for downloading images and running containers. Rather than providing a single container runtime, Kubernetes implements a Container Runtime Interface that permits pluggability of the container runtime. While Docker is likely the best-known runtime, Podman and Crio are two other commonly used container runtimes.

The **Kubernetes proxy** is a network proxy that runs on each node in a cluster. This proxy maintains network rules that allow communication to Pods running on nodes — in other words, communication to workloads running on your cluster. This communication can come from within or outside of the cluster.

### Kubernetes Objects - Part 1

A software **object** is a bundle of data that has an identity, a state, and a behavior. Examples include variables, data structures, and specific functions. **Entity** which also has an identity and associated data. For example, in banking, a customer account is an entity. **Persistent** means something will last even if there is a server failure or network attack.

Kubernetes objects are persistent entities. Examples include: Pods, Namespaces, ReplicaSets, Deployments, and more. Kubernetes objects consist of two main fields - **object spec** and **status**. The object spec is provided by the user which dictates an object’s desired state. Status is provided by Kubernetes. This describes the current state of the object. Kubernetes works towards matching the current state to the desired state.

**Labels** are key/value pairs attached to objects. They are intended for identification of objects. However, a label does not uniquely identify a single object. Many objects can have the same labels. This helps to organize and group objects. **Label selectors** are the core grouping method in Kubernetes. They allow you to identify a set of objects.

**Namespaces** provide a mechanism for isolating groups of resources within a single cluster. This is useful when teams share a cluster for cost-saving purposes or for maintaining multiple projects in isolation. Namespaces are ideal when the number of cluster users is large. Examples of namespaces are kube-system, intended for system users and the default namespace used to hold users’ applications.

Namespaces provide a scope for the names of objects. Each object must have a unique name for that resource type within that namespace.

A **Pod** is the simplest unit in Kubernetes. A Pod represents a process or a single instance of an application running in the cluster. A Pod usually wraps one or more containers. Creating replicas of a Pod serves to scale an application horizontally. YAML files are often used to define the objects that you want to create.

A **ReplicaSet** is a set of identical running replicas of a Pod that are horizontally scaled. The configuration files for a ReplicaSet and a Pod are different from each other. The replicas field specifies the number of replicas that should be running at any given time. Whenever this field is updated, the ReplicaSet creates or deletes Pods to meet the desired number of replicas.

Creating ReplicaSets directly is not recommended. Instead, create a Deployment, which is a higher-level concept that manages ReplicaSets and offers more features and better control. A **Deployment** is a higher-level object that provides updates for both Pods and ReplicaSets. Deployments run multiple replicas of an application using ReplicaSets and offer additional management capabilities on top of these ReplicaSets. Deployments are suitable for stateless applications. For stateful applications, Stateful Sets are used.

One key feature provided by Deployments but not by ReplicaSets is rolling updates. A rolling update scales up a new version to the appropriate number of replicas and scales down the old version to zero replicas. ReplicaSet ensures that the appropriate number of Pods exist, while the Deployment orchestrates the roll out of a new version.

### Kubernetes Objects - Part 2

A **Service** is a REST object, like Pods. Services are a logical abstraction for a set of Pods in a cluster. They provide policies for accessing the Pods and cluster. And act as a load balancer across the Pods. Each Service is assigned a unique IP address for accessing applications deployed on Pods. And a Service eliminates the need for a separate service discovery process. A Service supports multiple protocols such as TCP, which is the default protocol, UDP, and others, and supports multiple port definitions. The port number with the same name can vary in each backend Pod. In addition, a Service can have an optional selector and can optionally map incoming ports to a targetPort.

Why a Service is needed. A service is needed because Pods in a cluster can be destroyed and new Pods can be created at any time. This volatility leads to discoverability issues because of changing IP addresses. A Service keeps track of Pod changes and exposes a single IP address or a DNS name and utilizes selectors to target a set of Pods. For native Kubernetes applications, API endpoints are updated whenever changes are detected to the Pods in the Service. For Non-native applications, Kubernetes uses a virtual-IP-based bridge or load balancer in between the applications and the backend Pods.

There are four types of Services – ClusterIP, NodePort, LoadBalancer, and External Name.

- **ClusterIP** is the default and most common service type. Kubernetes assigns a cluster-internal IP address to the ClusterIP Service that makes the Service only reachable within the cluster. A ClusterIP service cannot make requests to Service from outside the cluster. You can set the ClusterIP address in the Service definition file, and the ClusterIP Service provides Inter-service communication within the cluster. For example, communication between the front-end and back-end components of your app.
- An extension of ClusterIP Service, a **NodePort** Service creates and routes the incoming requests automatically to the ClusterIP Service. A NodePort exposes the Service on each Node’s IP address at a static port. Note that for security purposes, production use is not recommended. Kubernetes exposes a single Service with no load-balancing requirements for multiple services.
- An extension of the NodePort Service, an **External Load Balancer**, or ELB, creates NodePort and ClusterIP Services automatically. An ELB integrates and automatically directs traffic to the NodePort Service. To expose a Service to the Internet, you need a new ELB with an IP address. You can use a cloud provider’s ELB to host your cluster.
- The **External Name Service** type maps to a DNS name and not to any selector and requires a `spec.externalName` parameter. The External Name Service maps the Service to the contents of the externalName field that returns a CNAME record and its value. You can use an External name to create a Service that represents external storage and enable Pods from different namespaces to talk to each other.

**Ingress** is an API object that, when combined with a controller, provides routing rules to manage external users’ access to multiple services in a Kubernetes cluster. In production, Ingress exposes applications to the Internet via port 80 (for HTTP) or port 443 (for HTTPS) While the cluster monitors Ingress, an external Load Balancer is expensive and is managed outside the cluster.

A **DaemonSet** is an object that makes sure that Nodes run a copy of a Pod. As nodes are added to a cluster, Pods are added to the nodes. Pods are garbage collected when removed from a cluster. If you delete a DaemonSet, all Pods are removed. DaemonSets are ideally used for storage, logs, and monitoring nodes.

A **StatefulSet** is an object that manages stateful applications, manages deployment and scaling of Pods, and provides guarantees about the ordering and uniqueness of Pods. A StatefulSet maintains a sticky identity for each Pod request and provides persistent storage volumes for your workloads.

**Job** creates Pods and tracks the Pod completion process. Jobs are retried until completed. Deleting a job will remove the created Pods. Suspending a Job will delete its active Pods until the job resumes. A job can run several Pods in parallel. And a CronJob is regularly used to create Jobs on an iterative schedule.

### Using Kubectl

**Kubectl** is the Kubernetes command line interface (or CLI). Kubectl stands for Kube Command Tool Line. It helps users deploy applications, inspect and manage cluster resources, view logs, and more.

Three Kubectl command types are **imperative commands**, **imperative object configuration**, and **declarative object configuration**.

Kubectl commands use the following structure: `Kubeclt [command] [type] [name] [flags]`

- command means any operation to be performed, like ‘create’, ‘get’, ‘apply’, or ‘delete’,
- type means resource type, like ‘pod’, ‘deployment’, or ‘ReplicaSet’,
- name means resource name (if applicable),
- flags means special options or modifiers that override default values.

**Imperative commands** allow you to create, update, and delete live objects directly. Operations should be specified to the command as arguments or flags. imperative commands don’t provide an audit trail, which is important for tracking changes. They aren’t flexible since options are limited, they don’t use templates, and they cannot integrate with change review processes. But they are ideal for development and test environments. Imperative commands do also have disadvantages. Suppose a developer runs a command to deploy an application. Another developer wants to deploy that same application, but they cannot because there is no configuration file. The second developer must check with the first developer for the exact command to deploy and then run it. It would be best if both developers used a template for the deployment since it overcomes the limitations of working with imperative commands.

In **imperative object configuration**, the kubectl command specifies required operations, optional flags, and at least one file name. The specified configuration file must contain a full definition of the objects in YAML or JSON format. To create the objects defined in the file, run the command ‘kubectl create -f nginx.yaml’. Using the same configuration templates in multiple environments will produce identical results. A configuration file: may be stored in a source control system like Git, it can integrate with change processes, and it provides audit trails and templates for creating new objects. But using it requires understanding of the object schema, and requires writing a YAML or JSON file. Now, imperative object configuration also has limitations. You need to specify all necessary command operations. For example, if a developer performs an update operation that isn’t merged into the configuration file, then another developer cannot use the updated configuration in future deployments. The second developer instead uses the original or previous configuration. It is better to define the desired state in a shared configuration file, then when you deploy, Kubernetes automatically determines the necessary operations. This is known as declarative object configuration.

**Declarative object configuration** stores configuration data in files. Operations are identified by Kubectl instead of being specified by the user. This works on directories or individual files. For example, the ‘kubectl apply’ command mentions a directory (as shown), then applies configuration data to all files in that directory. The user is not required to perform any operations since they are performed by the system automatically. Configuration files define a desired state, and Kubernetes actualizes that state. And this approach is the ideal method for production systems. Here is an example of declarative configuration. A developer performs updates to a running application. Since configuration data is stored in the shared template, there is still one source of truth for the configuration of this object. Now, even if another developer misses several of these updates, all they need to do is apply the current configuration template to ensure the deployed object is as expected. Kubernetes automatically determines and performs the necessary operations to match the current state to the desired state.

## Week 3

### ReplicaSet

Single-pod deployments cannot: Accommodate growing demands of the application and load balancing across pods; Handle outages by eliminating a single point of failure; Minimize downtime and service interruptions by providing high availability through redundant pods; Or automatically restart deployments if something goes wrong. We can work around these limitations with a ReplicaSet.

A ReplicaSet ensures the right number of pods are always up and running. It always tries to match the actual state of the replicas to the desired state. A ReplicaSet: Adds or deletes pods for scaling and redundancy, which helps maintain availability. It replaces failing pods or deletes additional pods to maintain the desired state. And it supersedes a ReplicaController and should be used instead.

A ReplicaSet is created for you when you create a deployment in your cluster. Deployments manage ReplicaSets, send pods declarative updates, and have many other useful features. That’s why a ReplicaSet is best managed by a Deployment. Kubernetes is designed to keep object types independent. That is why the ReplicaSet does not own any of the pods. Instead, it uses pod labels to decide which pods to acquire when bringing a deployment to the desired state.

### Autoscaling

ReplicaSets provide a good start for scaling, but you don’t always want 10 instances of your resource running. You should be able to scale as needed. Kubernetes autoscaling helps optimize resource usage and costs by automatically scaling a cluster in line with demand. Kubernetes enables autoscaling at two different layers: the cluster or node level and the pod level. Three types of autoscalers are available in Kubernetes: Horizontal Pod Autoscaler (or HPA), Vertical Pod Autoscaler (or VPA), and Cluster Autoscaler (or CA).

The **Horizontal Pod Autoscaler** (or HPA) adjusts the number of replicas of an application by increasing or decreasing the number of pods. The **Vertical Pod Autoscaler** (or VPA) adjusts the resource requests and limits of a container by increasing or decreasing the resource size or speed of the pods. And the **Cluster Autoscaler** (or CA) adjusts the number of nodes in the cluster when pods fail to schedule, or demand increases or decreases in relation to the nodes’ capacity.

In Kubernetes, an HPA automatically updates a workload resource (like a deployment) by horizontally scaling the workload to match the demand. Horizontal scaling, or “scaling out,” automatically increases or decreases the number of running pods as application usage changes. An HPA uses a cluster operator that sets targets for metrics like CPU or memory utilization and the maximum and minimum desired number of replicas.

Vertical scaling, or “scaling up,” refers to adding more resources to an existing machine. A VPA lets you scale a service vertically within a cluster. The cluster operator sets targets for metrics like CPU or memory utilization, similar to an HPA. The cluster then reconciles the size of the service’s pod or pods based on their current usage and the desired target.

A CA autoscales the cluster itself, increasing and decreasing the number of available nodes that pods can run on. Pods are autoscaled using HPA or VPA, but when the nodes themselves are overloaded with pods, you can use a CA to autoscale the nodes so that the pods can rebalance themselves across the cluster.

### Rolling Updates

**Rolling updates** are automated updates that occur on a scheduled basis. They roll out automated and controlled app changes across pods, Work with pod templates like deployments, and allow for rollback as needed.

To prepare your application to enable rolling updates, Add liveness probes and readiness probes to deployments. That way deployments are appropriately marked as ‘ready.’ Next, add a rolling update strategy to the YAML file.

Now let’s take a look at how rolling updates work, both: All-at-once And one-at-a-time. In an **all-at-once rollout**, all v1 objects must be removed before v2 objects can become active. In an **all-at-once rollback**, all v2 objects must be removed before v1 objects can become active. (see below the detailed explanation of one-at-a-time and try to understand the difference)

In a **one-at-a-time rollout**, the update is staggered so user access is not interrupted.Here you see version 2 of an app with three pods running that users can access. When version 1 of the app is deployed, new pods are created. The version 2 pods are marked for deletion and removed. And user access is blocked. Once the version 2 pods are removed, the version 1 pods become active and user access is restored. In a one-at-a-time rollout, the update is staggered so user access is not interrupted. Here you see version 1 of an app with three running pods that users can access. When version 2 is deployed, a new pod is created. The first version 1 pod is marked for deletion and removed. And the v2 pod becomes active. Then a second v2 pod is created. And the second version 1 pod is marked for deletion and removed. The second v2 pod becomes active. A third v2 pod is created. And the third version 1 pod is marked for deletion and removed. And now the third v2 pod becomes active. With a staggered update, user access is not interrupted.

### ConfigMaps and Secrets

As software developers, a good practice to adopt is to avoid hard coding configuration variables in application code by keeping the configuration variables separate so that any changes in configuration settings do not require code changes.

A **ConfigMap** is an API object that stores non-confidential data in key-value pairs. In addition, a configmap provides configuration data to pods and deployments so that the configuration data is not hard coded inside the application code and is meant for non-sensitive information as they do not provide secrecy or encryption. Data stored in a ConfigMap cannot exceed 1 megabyte. For larger amounts of data, consider mounting a volume or use a separate database or file service. A ConfigMap has optional data and binary data fields. And in this case, there is no “spec" field in the template, and the Config name must be a valid DNS subdomain name.

A ConfigMap is reusable for multiple deployments, thus decoupling the environment from the deployments themselves! You can create a ConfigMap by using string literals, by using an existing “properties” or ”key” = “value” file, or by providing a ConfigMap YAML descriptor file. You can use the first and second ways to help create such a YAML file.

Kubernetes applies the ConfigMap to the pod or the deployment just before running the pod or deployment.

Working with a **Secret** is like working with a ConfigMap. First, create a secret using a string literal. Next, the GET command verifies that the secret was created. Finally, to prove that our secret is indeed a secret, use the DESCRIBE command and check that you don’t see any secret, written using displayed text.

### Service Binding

**Service binding** is the process needed to consume external Services or backing Services, including REST APIs, databases, and event buses in our applications. Service binding manages configuration and credentials for back-end Services while protecting sensitive data. In addition, Service binding makes Service credentials available to you automatically as a Secret. Service binding consumes the external Service by binding the application to a deployment. Then, the application code uses the credentials from the binding and calls the corresponding Service.

## Week 4

### Introduction to Red Hat OpenShift

**OpenShift** (developed and supported by Red Hat®) is an enterprise-ready Kubernetes container platform built for the hybrid cloud strategy. It provides a consistent application platform to manage hybrid, multicloud, and edge deployments. It is built on the technological foundation of Linux, containers, and automation. It provides full-stack automated operations and self-service provisioning for developers to efficiently move ideas from development to production. And besides container orchestration, it provides additional tooling around the complete lifecycle of applications, from build, to CI/CD, to monitoring and logs.

OpenShift is used as an extension of Kubernetes to provide a more robust and comprehensive platform for containerized applications.

Let’s review the features of OpenShift:

- Apps can scale to thousands of instances across hundreds of nodes in seconds.
- Flexible hybrid infrastructure options simplify deployment and management.
- Open source standards use Kubernetes and Open Container Initiative (OCI) containers, which means development is familiar
- Containers are portable across multiple environments.
- It includes a comprehensive set of developer tools, multilanguage support, command line, IDE integrations, and more.
- It supports Over-air platform upgrades, and services from the OperatorHub can be fully configured and deployed with one-click upgrades.
- Container and app builds, deployments, scaling, and health management, are streamlined and automated.
- OpenShift also, enhances support for smaller-footprint topologies in edge scenarios for better mapping, connectivity, and availability.
- It easily manages and enforces policies across multiple clusters at scale.
- It offers access controls, networking and enterprise registry, built-in scanner, enhanced threat detection, lifecycle vulnerability management, and risk profiling.
- OpenShift supports enterprise persistent storage solutions for running stateful and stateless apps.
- OpenShift partner ecosystem provides additional storage and network services, as well as IDE, CI, integrations, and more.

OpenShift runs on top of a Kubernetes cluster, with object data stored in the etcd key-value store. It has a microservices-based architecture. Its services are: REST APIs, which expose the core objects. And controllers, which read the REST APIs, apply changes to the other objects, and report status or write back to the object. They also maintain the cluster desired state.

OpenShift features add: Management of source code, builds, and deployments for developers. Managing and promoting images at scale as they flow through your system. Application management at scale. Team and user tracking management of a large developer organization. And networking infrastructure that supports the cluster.

### Builds

A **Build** is the process of transforming inputs into a resultant object. For example, transforming source code to a container image. A Build requires a build configuration file (or BuildConfig), which defines the build strategy and input sources. Commonly used Build strategies are: Source-to-Image (S2I), Docker, and Custom.

An **ImageStream** is an abstraction for referencing container images within OpenShift. An ImageStream: Continuously creates and updates container images, but does not contain actual image data. Instead, it points to images stored in internal and external registries, or to other ImageStreams. A single ImageStream can consist of many different tags such as latest, dev and test. And each tag points to a certain image in a registry. To deploy an application, you’ll refer to the image stream tag rather than hardcode the registry URL and tag. If the source image location changes, you’ll update the image stream definition, rather than individually updating all the deployments. An ImageStream also provides a trigger capability that automatically invokes builds and deployments when a new version of an image is available.

Rather than running builds manually, automate the process using **triggers**.

- **Webhook triggers**: Send a request to an API endpoint. And they also support generic webhooks and the more often used GitHub webhooks which send the trigger request to the API endpoint on any new commit or a pull request or other circumstances.
- **Image change trigger**: Triggers builds when a new version of an image is available. For instance, if you build your application using a Node.js base image, that image is updated when security fixes are released, and other updates occur.
- **Configuration change trigger**: Causes a new build to run when you create a new BuildConfig resource.

The **S2I tool**: Builds reproducible container images, and Injects a container image with the app source to produce a ready-to-run image. The new image is built by incorporating a builder image plus the source that avoids using a Dockerfile, which enables going from Source to Image in a single step. OpenShift comes with a variety of available builder images, saving you time and development effort.

Using a Docker Build strategy requires a repository that contains a Dockerfile and the necessary artifacts. When you kick off a build, OpenShift takes the input, invokes the “docker build“ command and creates an image which is then pushed to the internal OpenShift registry. Here are four ways to implement the Docker build strategy: replace Dockerfile FROM image, use Dockerfile path, use Docker environment variables, or add Docker build arguments. In a custom build strategy, you must define and create your own builder image required for the build process. Custom builder images are regular Docker images that contain the logic needed to transform the inputs into the expected output. Both Docker and S2I strategies result in runnable images, but the custom build strategy creates additional objects like JAR files and CI/CD deployment that performs unit or integration tests. Custom builds are only available to cluster administrators because they run with high privileges.

Cloud-native development requires greater automation throughout the container lifecycle. Automation is available using the continuous integration and continuous deliverypipeline, or CI/CD. For example, the OpenShift CI/CD process automatically merges new code changes to the repository, then builds, tests, approves, and deploys a new version to different environments.

### Operators

**Operators** automate cluster tasks and act as a custom controller to extend the Kubernetes API. Operators run in a Pod and interact with the API server, package, deploy, and manage Kubernetes applications, and automate app creation, configuration, and management via continuous real-time decisions.

There are human operators and software operators. **Human operators** understand the systems they control. They know how to deploy services and how to recognize and fix problems. **Software operators** try to capture the knowledge of human operators and automate the same processes.

Operators provide: Ease of repeatable installation and upgrade processes. Regular full-system health checks of each component in the system. Over-the-air (or OTA) updates for components and software vendors’ content. A way to collect and spread knowledge from field engineers to all users. And integration with APIs and CLI tools, such as kubectl and oc commands.

**Service brokers provide**: A short-running process that cannot perform the consecutive day’s operations, such as upgrades, failover, or scaling. Customizations and parameterization only at the time of installation. And off-cluster services. Operators provide a long-running process that can perform operations, like upgrades, failover, or scaling every day. Customizations and parameterization, as operators constantly watch the current state of your cluster. And off-cluster services.

**Custom resource definitions** (or CRDs) store and retrieve objects in the Kubernetes API. CRDs extend Kubernetes functionality beyond built-in resources like Deployments and Pods. They make the Kubernetes API more modular and flexible. Users can install CRDs in clusters, but each CRD is available only in the cluster it is installed. Once installed, CRD objects are accessible using kubectl, similar to pods and other resources. To change the state of a cluster, custom controllers are used.

Controllers reconcile a cluster’s actual state with its configured state. **Custom controllers** do the same reconciling for custom resources. Combining CRDs and custom controllers creates a declarative API. This combination is known as “The Operator Pattern.” Custom controllers interpret CRD data as the desired state and reconcile a cluster’s actual state to match the CRD data.

The **Operate Framework** is an open-source toolset that covers coding, testing, delivery, and Operator updates. The Operator SDK (which includes Helm, Go, and Ansible) helps authors build, test, and package their Operators without requiring knowledge of Kubernetes API complexities. The Operator Lifecycle Manager (or OLM) controls the install, upgrade, and **role-based access control** (or RBAC) of Operators in a cluster. The Operator Registry stores CRDs, cluster service versions (or CSVs), and Operator metadata for packages and channels. It runs in Kubernetes or OpenShift clusters to provide the Operator catalog data to OLM. The OperatorHub web console lets cluster administrators find Operators to install on their cluster.

### Istio

A **service mesh** is a dedicated layer for making service-to-service communication secure and reliable. Among other things, service meshes provide traffic management to control the flow of traffic between services, security to encrypt traffic between services, and observability of service behavior to troubleshoot and optimize applications. The “Service mesh” term describes the software that creates a security or network domain with the pattern for achieving the above capabilities.

**Istio** is a platform-independent service mesh often used on Kubernetes. In keeping with the definition of a service mesh, Istio exhibits these four concepts.

- First, there’s connection. Connection enables Istio to intelligently control the traffic between services in canary deployments, A/B tests, and other deployment models.
- Next is security. Istio secures services through authentication, authorization, and encryption.
- Istio also provides enforceability and provides control by enforcing policies across an entire fleet.
- And finally, Istio supports observability. Using Istio, you can observe the traffic flow in your mesh, trace call flows and dependencies, and view metrics such as latency and errors.

Istio features

- Transport Security Layer encrypted communications between services in a cluster, combined with the appropriate authentication and authorization.
- Istio load balances traffic for different protocols, including HTTP, TCP, gRPC, and WebSocket traffic.
- Istio supports granular configuration of traffic flow, known as routing rules, and supports control with continuous retries, fault injection methods, and automatic failovers.
- Along with policies and API support for access controls, rate limits, and quotas.
- Istio also provides automatic monitoring, logging, and tracking of both inbound and outbound traffic.

Istio is extensible and can handle a diverse range of deployment needs. Istio runs on Kubernetes, where you can add applications of a cluster to the mesh, extend the mesh to additional clusters, or connect to virtual machines or other endpoints running outside of Kubernetes.

There are two main components in Istio, the **control plane** and the **data plane**. Communication between services is handled by the data plane. If a service mesh is absent, the network cannot identify the type of traffic that flows, the source, or the destination and cannot make necessary decisions. All network traffic is subject to, or intercepted by, a proxy, called Envoy, which is use by the service mesh, and allows many features depending on the configuration. The control plane takes the desired configuration and its view of the services and dynamically programs and updates the proxy servers as the environment changes.

**Microservices** are a cloud-native architectural approach in which a single application contains many loosely coupled and independently deployable smaller components or services. Microservices have well-defined APIs for communicating with each other. The benefits of microservices are multiple. Code updates are easy, as only the relevant service needs to be updated instead of the entire application. They allow teams to use different technology stacks for each component. In addition, components can be scaled independently instead of the entire application. Challenges of microservices include encryption of traffic to ensure secure communication. Development teams might want to roll out new features to a subset of users or compare two versions of features in their application to see which engages users the most. In these cases, teams need canary deployments and A/B testing. The communication between microservices also leads to cascading failures if one service is unreachable or particularly slow. Developers need retries and circuit breaking to prevent errors in one microservice from cascading to others.

Istio performs traffic shifting by gradually migrating the traffic from one version of a microservice to other versions. So, say a team working on the ordering microservice has a new update to that microservice. The team begins by sending 5 percent of traffic to that second version. And over time, the team can increase this to 50 percent and eventually to 100 percent. Similarly, Istio request routing allows you to perform A/B tests and direct a particular version of a microservice to a subset of users while sending the original version to the remaining users. The process ensures that a new version increases user engagement or performance.

Istio also provides a variety of security measures for your microservices, including encryption. Istio defends from man-in-the-middle attacks by encrypting traffic between microservices. In addition, Istio makes it easy to implement policies for service access control so that services can only talk to the other required services.

Among other metrics, Istio provides service communication metrics. These metrics cover the four basic service monitoring needs: latency, traffic, errors, and saturation.
