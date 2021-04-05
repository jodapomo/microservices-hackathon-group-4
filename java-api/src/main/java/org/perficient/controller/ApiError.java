package org.perficient.controller;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ApiError {
    private String error;
    private String message;

    public ApiError(String error, String message) {
        this.error = error;
        this.message = message;
    }
}
