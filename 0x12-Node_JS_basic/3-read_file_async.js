const fs = require('fs');

module.exports = function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, { encoding: 'utf-8' }, (err, data) => {
      if (err) reject(Error('Cannot load the database'));

      let fileData = data;
      fileData = data.split('\n').filter((line) => line).slice(1);

      let csCount = 0;
      let csStudents = '';

      let sweCount = 0;
      let sweStudents = '';

      fileData.forEach((student) => {
        const studentData = student.split(',');

        if (studentData[3] === 'CS') {
          csCount += 1;
          csStudents += csStudents ? `, ${studentData[0]}` : studentData[0];
        } else if (studentData[3] === 'SWE') {
          sweCount += 1;
          sweStudents += sweStudents ? `, ${studentData[0]}` : studentData[0];
        }
      });

      console.log(`Number of students: ${fileData.length}`);
      console.log(`Number of students in CS: ${csCount}. List: ${csStudents}`);
      console.log(`Number of students in SWE: ${sweCount}. List: ${sweStudents}`);
      resolve();
    });
  });
};
