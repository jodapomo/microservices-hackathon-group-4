FROM openjdk:11
EXPOSE 8085
RUN mkdir -p /app/
ADD build/libs/java-api-1.0-SNAPSHOT.jar /app/java-api-1.0-SNAPSHOT.jar

RUN wget -O apm-agent.jar https://search.maven.org/remotecontent?filepath=co/elastic/apm/elastic-apm-agent/1.2.0/elastic-apm-agent-1.2.0.jar
CMD ["java","-javaagent:/apm-agent.jar", "-Delastic.apm.service_name=service-javaapi", "-Delastic.apm.application_packages=main.java", "-Delastic.apm.server_urls=http://apm-server:8200", "-jar", "/app/java-api-1.0-SNAPSHOT.jar"]
