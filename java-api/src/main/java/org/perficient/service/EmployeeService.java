package org.perficient.service;

import  org.perficient.entity.Employee;

import java.util.List;

public interface EmployeeService {
    Employee save(Employee employee);
    List<Employee> getAll();
    Employee getOne(Integer id);
    Employee update(Employee updatedEmployee);
    void delete(Integer id);
}
