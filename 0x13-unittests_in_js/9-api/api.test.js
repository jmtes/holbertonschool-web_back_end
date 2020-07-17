const mocha = require('mocha');
const { expect } = require('chai');

const request = require('request');

describe('API', () => {
  describe('GET index', () => {
    it('should return status code 200', (done) => {
      request('http://localhost:7865', (err, res, body) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(200);
      });
      done();
    });

    it('should return correct message', (done) => {
      request('http://localhost:7865', (err, res, body) => {
        if (err) throw err;
        expect(body).to.equal('Welcome to the payment system');
      });
      done();
    });
  });

  describe('GET /cart/:id', () => {
    it('should return status code 200 for numerical IDs', (done) => {
      request('http://localhost:7865/cart/100', (err, res, body) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(200);
      });
      done();
    });

    it('should return correct message', (done) => {
      request('http://localhost:7865/cart/100', (err, res, body) => {
        if (err) throw err;
        expect(res.body).to.equal('Payment methods for cart 100');
      });
      done();
    });

    it('should return 404 for non-numerical IDs', (done) => {
      request('http://localhost:7865/cart/gec', (err, res, body) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(404);
      });
      request('http://localhost:7865/cart/100gecs', (err, res, body) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(404);
      });
      request('http://localhost:7865/cart/gecs100', (err, res, body) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(404);
      });
      request('http://localhost:7865/cart/100gec100', (err, res, body) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(404);
      });
      done();
    });
  });
});
