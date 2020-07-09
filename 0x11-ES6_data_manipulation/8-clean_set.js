export default function cleanSet(set, startString) {
  let string = '';

  if (startString && typeof startString === 'string') {
    for (const item of set) {
      if (typeof item === 'string' && item.startsWith(startString)) {
        string += `${item.substring(startString.length)}-`;
      }
    }
  }

  return string.slice(0, -1);
}
