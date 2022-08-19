const chai = require('chai');
let expect = chai.expect;
const request = require('request');

describe('integration testing', () => {
  describe('GET /', () => {
    it('endpoint GET /', (done) => {
      const endpoint = {
        url: 'http://localhost:7865',
        method: 'GET',
      };
      request(endpoint, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });
});
