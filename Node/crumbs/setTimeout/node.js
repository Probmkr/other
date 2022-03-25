const func = () => {
  console.log('This is in func()');
}

console.log('This is before func()');
setTimeout(func, 1000);
console.log('This is after func');