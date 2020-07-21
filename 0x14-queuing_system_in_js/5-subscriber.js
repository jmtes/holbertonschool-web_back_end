import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('connect', () => console.log('Redis client connected to the server'));

subscriber.on('error', (err) => console.log(`Redis client not connected to the server: ${err.message}`));

subscriber.subscribe('holberton school channel');

subscriber.on('message', function showMessage(channel, message) {
  console.log(message);

  if (message === 'KILL_SERVER') {
    this.unsubscribe(channel);
    process.exit();
  }
});
