var delete_dtn = document.querySelectorAll(".delete");

delete_dtn.forEach(function(value) {
    console.log(value);
    value.addEventListener('click', function(e) {
        var result = window.confirm('お気に入りから削除します。\nよろしいですか？');
        if(result){
            // 何もしない
        }else{
            // ページ遷移をキャンセル
            e.preventDefault();
            e.stopPropagation();
        }
    });
});