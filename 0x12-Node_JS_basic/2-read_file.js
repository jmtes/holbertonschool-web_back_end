const fs = require('fs');

module.exports = function countStudents(path) {
  try {
    let data = fs.readFileSync(path, { encoding: 'utf-8' });
    data = data.split('\n').filter((line) => line).slice(1);

    let csCount = 0;
    let csStudents = '';

    let sweCount = 0;
    let sweStudents = '';

    data.forEach((student) => {
      const studentData = student.split(',');

      if (studentData[3] === 'CS') {
        csCount += 1;
        csStudents += csStudents ? `, ${studentData[0]}` : studentData[0];
      } else if (studentData[3] === 'SWE') {
        sweCount += 1;
        sweStudents += sweStudents ? `, ${studentData[0]}` : studentData[0];
      }
    });

    console.log(`Number of students: ${data.length}`);
    console.log(`Number of students in CS: ${csCount}. List: ${csStudents}`);
    console.log(`Number of students in SWE: ${sweCount}. List: ${sweStudents}`);
  } catch (err) {
    throw Error('Cannot load the database');
  }
};
