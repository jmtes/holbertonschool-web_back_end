export default function appendToEachArrayValue(array, appendString) {
  for (const [idx, item] of array.entries()) {
    array[idx] = appendString + item;
  }

  return array;
}
