// Create connection for redis
const Redis = require('ioredis');

const urlRedis = `${process.env.REDIS_PROTOCOL}://${process.env.REDIS_USER}:${process.env.REDIS_PASSWORD}@${process.env.REDIS_HOST}:${process.env.REDIS_PORT}/0`;
var REDISIO = new Redis(urlRedis);

const CHANNEL_CHAT_REDIS = process.env.CHANNEL_CHAT_REDIS || 'private-chat-app';

const handleOnMessageRedis = (channel, data) => {
  content = JSON.parse(data);

  console.log(`redis.on(message): ${content['message']}`);
  // funcCallBack(content['receiver_id']);
  console.log('>>>>><><>><><<<<<><>>><<><<');

  // if (channel == CHANNEL_CHAT_REDIS) {
  //   let data = message.data.dataMess;
  //   let receiver = data.receiver_username;
  //   let event = message.event;

  // lay socket id of receiver
  // let socketID = '';
  // users.forEach((element) => {
  //   if (element['user_name'] == receiver) {
  //     socketID = element['socket_id'];
  //   }
  // });

  // emit data to receiver
  // SOCKETIO.to(socketID).emit(channel + ':' + event, data);
  // }
  return content['message'];
};

module.exports = {
  CHANNEL_CHAT_REDIS,
  REDISIO,
  handleOnMessageRedis,
};
