import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

const client = redis.createClient();

const get = promisify(client.get).bind(client);

function reserveStockById(itemId, stock) {
  client.set(itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await get(itemId);
  return stock;
}

function getItemById(id) {
  let item;

  listProducts.forEach((product) => {
    if (product.itemId === id) item = product;
  });

  return item;
}

const app = express();

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);

  const item = getItemById(itemId);
  const stock = await getCurrentReservedStockById(itemId);

  if (item) {
    item.currentQuantity = stock;
    res.json(item);
    return;
  }

  res.status(404).json({ status: 'Product not found' });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);

  const item = getItemById(itemId);

  if (!item) {
    res.status(404).json({ status: 'Product not found' });
    return;
  }

  const stock = await getCurrentReservedStockById(itemId);

  if (stock < 1) {
    res.status(403).json({ status: 'Not enough stock available', itemId });
    return;
  }

  reserveStockById(itemId);
  res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(1245, () => {
  listProducts.forEach((product) => reserveStockById(product.itemId,
    product.initialAvailableQuantity));
});
