const express = require('express');
const mysql = require('mysql');

const app = express();
const PORT_SERVER = process.env.CHAT_APP_PORT || 5005;

// Create connection
const db = mysql.createConnection({
  host: process.env.MYSQL_HOST,
  port: process.env.MYSQL_PORT,
  user: process.env.MYSQL_USER,
  password: process.env.MYSQL_PASSWORD,
  database: process.env.MYSQL_DATABASE,
  dialect: 'mysql',
  pool: {
    max: 5,
    min: 0,
    acquire: 30000,
    idle: 10000,
  },
});

// Connect to MySQL

db.connect((err) => {
  if (err) {
    throw err;
  }
  console.log('MySql Connected');
});

// start define route
app.get('/', function (req, res) {
  res.send('Hello World!');
});

app.get('/get', function (req, res) {

    let sql = `SELECT *  FROM user;`;

    db.query(sql, (err, result, fields) => {
      if (err) {
        throw err;
      }
      console.log('result: ', result[0]['email']);
      console.log('================================================');

      // console.log('fields: ', fields);

      res.send('Getting record!');
    });


});

app.listen(PORT_SERVER, function () {
  console.log(`Example app listening on port ${PORT_SERVER}!`);
  console.log('process.env.CHAT_APP_PORT: ', process.env.CHAT_APP_PORT);
});
