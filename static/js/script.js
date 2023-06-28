function DropDown(el) {
 this.dd = el;
 this.initEvents();
}
DropDown.prototype = {
 initEvents : function() {
 var obj = this;
 }
}


 document.getElementById('dd').on('click', function(event){
 $(this).toggleClass('active');
 event.stopPropagation();
 });