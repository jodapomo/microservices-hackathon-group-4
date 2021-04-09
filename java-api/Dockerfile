FROM openjdk:11

WORKDIR /app
ADD --chown=gradle:gradle . /app
EXPOSE 8085

USER root  
RUN apt-get update
RUN apt-get -y install dos2unix
RUN find . -type f -print0 | xargs -0 dos2unix

RUN ./gradlew build --stacktrace
RUN mv ./build/libs/java-api-1.0-SNAPSHOT.jar .
RUN wget -O apm-agent.jar https://search.maven.org/remotecontent?filepath=co/elastic/apm/elastic-apm-agent/1.2.0/elastic-apm-agent-1.2.0.jar

CMD ["java","-javaagent:/app/apm-agent.jar", "-Delastic.apm.service_name=service-javaapi", "-Delastic.apm.application_packages=org.perficient", "-Delastic.apm.server_urls=http://apm-server:8200", "-jar", "java-api-1.0-SNAPSHOT.jar"]
