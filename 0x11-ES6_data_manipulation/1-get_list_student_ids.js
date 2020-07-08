export default function getListStudentIds(array) {
  if (Object.prototype.toString.call(array) === '[object Array]') {
    return array.map((item) => item.id);
  }
  return [];
}
