export default function concatArrays(array1, array2, string) {
  const stringArray = string.split('');
  return array1.concat(array2, stringArray);
}
