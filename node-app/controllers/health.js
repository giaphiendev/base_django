exports.checkHeath = (req, res) => {
  res.send('Welcome to my node js app!!!');
};
const mysql = require('mysql');

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

const testConnectDb = (req, res) => {
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
};
