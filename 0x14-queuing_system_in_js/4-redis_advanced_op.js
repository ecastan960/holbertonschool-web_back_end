import { createClient } from 'redis';

const client = createClient();
const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

keys.forEach((key, index) => {
  client.hset('HolbertonSchools', key, values[index], redis.print);
});

client.hgetall('HolbertonSchools', (err, res) => {
  console.log(res);
});
