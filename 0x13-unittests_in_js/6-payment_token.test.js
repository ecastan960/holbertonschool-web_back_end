let getPaymentTokenFromAPI = require('./6-payment_token.js');
const chai = require('chai');

describe('getPaymentTokenFromAPI', () => {
  it('async test', (done) => {
    getPaymentTokenFromAPI(true)
      .then((res) => {
        chai.expect(res).to.include({ data: 'Successful response from the API' });
        done();
      })
      .catch((error) => done(error));
  });
});
