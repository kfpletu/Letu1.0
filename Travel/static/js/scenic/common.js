/*创建函数createXhr*/
 /*目的：为了根据不同的浏览器创建不同*/
function createXhr(){
        if(window.XMLHttpRequest){
            return new XMLHttpRequest();
        }else{
            return new ActiveXObject("Microsoft.XMLHTTP");
        }
    }