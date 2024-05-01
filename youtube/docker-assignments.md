# Docker Assignments

### Write a Dockerfile to install git, java 11 and maven in Ubuntu docker image, build the image, create the container and verify the version of each packages

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

### Write a Dockerfile `ubuntuGradle.Dockerfile` to install git, wget, java 11 and gradle using Ubuntu docker image, build the image, create the container and verify the version of each packages
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

### Write a Dockerfile `centosGradle.Dockerfile` to install git, java 11 and gradle using Centos docker image, build the image, create the container and verify the version of each packages
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

### Write a Dockerfile `alpineGradle.Dockerfile` to install git, java 11 and gradle using Alpine docker image, build the image, create the container and verify the version of each packages
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