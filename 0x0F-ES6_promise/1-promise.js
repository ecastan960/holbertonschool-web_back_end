export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      const obj = {
        status: 200,
        body: 'success',
      };
      resolve(obj);
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
