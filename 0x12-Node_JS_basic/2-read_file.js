const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path,
      { encoding: 'utf8', flag: 'r' });
    const headers = data.slice(0, data.indexOf('\n')).split(',');
    const rows = data.slice(data.indexOf('\n') + 1).split('\n');
    const array = rows.map((row) => {
      const values = row.split(',');
      const el = headers.reduce((object, header, index) => {
        // eslint-disable-next-line
        object[header] = values[index];
        return object;
      }, {});
      return el;
    });
    console.log('Number of students:', array.length);
    let countFieldCS = 0;
    let countFieldSWE = 0;
    let nameCS = 'List:';
    let nameSWE = 'List:';
    for (const student of array) {
      if (student.field === 'CS') {
        countFieldCS += 1;
        nameCS = `${nameCS} ${student.firstname},`;
      }
      if (student.field === 'SWE') {
        countFieldSWE += 1;
        nameSWE = `${nameSWE} ${student.firstname},`;
      }
    }
    console.log(`Number of students in CS: ${countFieldCS}. ${nameCS.slice(0, -1)}`);
    console.log(`Number of students in SWE: ${countFieldSWE}. ${nameSWE.slice(0, -1)}`);
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
