const order = async mealName => {
  console.log(`オーダー: ${mealName}`);

  if (soup.exists()) {
    // スープがあったら
    return cook(mealName); // 作ってreturn → thenのコールバックに渡る
  } else {
    throw new Error('スープないぜ'); // catchのコールバックに渡る
  }
};