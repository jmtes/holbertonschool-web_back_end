export default function appendToEachArrayValue(array, appendString) {
  const arr = array;
  for (const [idx, item] of arr.entries()) {
    arr[idx] = appendString + item;
  }

  return arr;
}
