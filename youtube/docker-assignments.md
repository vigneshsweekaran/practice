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

### 6. Write a Dockerfile `tomcat.Dockerfile` to install java 11 and tomcat9 using ubuntu docker image, and by default start the tomcat when the container is created, build the image, create the container and verify tomcat is running on port 8080
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
docker run -d --name tomcat-p 8080:8080 mytomcat:1.0
```

Verify container is running
```
docker ps
```

Verify the tomcat UI in browser
```
http://ip-address:8080
```

CLEANUP:
Deleting the container
```

docker rm -f tomcat
```

### 7. Build a hello world java application and generate the war file
### Write a Dockerfile `tomcat-helloworld.Dockerfile` to install java 11 and tomcat9 using ubuntu docker image, copy the war file to webapps folder in Dockerfile
### By default start the tomcat when the container is created
### Build the image, create the container and verify hello-world application is running in tomcat on port http://ip-address:8080/hello-world

Clone the hello-wolrd java application from github
```
ubuntu@vignesh-teaching:~/vignesh$ pwd
/home/ubuntu/vignesh
ubuntu@vignesh-teaching:~/vignesh$ git clone https://github.com/vigneshsweekaran/hello-world.git
Cloning into 'hello-world'...
remote: Enumerating objects: 1353, done.
remote: Total 1353 (delta 0), reused 0 (delta 0), pack-reused 1353
Receiving objects: 100% (1353/1353), 218.97 KiB | 6.84 MiB/s, done.
Resolving deltas: 100% (590/590), done.
```
```
ubuntu@vignesh-teaching:~/vignesh$ cd hello-world/
ubuntu@vignesh-teaching:~/vignesh/hello-world$ ll
total 64
drwxrwxr-x 8 ubuntu ubuntu 4096 May  2 23:04 ./
drwxrwxr-x 3 ubuntu ubuntu 4096 May  2 23:04 ../
drwxrwxr-x 8 ubuntu ubuntu 4096 May  2 23:04 .git/
-rw-rw-r-- 1 ubuntu ubuntu  269 May  2 23:04 .gitattributes
drwxrwxr-x 3 ubuntu ubuntu 4096 May  2 23:04 .github/
-rw-rw-r-- 1 ubuntu ubuntu   69 May  2 23:04 .gitignore
-rw-rw-r-- 1 ubuntu ubuntu   95 May  2 23:04 Dockerfile
-rw-rw-r-- 1 ubuntu ubuntu 2047 May  2 23:04 README.md
-rw-rw-r-- 1 ubuntu ubuntu  646 May  2 23:04 appspec.yml
-rw-rw-r-- 1 ubuntu ubuntu 2146 May  2 23:04 buildspec.yml
drwxrwxr-x 3 ubuntu ubuntu 4096 May  2 23:04 cicd/
drwxrwxr-x 3 ubuntu ubuntu 4096 May  2 23:04 codedeploy/
drwxrwxr-x 5 ubuntu ubuntu 4096 May  2 23:04 deployment/
-rw-rw-r-- 1 ubuntu ubuntu 1248 May  2 23:04 pom.xml
-rw-rw-r-- 1 ubuntu ubuntu  231 May  2 23:04 sonar-project.properties
drwxrwxr-x 4 ubuntu ubuntu 4096 May  2 23:04 src/
```

Build the application and generate the war file
```
ubuntu@vignesh-teaching:~/vignesh/hello-world$ mvn clean package
[INFO] Packaging webapp
[INFO] Assembling webapp [hello-world] in [/home/ubuntu/vignesh/hello-world/target/hello-world-1.0-SNAPSHOT]
[INFO] Processing war project
[INFO] Copying webapp resources [/home/ubuntu/vignesh/hello-world/src/main/webapp]
[INFO] Webapp assembled in [43 msecs]
[INFO] Building war: /home/ubuntu/vignesh/hello-world/target/hello-world-1.0-SNAPSHOT.war
[INFO] WEB-INF/web.xml already added, skipping
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  6.266 s
[INFO] Finished at: 2024-05-02T23:06:44Z
[INFO] ------------------------------------------------------------------------
```
```
ubuntu@vignesh-teaching:~/vignesh/hello-world$ ll
total 68
drwxrwxr-x  9 ubuntu ubuntu 4096 May  2 23:06 ./
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:04 ../
drwxrwxr-x  8 ubuntu ubuntu 4096 May  2 23:04 .git/
-rw-rw-r--  1 ubuntu ubuntu  269 May  2 23:04 .gitattributes
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:04 .github/
-rw-rw-r--  1 ubuntu ubuntu   69 May  2 23:04 .gitignore
-rw-rw-r--  1 ubuntu ubuntu   95 May  2 23:04 Dockerfile
-rw-rw-r--  1 ubuntu ubuntu 2047 May  2 23:04 README.md
-rw-rw-r--  1 ubuntu ubuntu  646 May  2 23:04 appspec.yml
-rw-rw-r--  1 ubuntu ubuntu 2146 May  2 23:04 buildspec.yml
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:04 cicd/
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:04 codedeploy/
drwxrwxr-x  5 ubuntu ubuntu 4096 May  2 23:04 deployment/
-rw-rw-r--  1 ubuntu ubuntu 1248 May  2 23:04 pom.xml
-rw-rw-r--  1 ubuntu ubuntu  231 May  2 23:04 sonar-project.properties
drwxrwxr-x  4 ubuntu ubuntu 4096 May  2 23:04 src/
drwxrwxr-x 10 ubuntu ubuntu 4096 May  2 23:06 target/
```

Verify war file is generated in *target* folder
```
ubuntu@vignesh-teaching:~/vignesh/hello-world$ ll target
total 48
drwxrwxr-x 10 ubuntu ubuntu 4096 May  2 23:06 ./
drwxrwxr-x  9 ubuntu ubuntu 4096 May  2 23:06 ../
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:06 classes/
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:06 generated-sources/
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:06 generated-test-sources/
drwxrwxr-x  4 ubuntu ubuntu 4096 May  2 23:06 hello-world-1.0-SNAPSHOT/
-rw-rw-r--  1 ubuntu ubuntu 5467 May  2 23:06 hello-world-1.0-SNAPSHOT.war
drwxrwxr-x  2 ubuntu ubuntu 4096 May  2 23:06 maven-archiver/
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:06 maven-status/
drwxrwxr-x  2 ubuntu ubuntu 4096 May  2 23:06 surefire-reports/
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:06 test-classes/
```

Create a Dockerfile *tomcat-hello-world.Dockerfile*
```Dockerfile
FROM ubuntu:24.04

RUN apt update -y && \
    apt install curl openjdk-11-jdk -y

WORKDIR /opt

RUN curl https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.88/bin/apache-tomcat-9.0.88.tar.gz -o apache-tomcat-9.0.88.tar.gz && \
    tar -xvf apache-tomcat-9.0.88.tar.gz && \
    rm -rf apache-tomcat-9.0.88.tar.gz

COPY target/hello-world-*.war /opt/apache-tomcat-9.0.88/webapps/hello-world.war

CMD ["/opt/apache-tomcat-9.0.88/bin/catalina.sh", "run"]

```
```
ubuntu@vignesh-teaching:~/vignesh/hello-world$ ll
total 72
drwxrwxr-x  9 ubuntu ubuntu 4096 May  2 23:10 ./
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:04 ../
drwxrwxr-x  8 ubuntu ubuntu 4096 May  2 23:04 .git/
-rw-rw-r--  1 ubuntu ubuntu  269 May  2 23:04 .gitattributes
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:04 .github/
-rw-rw-r--  1 ubuntu ubuntu   69 May  2 23:04 .gitignore
-rw-rw-r--  1 ubuntu ubuntu   95 May  2 23:04 Dockerfile
-rw-rw-r--  1 ubuntu ubuntu 2047 May  2 23:04 README.md
-rw-rw-r--  1 ubuntu ubuntu  646 May  2 23:04 appspec.yml
-rw-rw-r--  1 ubuntu ubuntu 2146 May  2 23:04 buildspec.yml
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:04 cicd/
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:04 codedeploy/
drwxrwxr-x  5 ubuntu ubuntu 4096 May  2 23:04 deployment/
-rw-rw-r--  1 ubuntu ubuntu 1248 May  2 23:04 pom.xml
-rw-rw-r--  1 ubuntu ubuntu  231 May  2 23:04 sonar-project.properties
drwxrwxr-x  4 ubuntu ubuntu 4096 May  2 23:04 src/
drwxrwxr-x 10 ubuntu ubuntu 4096 May  2 23:06 target/
-rw-rw-r--  1 ubuntu ubuntu  405 May  2 23:10 tomcat-hello-world.Dockerfile

```

Build docker image
```
docker build -t mytomcat-hello-world:1.0 -f tomcat-hello-world.Dockerfile .
```

Create container to run in background and map the host port 8080 to container port 8080
```
docker run -d --name tomcat -p 8080:8080 mytomcat-hello-world:1.0
```

Verify container is running
```
docker ps
```

Verify the application in browser
```
http://ip-address:8080/hello-world
```

CLEANUP:
Deleting the container
```

docker rm -f tomcat
```

### 8. Build a hello world java application and generate the war file
### Write a Dockerfile `official-tomcat.Dockerfile` use official tomcat:9.0 docker image, copy the war file to webapps folder in Dockerfile
### Build the image, create the container and verify hello-world application is running in tomcat on port http://ip-address:8080/hello-world

lets Reuse the same war file
```
ubuntu@vignesh-teaching:~/vignesh/hello-world$ pwd
/home/ubuntu/vignesh/hello-world
```
```
ubuntu@vignesh-teaching:~/vignesh/hello-world$ ll
total 72
drwxrwxr-x  9 ubuntu ubuntu 4096 May  2 23:10 ./
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:04 ../
drwxrwxr-x  8 ubuntu ubuntu 4096 May  2 23:04 .git/
-rw-rw-r--  1 ubuntu ubuntu  269 May  2 23:04 .gitattributes
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:04 .github/
-rw-rw-r--  1 ubuntu ubuntu   69 May  2 23:04 .gitignore
-rw-rw-r--  1 ubuntu ubuntu   95 May  2 23:04 Dockerfile
-rw-rw-r--  1 ubuntu ubuntu 2047 May  2 23:04 README.md
-rw-rw-r--  1 ubuntu ubuntu  646 May  2 23:04 appspec.yml
-rw-rw-r--  1 ubuntu ubuntu 2146 May  2 23:04 buildspec.yml
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:04 cicd/
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:04 codedeploy/
drwxrwxr-x  5 ubuntu ubuntu 4096 May  2 23:04 deployment/
-rw-rw-r--  1 ubuntu ubuntu 1248 May  2 23:04 pom.xml
-rw-rw-r--  1 ubuntu ubuntu  231 May  2 23:04 sonar-project.properties
drwxrwxr-x  4 ubuntu ubuntu 4096 May  2 23:04 src/
drwxrwxr-x 10 ubuntu ubuntu 4096 May  2 23:06 target/
-rw-rw-r--  1 ubuntu ubuntu  405 May  2 23:10 tomcat-hello-world.Dockerfile
```
```
ubuntu@vignesh-teaching:~/vignesh/hello-world$ ll target
total 48
drwxrwxr-x 10 ubuntu ubuntu 4096 May  2 23:06 ./
drwxrwxr-x  9 ubuntu ubuntu 4096 May  2 23:10 ../
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:06 classes/
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:06 generated-sources/
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:06 generated-test-sources/
drwxrwxr-x  4 ubuntu ubuntu 4096 May  2 23:06 hello-world-1.0-SNAPSHOT/
-rw-rw-r--  1 ubuntu ubuntu 5467 May  2 23:06 hello-world-1.0-SNAPSHOT.war
drwxrwxr-x  2 ubuntu ubuntu 4096 May  2 23:06 maven-archiver/
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:06 maven-status/
drwxrwxr-x  2 ubuntu ubuntu 4096 May  2 23:06 surefire-reports/
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:06 test-classes/
```

Create a Dockerfile *official-tomcat.Dockerfile*
```Dockerfile
FROM tomcat:9.0.88-jre11

COPY ./target/hello-world-*.war /usr/local/tomcat/webapps/hello-world.war
```

```
ubuntu@vignesh-teaching:~/vignesh/hello-world$ ll
total 76
drwxrwxr-x  9 ubuntu ubuntu 4096 May  2 23:21 ./
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:04 ../
drwxrwxr-x  8 ubuntu ubuntu 4096 May  2 23:04 .git/
-rw-rw-r--  1 ubuntu ubuntu  269 May  2 23:04 .gitattributes
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:04 .github/
-rw-rw-r--  1 ubuntu ubuntu   69 May  2 23:04 .gitignore
-rw-rw-r--  1 ubuntu ubuntu   95 May  2 23:04 Dockerfile
-rw-rw-r--  1 ubuntu ubuntu 2047 May  2 23:04 README.md
-rw-rw-r--  1 ubuntu ubuntu  646 May  2 23:04 appspec.yml
-rw-rw-r--  1 ubuntu ubuntu 2146 May  2 23:04 buildspec.yml
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:04 cicd/
drwxrwxr-x  3 ubuntu ubuntu 4096 May  2 23:04 codedeploy/
drwxrwxr-x  5 ubuntu ubuntu 4096 May  2 23:04 deployment/
-rw-rw-r--  1 ubuntu ubuntu  100 May  2 23:21 official-tomcat.Dockerfile
-rw-rw-r--  1 ubuntu ubuntu 1248 May  2 23:04 pom.xml
-rw-rw-r--  1 ubuntu ubuntu  231 May  2 23:04 sonar-project.properties
drwxrwxr-x  4 ubuntu ubuntu 4096 May  2 23:04 src/
drwxrwxr-x 10 ubuntu ubuntu 4096 May  2 23:06 target/
-rw-rw-r--  1 ubuntu ubuntu  405 May  2 23:10 tomcat-hello-world.Dockerfile
```

Build docker image
```
docker build -t official-tomcat:1.0 -f official-tomcat.Dockerfile .
```

Create container to run in background and map the host port 8080 to container port 8080
```
docker run -d --name tomcat -p 8080:8080 official-tomcat:1.0
```

Verify container is running
```
docker ps
```

Verify the application in browser
```
http://ip-address:8080/hello-world
```

CLEANUP:
Deleting the container
```

docker rm -f tomcat
```