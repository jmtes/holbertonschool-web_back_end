export default function getStudentIdsSum(array) {
  return array.reduce((sum, item) => sum + item.id, 0);
}
