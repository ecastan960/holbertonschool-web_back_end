export default function getStudentIdsSum(students) {
  return students.reduce((currentTotal, student) => student.id + currentTotal, 0);
}
