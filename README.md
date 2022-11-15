# Meemoo Cookiecutter Prefect Flow
## Synopsis

A cookiecutter project that will create a Prefect flow used in meemoo.

Prerequisites

- Git
- Python 3.7+

## Usage

Install Cookiecutter if you haven't already:

```
$ pip3 install cookiecutter
```

Change into the directory in which you want to create a project.

Create a project:

```
$ cookiecutter https://github.com/viaacode/meemoo-cookiecutter-prefect-flow.git
```

Instead, you can also manually clone the Cookiecutter project:

```
$ git clone https://github.com/viaacode/meemoo-cookiecutter-prefect-flow.git
```

And create the project:

```
$ cookiecutter meemoo-cookiecutter-prefect-flow
```

Either way, tou will be prompted to fill in some variables:

```
project_name [Prefect flow]: 
repo_name [prefect-flow]: 
flow_name [prefect_flow]: 
queue_name [q-default]: (! Should always start with 'q-' to ensure it will be picked up)
organization [meemoo]: 
prefect_docker_image_tag [2.5.0-python3.9]: 
```

Change into the project and look around:

```
$ cd prefect-flow
$ ls -l
```

## Creating the Jenkins project

The `{repo_name}-multibranch-project.xml` contains the (definition of the) Jenkins project serialized in XML.
This needs to be uploaded to Jenkins. This can be done by using the Jenkins REST API.
You could use the [ci-cd-concepts-creator](https://github.com/viaacode/ci-cd-concepts-creator) to upload it to Jenkins.

First set the following environment variables:
```
JENKINS_API_URL=
JENKINS_API_USER=
JENKINS_API_TOKEN=
```

Then run the upload command:

```
python -m concepts_creator upload prefect {repo_name} /folder/to/prefect/flow/.openshift
```

