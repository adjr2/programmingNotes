## Overview

A Kubernetes deployment strategy defines an application’s lifecycle that achieves and maintains the configured state for objects and applications in an automated manner. Effective deployment strategies minimize risk.

Kubernetes deployment strategies are used to:

Deploy, update, or rollback ReplicaSets, Pods, Services, and Applications

Pause/Resume Deployments

Scale Deployments manually or automatically

### Types of deployment strategies

The following are six types of deployment strategies:

- Recreate
- Rolling
- Blue/green
- Canary
- A/B testing
- Shadow

You can use either a single deployment strategy or a combination of multiple deployment strategies.

#### Recreate strategy

In the recreate strategy, Pods running the live version of the application are all shut down simultaneously, and a new version of the application is deployed on newly created Pods.

Recreate is the simplest deployment strategy. There is a short downtime between the shutdown of the existing deployment and the new deployment.

Recreate strategy steps include:

1. A new version of the application (v2) is ready for deployment.
2. All Pods running the current version (v1) are shut down or deleted.
3. New (v2) Pods are created.

The rollback process is completed in the reverse order, replacing version 2 (v2) with version 1 (v1).

#### Rolling (ramped) strategy

In a rolling strategy, each Pod is updated one at a time. A single v1 Pod is replaced with a new v2 Pod. Each v1 Pod is updated in this way until all Pods are v2. During a rolling strategy update, there is hardly any downtime since users are directed to either version.

Rolling strategy steps include:

1. A new version of the application (v2) is ready for deployment.
2. One of the Pods running the current version (v1) is shut down or deleted.
3. A new (v2) Pod is created to replace the (v1) Pod that was removed.
4. Steps 2 and 3 are repeated until all (v1) Pods are removed and replaced with (v2) Pods.

The rollback process is reversed, where v2 Pods are replaced by v1 Pods.

#### Blue/green strategy

In a blue/green strategy, the blue environment is the live version of the application. The green environment is an exact copy that contains the deployment of the new version of the application. The green environment is thoroughly tested. Once all changes, bugs, and issues are addressed, user traffic is switched from the blue environment to the green environment.

Blue/green strategy steps include:

1. Create a new environment identical to the current production environment.

2. Design the new version and test it thoroughly until it is ready for production.

3. Route all user traffic to the new version.

To perform a rollback, switch the environments back.

#### Canary strategy

In a canary strategy, the new version of the application is tested using a small set of random users alongside the current live version of the application. Once the new version of the application is successfully tested, it is then rolled out to all users.

Canary strategy steps include:

1. Design a new version of the application.

2. Route a small sample of user requests to the new version.

3. Test for efficiency, performance, bugs, and issues, and rollback as needed.

4. Repeat steps 1 to 3. Once all issues are resolved, route all traffic to the new version.

Rollback has no downtime since few users are exposed to the new version.

#### A/B testing strategy

The A/B testing strategy, also known as split testing, evaluates two versions of an application (version A and version B). With A/B testing, each version has features that cater to different sets of users. You can select which version is best for global deployment based on user interaction and feedback.

A/B testing strategy steps include:

1. Design a new version of the application by adding mostly UI features.
2. Identify a small set of users based on conditions like weight, cookie value, query parameters, geolocalization, browser version, screen size, operating system, and language.
3. Route requests from the user set to the new version.
4. Check for bugs, efficiency, performance, and issues.
5. Once all issues are resolved, route all traffic to the new version.

Rollbacks can be implemented, but downtime can impact the user.

#### Shadow strategy

In a shadow strategy, a “shadow version” of the application is deployed alongside the live version. User requests are sent to both versions, and both handle all requests, but the shadow version does not forward responses back to the users. This lets developers see how the shadow version performs using real-world data without interrupting user experience.

To perform a rollback, switch the environments back.
