import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';
import express from 'express';

const client = redis.createClient();
const set = promisify(client.set).bind(client);
const get = promisify(client.get).bind(client);

let reservationEnabled;

const reserveSeat = async (number) => {
  await set('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const availableSeats = await get('available_seats');
  return availableSeats;
};

const q = kue.createQueue();

const process = async () => {
  q.process('reserve_seat', async (job, done) => {
    let seats = await getCurrentAvailableSeats();

    if (seats <= 0) {
      done(Error('Not enough seats available'));
    } else {
      await reserveSeat(seats - 1);
      seats = await getCurrentAvailableSeats();

      if (seats <= 0) reservationEnabled = false;

      done();
    }
  });
};

const app = express();

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (reservationEnabled === false) {
    res.status(403).json({ status: 'Reservations are blocked' });
    return;
  }

  const newJob = q.create('reserve_seat', {}).save((err) => {
    if (err) {
      res.status(500).json({ status: 'Reservation failed' });
      return;
    }
    res.json({ status: 'Reservation in process' });
  });

  newJob.on('complete', () => console.log(`Seat reservation job ${newJob.id} completed`));

  newJob.on('failed', (err) => console.log(`Seat reservation job ${newJob.id} failed: ${err}`));
});

app.get('/process', (req, res) => {
  process().then(() => res.json({ status: 'Queue processing' }));
});

app.listen(1245, () => {
  reserveSeat(50);
  reservationEnabled = true;
});
