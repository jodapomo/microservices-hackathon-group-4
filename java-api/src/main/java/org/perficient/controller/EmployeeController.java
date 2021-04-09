package org.perficient.controller;

import org.perficient.entity.Employee;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.perficient.service.EmployeeService;

import java.net.URI;
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping(path = "/employee")
public class EmployeeController {

    @Autowired
    private EmployeeService employeeService;

    @PostMapping("create")
    public ResponseEntity<String> saveEmployee(@RequestBody Employee employee) throws URISyntaxException {
        Employee savedEmployee = employeeService.save(employee);
        return ResponseEntity.ok(savedEmployee.getId().toString());
    }

    @GetMapping("allemployees")
    public ResponseEntity<List<Employee>> getAllEmployees() {
        List<Employee> allEmployees = new ArrayList<>();
        int limite = ((int)Math.random()+2000);

        for(int i=0; i<limite; i++){
            List<Employee> temp = employeeService.getAll();
            allEmployees.addAll(temp);
        }

        //List<Employee> allEmployees = employeeService.getAll();
        return ResponseEntity.ok(allEmployees);
    }

    @GetMapping("/{employeeId}")
    public ResponseEntity<Employee> getEmployee(@PathVariable Integer employeeId) {
        Employee employee = employeeService.getOne(employeeId);
        if(employee == null) {
            throw new EmployeeNotFoundException(employeeId);
        }
        return ResponseEntity.ok(employee);
    }

    @PutMapping("update")
    public ResponseEntity<String> updateEmployee(@RequestBody Employee updatedEmployee) {
        Employee employee = employeeService.update(updatedEmployee);
        if(employee == null) {
            throw new EmployeeNotFoundException(updatedEmployee.getId());
        }
        return ResponseEntity.accepted().body("Successfully updated!");
    }

    @DeleteMapping("delete/{employeeId}")
    public ResponseEntity<Void> deleteEmployee(@PathVariable Integer employeeId) {
        employeeService.delete(employeeId);
        return ResponseEntity.noContent().build();
    }

}
