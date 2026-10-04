const fs = require('fs');

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = {};

      lines.slice(1).forEach((line) => {
        const parts = line.split(',');
        if (parts.length >= 4) {
          const firstname = parts[0];
          const field = parts[3];
          if (!students[field]) {
            students[field] = [];
          }
          students[field].push(firstname);
        }
      });

      resolve(students);
    });
  });
}

module.exports = readDatabase;
