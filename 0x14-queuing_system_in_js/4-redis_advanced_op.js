import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

const hgetall = promisify(client.hgetall).bind(client);

async function main() {
  const HolbertonSchools = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  for (const prop in HolbertonSchools) {
    // eslint-disable-next-line
    // if (Object.prototype.hasOwnProperty.call(HolbertonSchools, prop)) await redis.hset('HolbertonSchools', prop, HolbertonSchools.prop);

    if (Object.prototype.hasOwnProperty.call(HolbertonSchools, prop)) client.hset('HolbertonSchools', prop, HolbertonSchools[prop], redis.print);
  }

  const hashVal = await hgetall('HolbertonSchools');
  console.log(hashVal);
}

main();
