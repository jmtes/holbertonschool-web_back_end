const http = require('http');
const fs = require('fs');

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

const app = http
  .createServer((req, res) => {
    if (req.url === '/' && req.method === 'GET') {
      res.write('Hello Holberton School!');
      res.end();
    } else if (req.url === '/students' && req.method === 'GET') {
      countStudents('database.csv')
        .then(
          // eslint-disable-next-line
          ({ totalStudents, csCount, csStudents, sweCount, sweStudents }) => {
            res.write('This is the list of our students\n');
            res.write(`Number of students: ${totalStudents}\n`);
            res.write(
              // eslint-disable-next-line
              `Number of students in CS: ${csCount}. List: ${csStudents}\n`
            );
            res.write(
              // eslint-disable-next-line
              `Number of students in SWE: ${sweCount}. List: ${sweStudents}`
            );
            res.end();
            // eslint-disable-next-line
          }
        )
        .catch((err) => {
          throw err;
        });
    } else {
      res.end();
    }
  })
  .listen(1245);

module.exports = app;
