export default function updateStudentGradeByCity(students, city, newGrades) {
  const location = students.filter((student) => student.location === city);
  const grades = location.map((loc) => {
    let check = true;
    let result = loc;
    for (const grades of newGrades) {
      if (grades.studentId === loc.id) {
        result = loc;
        result.grade = grades.grade;
        check = false;
      }
    }
    if (check) result.grade = 'N/A';
    return result;
  });
  return grades;
}
