var apm = require("elastic-apm-node").start({
  serviceName: "node-api",
  serverUrl: "http://apm-server:8200",
});

require("dotenv").config();
const express = require("express");
const env = require("./env");
const axios = require("axios");
const cors = require('cors')

const app = express();

app.use(cors());
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

const authenticate = async (username, password) => {
  const params = new URLSearchParams();
  params.append("username", username);
  params.append("password", password);
  const response = await axios.post(`${env.AUTH_API_URL}/auth/`, params, {
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });
  return response.data;
};

const getUser = async (req) => {
  const token = req.header("authorization");
  const response = await axios.get(`${env.AUTH_API_URL}/users/1`, {
    headers: { Authorization: token || "" },
  });
  return response.data;
};

const createUser = async (email, password, name, lastname) => {
  const response = await axios.post(`${env.AUTH_API_URL}/register/`, {
    email,
    name,
    lastname,
    password,
  });
  return response.data;
};

app.get("/", function (req, res) {
  var response = {
    message: "Ok",
  };
  res.json(response);
});

app.post("/login", async (req, res) => {
  try {
    const response = await authenticate(req.body.username, req.body.password);
    res.status(200).json(response);
  } catch (error) {
    const response = error.response;
    if (response) return res.status(response.status).json(response.data);
    return res.status(500).json(error);
  }
});

app.post("/users", async (req, res) => {
  try {
    const response = await createUser(req.body.email, req.body.password, req.body.name, req.body.lastname);
    res.status(200).json(response);
  } catch (error) {
    const response = error.response;
    if (response) return res.status(response.status).json(response.data);
    return res.status(500).json(error);
  }
});

app.get("/employees/:employeeId", async (req, res) => {
  try {
    const { employeeId } = req.params;
    await getUser(req);
    const employee = await axios.get(
      `${env.EMPLOYEES_API_URL}/employee/${employeeId}`
    );
    res.status(200).json(employee.data);
  } catch (error) {
    const response = error.response;
    if (response) return res.status(response.status).json(response.data);
    return res.status(500).json(error);
  }
});

app.get("/employees", async (req, res) => {
  try {
    await getUser(req);
    const employees = await axios.get(
      `${env.EMPLOYEES_API_URL}/employee/allemployees`
    );
    res.status(200).json(employees.data);
  } catch (error) {
    const response = error.response;
    if (response) return res.status(response.status).json(response.data);
    return res.status(500).json(error);
  }
});

app.post("/employees", async (req, res) => {
  try {
    const { id, name, role, salary } = req.body;
    await getUser(req);
    const employee = await axios.post(
      `${env.EMPLOYEES_API_URL}/employee/create`,
      {
        id,
        name,
        role,
        salary,
      }
    );
    res.status(200).json(employee.data);
  } catch (error) {
    const response = error.response;
    if (response) return res.status(response.status).json(response.data);
    return res.status(500).json(error);
  }
});

console.log(`Server listening port: ${env.API_PORT}`);
app.listen(env.API_PORT);
module.exports = app;
