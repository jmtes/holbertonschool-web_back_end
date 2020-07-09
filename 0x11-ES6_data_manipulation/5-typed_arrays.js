export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer, 0, 10);

  try {
    view.setInt8(position, value);
    return view;
  } catch (err) {
    throw Error('Position outside range');
  }
}
