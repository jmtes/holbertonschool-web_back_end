module.exports = function calculateNumber(a, b = 0) {
  const aNum = Number(a);
  const bNum = Number(b);

  if (Number.isNaN(aNum) || Number.isNaN(bNum))
    throw TypeError('Parameters must be numbers or able to coerce to number');

  return Math.round(a) + Math.round(b);
};
