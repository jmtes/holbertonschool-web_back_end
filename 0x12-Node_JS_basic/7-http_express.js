const express = require('express');
const fs = require('fs');

const app = express();
const dbPath = process.argv[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, { encoding: 'utf-8' }, (err, data) => {
      if (err) reject(Error('Cannot load the database'));

      let fileData = data;
      fileData = data
        .split('\n')
        .filter((line) => line)
        .slice(1);

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

      resolve({
        totalStudents: fileData.length,
        csCount,
        csStudents,
        sweCount,
        sweStudents,
      });
    });
  });
}

app.get('/', (req, res) => res.send('Hello Holberton School!'));

app.get('/students', (req, res) => {
  countStudents(dbPath)
    .then(({
      totalStudents, csCount, csStudents, sweCount, sweStudents,
    }) => {
      const header = 'This is the list of our students\n';
      const total = `Number of students: ${totalStudents}\n`;
      const cs = `Number of students in CS: ${csCount}. List: ${csStudents}\n`;
      const swe = `Number of students in SWE: ${sweCount}. List: ${sweStudents}`;

      res.send(header + total + cs + swe);
    })
    .catch((err) => {
      throw err;
    });
});

app.listen(1245);

module.exports = app;
