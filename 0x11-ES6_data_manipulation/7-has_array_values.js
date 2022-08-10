export default function hasValuesFromArray(set, array) {
  for (const number of array) {
    if (!set.has(number)) return false;
  }
  return true;
}
