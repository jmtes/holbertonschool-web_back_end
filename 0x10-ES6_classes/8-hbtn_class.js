export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number') throw TypeError('size should be a number');
    if (typeof location !== 'string') throw TypeError('location must be a string');

    this._size = size;
    this._location = location;
  }

  [Symbol.toPrimitive](hint) {
    if (hint === 'string') return this._location;
    return this._size;
  }
}
