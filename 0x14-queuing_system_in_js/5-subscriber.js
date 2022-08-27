import { createClient } from 'redis';

const client = createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const subscription = 'holberton school channel';
client.subscribe(subscription);
client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe(subscription);
    client.quit();
  }
});
