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
      alert("保存しました。")
      window.location.href="http://127.0.0.1:8000/"
      return
    }
    alert("保存できませんでした。")
  })
}