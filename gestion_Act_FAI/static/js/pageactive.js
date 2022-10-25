function relief()
{
  var pageurl = location.href;
  var dnl = document.getElementsByTagName("a");
  for(i = 0; i < dnl.length;i++)
  {
    var x = dnl.item(i);
    if(x.href == pageurl) 
    {
      x.style.fontWeight = "bold";
      x.setAttribute("class",x.className+" active")
    }
  }	
}
window.onload=relief; 