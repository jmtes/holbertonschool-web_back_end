export default function hasValuesFromArray(set, array) {
  const difference = new Set(array);
  for (const item of set) {
    difference.delete(item);
  }

  return difference.size === 0;
}
