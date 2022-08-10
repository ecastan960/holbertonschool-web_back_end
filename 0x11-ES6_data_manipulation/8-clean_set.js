export default function cleanSet(set, startString) {
  if (!startString) return '';
  let result = '';
  set.forEach((element) => {
    if (element && element.startsWith(startString)) result += `${element.slice(startString.length)}-`;
  });
  return result.slice(0, result.length - 1);
}
