function menu(href) {
    parent.location.href = href;
}

function hist_search() {
    category = document.forms["hist_form"].elements['category'].value;
    os = document.forms["hist_form"].elements['os'].value;
    skil = document.forms["hist_form"].elements['skil'].value;

    parent.frames["hist_body"].document.forms["result_form"].elements['category'].value = category;
    parent.frames["hist_body"].document.forms["result_form"].elements['os'].value = os;
    parent.frames["hist_body"].document.forms["result_form"].elements['skil'].value = skil;
    parent.frames["hist_body"].document.forms["result_form"].submit();

}
