export default class HolbertonCourse {
  constructor(name, length, students) {
    // Check arg types
    if (typeof name !== 'string') throw TypeError('name must be a string');
    if (typeof length !== 'number') throw TypeError('length must be a number');
    if (Object.prototype.toString.call(students) !== '[object Array]') throw TypeError('students must be an array of strings');
    students.forEach((student) => {
      if (typeof student !== 'string') throw TypeError('students must be an array of strings');
    });

    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName !== 'string') throw TypeError('name must be a string');
    this._name = newName;
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof newLength !== 'number') throw TypeError('length must be a number');
    this._length = newLength;
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (Object.prototype.toString.call(newStudents) !== '[object Array]') throw TypeError('students must be an array of strings');
    newStudents.forEach((student) => {
      if (typeof student !== 'string') throw TypeError('students must be an array of strings');
    });

    this._students = newStudents;
  }
}
