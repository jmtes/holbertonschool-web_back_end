export default function updateUniqueItems(map) {
  if (Object.prototype.toString.call(map) !== '[object Map]') throw Error('Cannot process');

  map.forEach((val, key) => {
    if (val === 1) map.set(key, 100);
  });

  return map;
}
