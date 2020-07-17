const express = require('express');

const app = express();

app.use(express.json({ extended: false }));

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id([0-9]+)', (req, res) => {
  res.send(`Payment methods for cart ${req.params.id}`);
});

app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

app.post('/login', (req, res) => {
  if (req.body.userName) {
    res.send(`Welcome ${req.body.userName}`);
    return;
  }
  res.status(400).send('Please provide a user name.');
});

app.listen(7865, () => {
  console.log('API available on localhost port 7865');
});
