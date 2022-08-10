export default function createInt8TypedArray(length, position, value) {
  const dataview = new DataView(new ArrayBuffer(length), 0);
  if (position > length - 1) throw Error('Position outside range');
  dataview.setInt8(position, value);
  return dataview;
}
