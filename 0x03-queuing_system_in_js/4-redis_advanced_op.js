// 4-redis_advanced_op.js
import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const key = 'HolbertonSchools';
const values = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
};

// Store the hash values
for (const [field, value] of Object.entries(values)) {
  client.hset(key, field, value, redis.print);
}

// Display the hash values
client.hgetall(key, (err, obj) => {
  if (err) {
    console.error(err);
  } else {
    console.log(obj);
  }
});
