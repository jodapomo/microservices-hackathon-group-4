var apm = require('elastic-apm-node').start({
  serviceName: 'node-api',
  serverUrl: 'http://apm-server:8200'
})

require('dotenv').config();
const express = require('express');
const env = require('./env');
const axios = require('axios');

const app = express();

const getToken = (req) => {
  const bearerHeader = req.headers['authorization'];

  if (bearerHeader) {
    const bearer = bearerHeader.split(' ');
    return bearer[1];
  }

  return ''
}

const authenticate = async (token) => {
  try {
    await axios.get(`${env.AUTH_API_URL}/auth/${token}`);
  } catch (error) {
    throw {
      error,
      message: 'Authentication failed'
    }
  }
}

app.get('/', function(req, res){
  var response = {
    message : 'Ok'
  }
  res.json(response);
})


app.get('/products', async (req, res) => {
  try {
    const token = getToken(req);
    await authenticate(token);
    const products = await axios.get(`${env.UNNAMED_API_URL}/products`);
    res.status(200).json(products);
  } catch (error) {
    console.log(error);
    res.status(500).json(error);
  }
});

app.post('/payments', async (req, res) => {
  try {
    const token = getToken(req);
    await authenticate(token);
    const payment = await axios.post(`${env.UNNAMED_API_URL}/payments`);
    res.status(200).json(payment);
  } catch (error) {
    console.log(error);
    res.status(500).json(error);
  }
});

console.log(`Server listening port: ${env.API_PORT}`);
app.listen(env.API_PORT);
module.exports = app;
