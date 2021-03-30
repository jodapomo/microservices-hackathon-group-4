package org.perficient.controller;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class EmployeeNotFoundException extends RuntimeException {
    private Integer id;
    private String message;

    public EmployeeNotFoundException(Integer id) {
        this.message = "Employee could not be found with id: " + id;
        this.id = id;
    }
}
