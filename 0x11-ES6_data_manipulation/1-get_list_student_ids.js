export default function getListStudentIds(array) {
  let result = [];
  if (!Array.isArray(array)) return result;
  result = array.map((el) => el.id);
  return result;
}
