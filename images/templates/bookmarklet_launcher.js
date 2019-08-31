(function () {
    /*检测是否定义了myBookmaklet变量*/
    /*上述脚本将判读书签工具是否已被加载。当用户重复书签工具时，可避免对其进行重复加载。 */
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    }
    else {
        document.body.appendChild(document.createElement('script')).src='http://127.0.0.1:8000/static/js/bookmarklet.js' +
            '?r='+Math.floor(Math.random()*99999999999999999999);
    }
})();