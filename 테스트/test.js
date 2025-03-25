function oddEven1(x) {
  return x % 2 === 0 ? "짝수" : "홀수";
}
console.log(oddEven1(2));
console.log("=".repeat(50));
const oddEven2 = function (x) {
  if (x % 2 === 0) return console.log("짝수");
  else return console.log("홀수");
};
oddEven2(3);
console.log("=".repeat(50));
const oddEven3 = (x) => {
  if (x % 2 === 0) return console.log("짝수");
  else return console.log("홀수");
};
oddEven3(4);
