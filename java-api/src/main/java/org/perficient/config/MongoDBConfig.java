package org.perficient.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;
import org.perficient.repository.EmployeeRepository;
import org.perficient.service.EmployeeService;

@Configuration
@EnableMongoRepositories(basePackageClasses = EmployeeRepository.class)
public class MongoDBConfig implements CommandLineRunner {

    @Autowired
    private EmployeeService employeeService;

    @Override
    public void run(String... args) throws Exception {
        /*employeeService.save(new Employee(1, "Bobby", "Java Developer", 80000));
        employeeService.save(new Employee(2, "Sam", "Dev Ops", 120000));
        employeeService.save(new Employee(3, "Hank", "Human Resources", 65000));*/
    }
}

