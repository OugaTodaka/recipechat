const form = document.getElementById("form")
const submitButton = document.getElementById("submit-button")

submitButton.onclick = () => {
  const formData = new FormData(form)
  const action = form.getAttribute("action")
  const options = {
    method: 'POST',
    body: formData,
  }
  fetch(action, options).then((e) => {
    if(e.status === 200) {
      alert("保存しました。検索結果を表示します")
      window.location.href="http://127.0.0.1:8000/"
      return
    }
    alert("保存できませんでした。")
  })
}

document.addEventListener('DOMContentLoaded', () => {
  const chatElement = document.querySelector('.chat');

  // チャットリストをスクロールの最下部に設定
  const scrollToBottom = () => {
      chatElement.scrollTop = chatElement.scrollHeight;
  };

  // ページ読み込み時にスクロール位置を最下部に
  scrollToBottom();

  // 新しいメッセージが追加された際にスクロール
  const observer = new MutationObserver(() => {
      scrollToBottom();
  });

  // チャットリストの変更を監視
  observer.observe(chatElement, { childList: true });

  // 送信ボタンが押されたときにもスクロール
  const submitButton = document.getElementById('submit-button');
  submitButton.addEventListener('click', () => {
      setTimeout(scrollToBottom, 100); // メッセージ送信後にスクロール
  });
});
