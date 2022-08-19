function getPaymentTokenFromAPI(sucess) {
  if (sucess) return Promise.resolve({ data: 'Successful response from the API' });
}
module.exports = getPaymentTokenFromAPI;