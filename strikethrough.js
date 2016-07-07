var domReady = function(callback) {
        document.readyState === "interactive" || document.readyState === "complete" ? callback() : document.addEventListener("DOMContentLoaded", callback);
};

domReady(function() { 
    items = document.getElementsByClassName("list-item");

    for (i = 0; i < items.length; i++) {
        items[i].addEventListener('change', function(event){
            while(!!event) {
                for (i = 0; i < items.length; i++) {
                    console.log(items[i])
                    event = false;
                }
            }
        })
    }
});
