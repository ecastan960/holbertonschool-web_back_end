export default function getResponseFromAPI() {
  const p = new Promise((resolve) => {
    const a = 1 + 1;
    if (a === 2) {
      resolve('Success');
    }
  });
  return p;
}
