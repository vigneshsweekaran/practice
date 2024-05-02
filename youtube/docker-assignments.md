# Docker Assignments

### 1. Write a Dockerfile to install git, java 11 and maven in Ubuntu docker image, build the image, create the container and verify the version of each packages

```Dockerfile
FROM ubuntu:24.04

RUN apt update -y && \
    apt install git openjdk-11-jdk maven -y
```

Build docker image
```
docker build -t myubuntu:1.0 .
```

Create container
```
docker run -it myubuntu:1.0 bash
```

### 2. Write a Dockerfile `ubuntuGradle.Dockerfile` to install git, wget, java 11 and gradle using Ubuntu docker image, build the image, create the container and verify the version of each packages
```Dockerfile
FROM ubuntu:latest

RUN apt update && apt install -y --no-install-recommends \
    git \
    wget \
    openjdk-11-jdk \
    gradle \
    && rm -rf /var/lib/apt/lists/*
```

Build docker image
```
docker build -t ubuntu-gradle:1.0 -f ubuntuGradle.Dockerfile .
```

Create container
```
docker run -it ubuntu-gradle:1.0 bash
```

### 3. Write a Dockerfile `centosGradle.Dockerfile` to install git, java 11 and gradle using Centos docker image, build the image, create the container and verify the version of each packages
```Dockerfile
FROM centos:latest

ENV PATH=$PATH:/opt/gradle/gradle-7.0.2/bin

RUN yum update -y && yum install -y \
    git \
    wget \
    unzip \
    java-11-openjdk-devel \
    && yum clean all

RUN mkdir /opt/gradle \
    && wget -q https://services.gradle.org/distributions/gradle-7.0.2-bin.zip \
    && unzip gradle-7.0.2-bin.zip -d /opt/gradle/ \
    && rm -f gradle-7.0.2-bin.zip
```

Build docker image
```
docker build -t centos-gradle:1.0 -f centosGradle.Dockerfile .
```

Create container
```
docker run -it centos-gradle:1.0 bash
```

### 4. Write a Dockerfile `alpineGradle.Dockerfile` to install git, java 11 and gradle using Alpine docker image, build the image, create the container and verify the version of each packages
```Dockerfile
FROM alpine:latest

ENV PATH=$PATH:/opt/gradle/gradle-7.0.2/bin

RUN apk add --no-cache \
    git \
    openjdk11
    
RUN mkdir /opt/gradle \
    && wget -q https://services.gradle.org/distributions/gradle-7.0.2-bin.zip \
    && unzip gradle-7.0.2-bin.zip -d /opt/gradle/ \
    && rm -f gradle-7.0.2-bin.zip
```

Build docker image
```
docker build -t alpine-gradle:1.0 -f alpineGradle.Dockerfile .
```

Create container
```
docker run -it alpine-gradle:1.0 bash
```

### 5. Write a Dockerfile `ubuntuMavenSleep.Dockerfile` to install git, java 11 and maven using ubuntu docker image, add the sleep infinity in Dockerfile, build the image, create the container and verify the version of each packages
```Dockerfile
FROM ubuntu:24.04

RUN apt update -y && \
    apt install git openjdk-11-jdk maven -y

CMD ["sleep","infinity"]
```

Build docker image
```
docker build -t ubuntu-maven-sleep:1.0 -f ubuntuMavenSleep.Dockerfile .
```

Create container to run in background, no need to pass sleep infinity, since sleep infinity is already specified in Dockefile CMD
```
docker run -d ubuntu-maven-sleep:1.0
```

Verify container is running
```
docker ps
```

### 6. Write a Dockerfile `tomcat.Dockerfile` to install java 11 and tomcat9 using ubuntu docker image, add by default start the tomcat when the container is started, build the image, create the container and verify the version of each packages
```Dockerfile
FROM ubuntu:24.04

RUN apt update -y && \
    apt install curl openjdk-11-jdk -y

WORKDIR /opt

RUN curl https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.88/bin/apache-tomcat-9.0.88.tar.gz -o apache-tomcat-9.0.88.tar.gz && \
    tar -xvf apache-tomcat-9.0.88.tar.gz && \
    rm -rf apache-tomcat-9.0.88.tar.gz

CMD ["/opt/apache-tomcat-9.0.88/bin/catalina.sh", "run"]

```

Build docker image
```
docker build -t mytomcat:1.0 -f tomcat.Dockerfile .
```

Create container to run in background and map the host port 8080 to container port 8080
```
docker run -d -p 8080:8080 mytomcat:1.0
```

Verify container is running
```
docker ps
```
