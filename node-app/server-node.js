const app = require('express')();
const http = require('http').createServer(app);

// import in routes
const routers = require('./routes/health');

// import in routes
const { DATABASE } = require('./utils/mysqlConnect');
const {
  CHANNEL_CHAT_REDIS,
  REDISIO,
  handleOnMessageRedis,
} = require('./utils/chatSocket');
const SOCKETIO = require('socket.io')(http, {
  cors: { credentials: true },
});

// Connect to MySQL
DATABASE.connect((err) => {
  if (err) {
    throw err;
  }
  console.log('MySql Connected');
});

// start define route
app.use('/', routers);

// server listen on port
const PORT_SERVER = process.env.CHAT_APP_PORT || 5005;

http.listen(PORT_SERVER, function () {
  console.log(`Node app listening on port ${PORT_SERVER}!`);
});

// start chat app
var users = [];

// redisio subcribe channel in redis server
REDISIO.subscribe(CHANNEL_CHAT_REDIS, () => {
  console.log(`channel has been subscribe: ${CHANNEL_CHAT_REDIS}`);
});
REDISIO.on('message', (channel, data) => {
  var text = handleOnMessageRedis(channel, data);
  console.log('run throught redisio on message');
  SOCKETIO.emit('typing', text);
});

// socket.io
SOCKETIO.on('connection', (socket) => {
  console.log('on.connection socket.id: ', socket.id);
  socket.on('user_connected', (user_name) => {
    console.log('user_connected ', user_name);
    SOCKETIO.emit('typing', socket.id + ' hien');

    // let tuple = {
    //   user_name: user_name,
    //   socket_id: socket.id,
    // };
    // // get unique element
    // if (users.length > 0) {
    //   users.forEach((element) => {
    //     if (element['user_name'] == tuple['user_name']) {
    //       let id = users.indexOf(element);
    //       // xoa user_name da co trong users
    //       users.splice(id, 1);
    //     }
    //   });
    // }

    // users.push(tuple);

    // emit array of user with status active
    // lay socket id of receiver
    // let socketID = '';
    // users.forEach((element) => {
    //   if (element['user_name'] == '_1admin1') {
    //     socketID = element['socket_id'];
    //   }
    // });
    // SOCKETIO.to(socketID).emit('updateUsers', users);
  });

  // disconnect
  socket.on('disconnect', function () {
    console.log('on.disconnect socket.id: ', socket.id);
    // remove element
    // users.forEach((element) => {
    //   if (element['socket_id'] == socket.id) {
    //     let id = users.indexOf(element);
    //     users.splice(id, 1);
    //   }
    // });
    // update users
    // SOCKETIO.emit('updateUsers', users);
  });
});
