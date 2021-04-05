FROM openjdk:11
EXPOSE 8085
RUN mkdir -p /app/
ADD build/libs/java-api-1.0-SNAPSHOT.jar /app/java-api-1.0-SNAPSHOT.jar
ENTRYPOINT ["java", "-jar", "/app/java-api-1.0-SNAPSHOT.jar"]
