// 料理を受け取るためのコールバック関数
const receiveMeal = meal => {
  console.log(`${meal}ゲットだぜ`);
};
// const receiveMeal = () => {
//   console.log(`なにかゲットだぜ`);
// };

const wait = () => {
  const time = new Date();
  while(new Date - time < 1000){};
}

// 料理が失敗したときのコールバック関数
const failedReceivingMeal = err => {
  console.log(err.message);
};

const order = mealName => {
  console.log(`オーダー: ${mealName}`);
  return new Promise((resolve, reject) => {
    wait()
    console.log(`${mealName} 完成`)
    resolve(mealName);
  });
}
// order関数はPromiseを返す & 料理を行う。
// 調理が終わったら、thenに渡された関数にラーメンを渡す。
// 調理に失敗したら、catchに渡された関数にエラーを渡す。
order('全マシ').then(receiveMeal).catch(failedReceivingMeal);