export default function cleanSet(set, startString) {
  let string = '';

  if (startString) {
    for (const item of set) {
      if (item.startsWith(startString)) {
        string += `${item.split(startString)[1]}-`;
      }
    }
  }

  return string.slice(0, -1);
}
