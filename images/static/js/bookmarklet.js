(function () {
    var jquert_version = '3.3.1'
    var site_url ='http://127.0.0.1:8000';
    var static_url = site_url + 'static/';
    var min_width = 100;
    var min_heigth = 100;

    function bookmarklet(msg) {
        //Here goes our bookmarklet code
        //加载css文件
        var css = jQuery('<link>')
        css.attr({
                rel:'stylesheet',
                type:'text/css',
                //使用一个随机数最为参数加载bookmarklet.css样表，防止浏览器返回一份缓存文件
                href:static_url+'css/bookmarklet.css?r='+Math.floor(Math.random()*99999999999999999999)
            });
        jQuery('head').append(css);
        //加载Html
        box_html = '<div id = "bookmarklet"><a href="#" id="close">&time;</a>'+
                '<h1>select an image to bookmark:</h1><div class="image"></div></div>'
        jQuery('body').append(box_html);

        //关闭事件
        //获取包换ID=close 其中他的父元素ID= bookmarklet的父元素
        jQuer('#bookmarklet #close').click(function () {
            jQuery('#bookmarklet').remove();
        })
        //找到图像并且显示它
        jQuery.each(jQuery('img[src$="jpg"]'),function (index,image) {
            if (jQuery(image).width()>=min_width && jQuery(image).height()>=min_heigth)
            {
                image_url = jQuery(image).attr('src')
                jQuery('#bookmarklet.image').append('<a href="#"><img src="'+image_url+'"/></a>');
            }
        });
    };

    //Check if jQuery is loaded
    if (typeof window.jQuery!='undefined'){
        bookmarklet();
    }else {
        var script = document.createElement('script');
        script.src='//ajax.googleapis.com/ajax/lib/jquery/'+jquert_version+'/jquery.min.js';

        document.head.appendChild(script);

        var attempts = 15;
        (function () {

            if(typeof  window.jQuery == 'undefined'){
                if(--attempts > 0) {
                    window.setTimeout(arguments.callee,250)
                }else {
                alert('An error ocurrend while loading jQuery')
                }
            }else {
                bookmarklet()
            }
        })();
    }
})()
//  1PpMcdxKNGTi2dQTr5nOgocQBWc_4LgphQuyhZF2DYoBH6EWT
// ./ngrok authtoken 1PpMcdxKNGTi2dQTr5nOgocQBWc_4LgphQuyhZF2DYoBH6EWT
