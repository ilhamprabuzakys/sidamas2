/***=======================================================
* DASHBOARD
* CREATE A NEW INSTANCE OF TAGIFY USING ONLY A CLASSNAME
========================================================***/
$(function () {
    $("input:is(.tagify)").each(function () {
        // console.log('Terdapat tagify :', $(this).get()[0]);
        new Tagify($(this).get()[0]);
    });
});
