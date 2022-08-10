export default function getStudentsByLocation(students, city) {
  const result = students.filter((student) => student.location === city);
  return result;
}
